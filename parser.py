import pandas as pd
import os

def residential_schema():
    '''Returns two lists, one for residential data spacing and one
    for residential data column headers
    Parameters
    ----------

    Returns
    -------
    r_widths : list of integers
        List of residential data field widths
    r_headers : list of strings
        List of residential data field titles
    '''

    r_widths = [
                7,1,1,1,3,3,2,1,1,1,1,13,1,2,1,2,4,4,2,2,1,1,1,1,2,1,1,1,1,6,6,1,1,
                1,1,1,6,2,1,2,1,1,1,1,2,2,2,4,4,4,4,4,4,
                2,2,2,2,4, # additions 1
                2,2,2,2,4, # additions 2
                2,2,2,2,4, # additions 3
                2,2,2,2,4, # additions 4
                2,2,2,2,4, # additions 5
                2,2,2,2,4, # additions 6
                2,2,2,2,4, # additions 7
                2,2,2,2,4, # additions 8
                1,2,2,4,6,1,1,2,4, # accessory 1
                1,2,2,4,6,1,1,2,4, # accessory 2
                1,2,2,4,6,1,1,2,4, # accessory 3
                1,2,2,4,6,1,1,2,4, # accessory 4
                1,2,2,4,6,1,1,2,4, # accessory 5
                1,1,2,1,1,3,8,9,373,
                ]
    r_columns = [
            'Condo Percent Owernship', 'Grade to Street', 'Topography 1',
            'Topography 2', 'Utilites', 'Street-Features', 'Access', 'Drainage',
            'Traffic', 'Common-Area Pic 9', 'Cama-Well-Site', 'Filler',
            'Bldg-Indicator', 'Story-Hgt', 'External-Wall', 'Style', 'Year-Built',
            'Effective Year', 'Total-All Rooms', 'Bedrooms', 'Recrooms',
            'Number of Full-Baths', 'Number of Half-Baths', 'Additional Fixtures',
            'Total Fixtures', 'Heat-Type', 'Heat-System', 'Heat-Fuel',
            'Physical Condition', 'Recroom Area', 'Basement Area', 'Wood-Stacks',
            'Wood-Openings', 'Free Stdg Fireplace Stacks',
            'Easy Set Fireplace Stacks', 'Number of Basement Garages',
            'Unfinished Area', 'Special Items 1', 'Number of Special Items 1',
            'Special Items 2', 'Number of Special Items 2', 'Grade Factor',
            'Grade-Sign', 'Cost Design Factor', 'Cost Design Percent',
            'Desirability Utility', 'Percent Incomplete', 'Basement Area',
            'First-Floor Area', 'Second-Floor Area', 'Third-Floor Area',
            'Half Floor Area', 'Finished Attic Area ', 'Additions Lower Level',
            'First Floor Additions 1', 'Second Floor Additions 1',
            'Third Floor Additions 1', 'Area of Addition 1', 'Additions Lower Level 1',
            'First Floor Additions 2', 'Second Floor Additions 2',
            'Third Floor Additions 2', 'Area of Addition 2', 'Additions Lower Level 2',
            'First Floor Additions 3', 'Second Floor Additions 3',
            'Third Floor Additions 3', 'Area of Addition 3', 'Additions Lower Level 3',
            'First Floor Additions 4', 'Second Floor Additions 4',
            'Third Floor Additions 4', 'Area of Addition 4', 'Additions Lower Level 4',
            'First Floor Additions 5', 'Second Floor Additions 5',
            'Third Floor Additions 5', 'Area of Addition 5', 'Additions Lower Level 5',
            'First Floor Additions 6', 'Second Floor Additions 6',
            'Third Floor Additions 6', 'Area of Addition 6', 'Additions Lower Level 6',
            'First Floor Additions 7', 'Second Floor Additions 7',
            'Third Floor Additions 7', 'Area of Addition 7', 'Additions Lower Level 7',
            'First Floor Additions 8', 'Second Floor Additions 8',
            'Third Floor Additions 8', 'Area of Addition 8', 'Accessory Type 8',
            'Accessory Type-Sub 1', 'Accessory Quantity 1', 'Accessory Year Built 1',
            'Accessory Area 1', 'Accessory Grade 1', 'Accessory Condition 1',
            'Accessory Percent Good 1', 'Accessory Modifier Code 1', 'Accessory Type 2',
            'Accessory Type-Sub 2', 'Accessory Quantity 2', 'Accessory Year Built 2',
            'Accessory Area 2', 'Accessory Grade 2', 'Accessory Condition 2',
            'Accessory Percent Good 2', 'Accessory Modifier Code 2', 'Accessory Type 3',
            'Accessory Type-Sub 3', 'Accessory Quantity 3', 'Accessory Year Built 3',
            'Accessory Area 3', 'Accessory Grade 3', 'Accessory Condition 3',
            'Accessory Percent Good 3', 'Accessory Modifier Code 3', 'Accessory Type 4',
            'Accessory Type-Sub 4', 'Accessory Quantity 4', 'Accessory Year Built 4',
            'Accessory Area 4', 'Accessory Grade 4', 'Accessory Condition 4',
            'Accessory Percent Good 4', 'Accessory Modifier Code 4', 'Accessory Type 5',
            'Accessory Type-Sub 5', 'Accessory Quantity 5', 'Accessory Year Built 5',
            'Accessory Area 5', 'Accessory Grade 5', 'Accessory Condition 5',
            'Accessory Percent Good 5', 'Accessory Modifier Code 5', 'Condo Type',
            'Condo Style', 'Condo Floor', 'Condo Other', 'Wet-Land',
            'Planned Living Unit', 'Create Date', 'Total Living Area', 'Filler'
                ]

    return r_widths, r_columns


