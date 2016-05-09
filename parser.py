import pandas as pd


def parse(directory):
    ''' this function parses the fixed width data from the Anchorage
    Municipality Property Tax file into a SQLite database

    Parameters
    ----------
    directory : string
        location of fixed width data

    Returns
    '''

    from sqlalchemy import create_engine

    widths = [
        3, 2, 1, 2, 3, 2, 30,30,30,30,16,2,9,30,30,30,10,4,7,8,25,6,2,2,5,3,5,1,9,9,9,9,9,9,9,
        9,9,9,6,6,2,2,16,1,3, 1, 1, 3, 5, 1, 736,
        ]

year = '2006'
fname = year+'.ascii'
df = pd.read_fwf(fname, colspecs='infer', compression='infer',
        header=None, widths=widths)

df.columns = [
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
df.head(5)

df.head(5).to_csv('test.csv')

df_r = df[df.LCI == 'R']
df_c = df[df.LCI == 'C']

df_r.to_csv(year+'_r.csv')
r_width = [
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
df_r.VariableSchema.to_csv(year+'_r_extra.csv', index=False, index_label=False, header=False)
df_r_extra = pd.read_fwf(year+'_r_extra.csv', header=None, widths=r_width)
df_r_extra.to_csv(year+'_r_extra_formatted.csv')
