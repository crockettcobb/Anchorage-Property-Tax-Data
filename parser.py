import pandas as pd
import os


def parse(commercial_parse=True, residential_parse=True):
    ''' this function parses the fixed width data from the Anchorage
    Municipality Property Tax file into a SQLite database

    Parameters
    ----------
    directory : string
        location of fixed width data

    Returns
    '''
    from sqlalchemy import create_engine

    r_engine = create_engine('sqlite:///data/processed/SQLite/residential.db')
    c_engine = create_engine('sqlite:///data/processed/SQLite/commercial.db')

    general = pd.read_csv('schema/general.csv',nrows=2, header=0)
    residential = pd.read_csv('schema/residential_specific_headers.csv',nrows=2, header=0)
    commercial = pd.read_csv('schema/commercial_specific_headers.csv',nrows=2, header=0)

    g_widths = general.iloc[0].values.tolist()
    g_columns = general.columns
    assert len(g_widths) == len(g_columns)

    r_widths = residential.iloc[0].values.tolist()
    r_columns = residential.columns
    assert len(r_widths) == len(r_columns)

    c_widths = commercial.iloc[0].values.tolist()
    c_columns = commercial.columns
    assert len(c_widths) == len(c_columns)

    years = [2006, 2009, 2012, 2015, 2016]
    year = 2006
    for year in years:
        fname = 'data/raw/'+str(year)+'.ascii.bz2'
        df = pd.read_fwf(fname, colspecs='infer', compression='infer', header=None, widths=g_widths, encoding = "ISO-8859-1")

        df.columns = g_columns
        df_r = df[df.LCI == 'R']
        df_c = df[df.LCI == 'C']
        # free up some memory
        del df

        # reset the index after dropping the commercial values
        df_r = df_r.reset_index(drop=True).copy()
        df_c = df_c.reset_index(drop=True).copy()

        if residential_parse:
            # export the residential-specific string
            df_r.VariableSchema.to_csv(str(year)+'_r_extra.csv', index=False, header=False, encoding = "ISO-8859-1")
            df_r.drop('VariableSchema', axis=1, inplace=True)

            # read in the residential specific information
            df_r2 = pd.read_fwf(str(year)+'_r_extra.csv', header=None, widths=r_widths, encoding = "ISO-8859-1")
            df_r2.columns = r_columns

            # delete the interstitial file
            fname = str(year)+'_r_extra.csv'
            os.remove(fname)

            # combine the generic data with the residential data
            df_rf = pd.merge(df_r, df_r2, how='inner', left_index=True, right_index=True)
            assert len(df_rf) == len(df_r) == len(df_r2)

            # df_rf.to_csv('data/'+year+'_r_final.csv', index=False)
            df_rf.to_sql(str(year), con=r_engine, if_exists='replace', index=False)

        if commercial_parse:
            # export the commercial-specific string
            df_c.VariableSchema.to_csv(str(year)+'_c_extra.csv', index=False, header=False, encoding = "ISO-8859-1")
            df_c.drop('VariableSchema', axis=1, inplace=True)

            # read in the commercial specific information
            df_c2 = pd.read_fwf(str(year)+'_c_extra.csv', header=None, widths=c_widths, encoding = "ISO-8859-1")
            df_c2.columns = c_columns

            # delete the interstitial file
            fname = str(year)+'_c_extra.csv'
            os.remove(fname)

            # combine the generic data with the commercial specific data
            df_cf = pd.merge(df_c, df_c2, how='inner', left_index=True, right_index=True)
            assert len(df_cf) == len(df_c) == len(df_c2)

            # df_cf.to_csv('data/processed/csv/'+str(year)+'_c_final.csv', index=False)
            df_cf.to_sql(str(year), con=c_engine, if_exists='replace', index=False)


if __name__ == '__main__':
    parse()