def common_schema():
    '''Creates the field widths and column titles for the shared data
    Parameters
    ----------

    Returns
    -------
    g_width : list of integers
        list of field widths for generic data
    g_columns : list of strings
        list of field titles for generic data
    '''

    g_width = [
            3, 2, 1, 2, 3, 2, 30,30,30,30,16,2,9,30,30,30,10,4,7,8,25,6,2,2,
            5,3,5,1,9,9,9,9,9,9,9,9,9,9,6,6,2,2,16,1,3, 1, 1, 3, 5, 1, 736,
            ]

    g_columns = [
        'Book','Page','Block','Lot','Appendage','Card Number','Owner Line 1',
        'Owner Line 2','Owner Line 3','Owner Line 4','City','State','Zip','Legal1',
        'Legal2','Legal3','Condo Unit Number','Deed-Book','Deed-Page','Deed-Date',
        'Site Street','Street Number','Street Ext','Street Direct','Street Type',
        'Tax-District','Zone','Land-Code','Land-SQFT','Current Land Value',
        'Current Bldg Value','Current Total Value','Land Value Previous',
        'Bldg Value Previous','Total Value Previous','Land Value Previous 2',
        'Bldg Value Previous 2','Total Value Previous 2' ,'Plat Number','Grid Map',
        'Card Number of Cards','Parcel Status','Filler','LCI','Land-Use Code',
        'Multiple-Use Flag','Class Code','Total Living-Units','Neighborhood','Lease-Hold Flag', 'VariableSchema'
        ]

    return g_width, g_columns


def parse_residential():
    ''' this function parses the fixed width data from the Anchorage
    Municipality Property Tax file into a SQLite database

    Parameters
    ----------
    directory : string
        location of fixed width data

    Returns
    '''

    from sqlalchemy import create_engine

    r_engine = create_engine('sqlite:///data/residential.db')

    g_widths, g_columns = common_schema()
    r_width, r_columns = residential_schema()

    years = [2006, 2009, 2012, 2015, 2016]

    for year in years:
        fname = 'data/'+str(year)+'.ascii.bz2'
        df = pd.read_fwf(fname, colspecs='infer', compression='infer', header=None, widths=g_widths, encoding = "ISO-8859-1")

        df.columns = g_columns
        df_r = df[df.LCI == 'R']
        # free up some memory
        del df

        # reset the index after dropping the commercial values
        df_r = df_r.reset_index(drop=True).copy()

        # export the residential-specific string
        df_r.VariableSchema.to_csv(str(year)+'_r_extra.csv', index=False, header=False, encoding = "ISO-8859-1")
        df_r.drop('VariableSchema', axis=1, inplace=True)

        # read in the residential specific information
        df_r2 = pd.read_fwf(str(year)+'_r_extra.csv', header=None, widths=r_width, encoding = "ISO-8859-1")
        df_r2.columns = r_columns

        # delete the interstitial file
        fname = str(year)+'_r_extra.csv'
        os.remove(fname)

        # combine the generic data with the residential data
        df_rf = pd.merge(df_r, df_r2, how='inner', left_index=True, right_index=True)

        # df_rf.to_csv('data/'+year+'_r_final.csv', index=False)
        df_rf.to_sql(str(year), con=r_engine, if_exists='replace', index=False)

if __name__ == '__main__':
    parse_residential()
