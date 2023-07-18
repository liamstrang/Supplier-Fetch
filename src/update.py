import time
import pandas as pd
import os
from pathlib import Path
import coloredlogs, logging

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

today = time.strftime("%d%m%Y")
downloadDir = str(Path.home() / "Downloads")
datafeedDir = downloadDir+'/'+today

def update_leader():
    print("------------------------------")
    logger.warning("LEADER: Updating Feed")
    
    try:
        feed = datafeedDir+"/leader.csv"
        df = pd.read_csv(feed, na_filter=False, encoding = 'unicode_escape')
        df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
        df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)

        df.loc[df['AA'] == ">5", 'AA'] = 15
        df.loc[df['AQ'] == ">5", 'AQ'] = 15
        df.loc[df['AN'] == ">5", 'AN'] = 15
        df.loc[df['AV'] == ">5", 'AV'] = 15
        df.loc[df['AW'] == ">5", 'AW'] = 15

        df.loc[df['AA'] == ">100", 'AA'] = 100
        df.loc[df['AQ'] == ">100", 'AQ'] = 100
        df.loc[df['AN'] == ">100", 'AN'] = 100
        df.loc[df['AV'] == ">100", 'AV'] = 100
        df.loc[df['AW'] == ">100", 'AW'] = 100

        df.loc[df['AA'] == "CALL", 'AA'] = 0
        df.loc[df['AQ'] == "CALL", 'AQ'] = 0
        df.loc[df['AN'] == "CALL", 'AN'] = 0
        df.loc[df['AV'] == "CALL", 'AV'] = 0
        df.loc[df['AW'] == "CALL", 'AW'] = 0

        df.AA = pd.to_numeric(df.AA, errors='coerce')
        df.AQ = pd.to_numeric(df.AQ, errors='coerce')
        df.AN = pd.to_numeric(df.AN, errors='coerce')
        df.AV = pd.to_numeric(df.AV, errors='coerce')
        df.AW = pd.to_numeric(df.AW, errors='coerce')

        df.AA = df.AA.astype(int)
        df.AQ = df.AQ.astype(int)
        df.AN = df.AN.astype(int)
        df.AV = df.AV.astype(int)
        df.AW = df.AW.astype(int)

        df['AT'] = df.loc[:,['AA','AQ', 'AN', 'AV', 'AW']].sum(axis=1)
        df.AT = df.AT.astype(int)
        
        df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True, inplace=True)
        
        df.to_csv(feed, index=False)
        logger.debug("LEADER: Successfully Updated Feed")
    except Exception as e:
        logger.critical(e)

def update_leader_m():
    print("------------------------------")
    logger.warning("LEADER-M: Updating Feed")
    
    try:
        #0 STOCK M
        '''
        feed = datafeedDir+"/leader-m.csv"
        df = pd.read_csv(feed, na_filter=False, encoding = 'unicode_escape')
        df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
        df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
        df['AA'] = 0
        df['AQ'] = 0
        df['AN'] = 0
        df['AV'] = 0
        df['AW'] = 0
        df['AT'] = 0
        
        df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True, inplace=True)
        
        df.to_csv(feed, index=False)
        logger.debug("LEADER-M: Successfully Updated Feed")
        '''
        
        #ACTUAL STOCK MWAVE
        
        feed = datafeedDir+"/leader-m.csv"
        df = pd.read_csv(feed, na_filter=False, encoding = 'unicode_escape')
        df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
        df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)

        df.loc[df['AA'] == ">5", 'AA'] = 15
        df.loc[df['AQ'] == ">5", 'AQ'] = 15
        df.loc[df['AN'] == ">5", 'AN'] = 15
        df.loc[df['AV'] == ">5", 'AV'] = 15
        df.loc[df['AW'] == ">5", 'AW'] = 15

        df.loc[df['AA'] == ">100", 'AA'] = 100
        df.loc[df['AQ'] == ">100", 'AQ'] = 100
        df.loc[df['AN'] == ">100", 'AN'] = 100
        df.loc[df['AV'] == ">100", 'AV'] = 100
        df.loc[df['AW'] == ">100", 'AW'] = 100

        df.loc[df['AA'] == "CALL", 'AA'] = 0
        df.loc[df['AQ'] == "CALL", 'AQ'] = 0
        df.loc[df['AN'] == "CALL", 'AN'] = 0
        df.loc[df['AV'] == "CALL", 'AV'] = 0
        df.loc[df['AW'] == "CALL", 'AW'] = 0

        df.AA = pd.to_numeric(df.AA, errors='coerce')
        df.AQ = pd.to_numeric(df.AQ, errors='coerce')
        df.AN = pd.to_numeric(df.AN, errors='coerce')
        df.AV = pd.to_numeric(df.AV, errors='coerce')
        df.AW = pd.to_numeric(df.AW, errors='coerce')

        df.AA = df.AA.astype(int)
        df.AQ = df.AQ.astype(int)
        df.AN = df.AN.astype(int)
        df.AV = df.AV.astype(int)
        df.AW = df.AW.astype(int)

        df['AT'] = df.loc[:,['AA','AQ', 'AN', 'AV', 'AW']].sum(axis=1)
        df.AT = df.AT.astype(int)
        
        df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True, inplace=True)
        
        df.to_csv(feed, index=False)
        logger.debug("LEADER-M: Successfully Updated Feed")
        
    except:
        logger.critical("LEADER-M: Error Updating Feed - Please do it manually")

def update_compuworld():
    print("------------------------------")
    logger.warning("COMPUWORLD: Updating Feed")

    try:
        feed = datafeedDir+"/compuworld.csv"
        df = pd.read_csv(feed, na_filter=False, encoding = 'unicode_escape')

        df['Stock Qty'] = df['Stock Qty'].replace('', 0)
        df['Stock Qty'] = pd.to_numeric(df['Stock Qty'], errors='coerce')
        df['Stock Qty'] = df['Stock Qty'].astype(int)
        df.loc[df['Stock Qty'] < 0, 'Stock Qty'] = 0

        df.to_csv(feed, index=False)
        logger.debug("COMPUWORLD: Successfully Updated Feed")
    except Exception as e:
        logger.critical(e)

def update_bluechip():
    print("------------------------------")
    logger.warning("BLUECHIP: Updating Feed")

    try:
        feed = datafeedDir+"/bluechip.csv"
        df = pd.read_csv(feed, na_filter=False)

        df['NSW_Qty'] = pd.to_numeric(df['NSW_Qty'], errors='coerce')
        df['VIC_Qty'] = pd.to_numeric(df['VIC_Qty'], errors='coerce')
        df['QLD_Qty'] = pd.to_numeric(df['QLD_Qty'], errors='coerce')
        df['SA_Qty'] = pd.to_numeric(df['SA_Qty'], errors='coerce')
        df['WA_Qty'] = pd.to_numeric(df['WA_Qty'], errors='coerce')

        df['NSW_Qty'] = df['NSW_Qty'].astype(int)
        df['VIC_Qty'] = df['VIC_Qty'].astype(int)
        df['QLD_Qty'] = df['QLD_Qty'].astype(int)
        df['SA_Qty'] = df['SA_Qty'].astype(int)
        df['WA_Qty'] = df['WA_Qty'].astype(int)

        df['NSW_Qty'] = df.loc[:,['NSW_Qty','VIC_Qty', 'QLD_Qty', 'SA_Qty', 'WA_Qty']].sum(axis=1)

        df.to_csv(feed, index=False)
        logger.debug("BLUECHIP: Successfully Updated Feed")
    except:
        logger.critical("BLUECHIP: Error Updating Feed - Please do it manually")

def update_multimedia():
    print("------------------------------")
    logger.warning("MULTIMEDIA: Updating Feed")

    try:
        feed = datafeedDir+"/multimedia.csv"
        df = pd.read_csv(feed, na_filter=False, encoding = 'unicode_escape')
        
        df = df.replace('&quot;', '', regex=True)
        df = df.replace('&amp;', '', regex=True)
        df = df.replace('\'', '', regex=True)
        df = df.replace('"', '', regex=True)
        df = df.replace(';', '', regex=True)

        df.to_csv(feed, index=False)
        logger.debug("MULTIMEDIA: Successfully Updated Feed")
    except:
        logger.critical("MULTIMEDIA: Error Updating Feed - Please do it manually")

def update_mittoni():
    print("------------------------------")
    logger.warning("MITTONI: Updating Feed")

    try:
        feed = datafeedDir+"/mittoni.csv"
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')

        df['Availability NSW'] = pd.to_numeric(df['Availability NSW'], errors='coerce')
        df['Availability Vic'] = pd.to_numeric(df['Availability Vic'], errors='coerce')

        df['Availability NSW'] = df.loc[:,['Availability NSW','Availability Vic']].sum(axis=1)
        df['Availability NSW'] = df['Availability NSW'].astype(int)

        df.loc[df["UPC"] == '','UPC'] = df["EAN"]

        df.to_csv(feed, index=False)
        logger.debug("MITTONI: Successfully Updated Feed")
    except:
        logger.critical("MITTONI: Error Updating Feed - Please do it manually")

def update_powerhouse():
    print("------------------------------")
    logger.warning("POWERHOUSE: Updating Feed")

    try:
        feed = datafeedDir+"/powerhouse.csv"
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')

        df['In stock'] = df['In stock'].astype(int)

        df.to_csv(feed, index=False)
        logger.debug("POWERHOUSE: Successfully Updated Feed")
    except:
        logger.critical("POWERHOUSE: Error Updating Feed - Please do it manually")

def update_force():
    print("------------------------------")
    logger.warning("FORCE: Updating Feed")

    try:
        feed = datafeedDir+"/force.csv"
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')

        df = df.replace('\$', '', regex=True)
        df[' Clearance Price'] = pd.to_numeric(df[' Clearance Price'], errors='coerce')
        df[' Unit Price'] = pd.to_numeric(df[' Unit Price'], errors='coerce')

        df.loc[df[' Clearance Price'] == 0, ' Clearance Price'] = df[' Unit Price']
        df[' Unit Price'] = df[' Clearance Price']

        df.to_csv(feed, index=False)
        logger.debug("FORCE: Successfully Updated Feed")
    except:
        logger.critical("FORCE: Error Updating Feed - Please do it manually")

def update_alloys():
    print("------------------------------")
    logger.warning("ALLOYS: Updating Feed")

    try:
        feed = datafeedDir+"/alloys.csv"
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')

        df['Qty_ADL'] = df['Qty_ADL'].astype(int)
        df['Qty_BNE'] = df['Qty_BNE'].astype(int)
        df['Qty_MEL'] = df['Qty_MEL'].astype(int)
        df['Qty_SYD'] = df['Qty_SYD'].astype(int)

        df['Quantity'] = df['Quantity'].astype(int)

        df['Qty_SYD'] = df.loc[:,['Qty_SYD','Qty_MEL', 'Qty_BNE', 'Qty_ADL']].sum(axis=1)

        df.to_csv(feed, index=False)
        logger.debug("ALLOYS: Successfully Updated Feed")
    except:
        logger.critical("ALLOYS: Error Updating Feed - Please do it manually")

def update_dicker():
    print("------------------------------")
    logger.warning("DICKER: Updating Feed")

    try:
        feed = datafeedDir+"/dicker.csv"
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')
        
        try:
            df['RRPEx'] = df.RRPEx.str.replace(r'\.$', '', regex=True)
            df['DealerEx'] = df.DealerEx.str.replace(r'\.$', '', regex=True)
            
            df['RRPEx'] = df.RRPEx.str.replace(r',', '', regex=True)
            df['DealerEx'] = df.DealerEx.str.replace(r',', '', regex=True)

            df['RRPEx'] = df['RRPEx'].astype(float)
            df['DealerEx'] = df['DealerEx'].astype(float)
        except:
            logger.debug("Prices have already been updated")

        df = df[~df['VendorStockCode'].str.contains('CON')]
        df = df[~df['PrimaryCategory'].str.contains('SERVICES')]
        df = df[~df['PrimaryCategory'].str.contains('SOFTWARE')]
        df = df[~df['SecondaryCategory'].str.contains('WARRANTY')]
        df = df[~df['Type'].str.contains('BundledItem')]
        df = df[~df['Type'].str.contains('SpecialItem')]

        df['StockAvailable'] = pd.to_numeric(df['StockAvailable'], errors='coerce')
        df['StockAvailable'] = df['StockAvailable'].astype(int)
        df.loc[df['StockAvailable'] == 999999999, 'StockAvailable'] = 0

        df.loc[df['ETA'] == "TBA", 'ETA'] = ''

        df.to_csv(feed, index=False)
        logger.debug("DICKER: Successfully Updated Feed")
    except Exception as e:
        logger.critical(e)

def update_synnex():
    print("------------------------------")
    logger.warning("SYNNEX: Updating Feed")

    try:
        feed = datafeedDir+"/synnex.csv"
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')

        df['MOQ'] = pd.to_numeric(df['MOQ'], errors='coerce')
        df = df[df['MOQ'] == 1]

        df = df.drop('LONG_DESCRIPTION', axis=1)
        df = df.drop('NOTES_COMMENTS', axis=1)
        df = df.drop('CATEGORY_OF_PRODUCT_1', axis=1)
        df = df.drop('CATEGORY_OF_PRODUCT_2', axis=1)
        df = df.drop('CATEGORY_OF_PRODUCT_3', axis=1)
        df = df.drop('GOV_BUY_EX', axis=1)
        df = df.drop('GOV_RETAIL_EX', axis=1)
        df = df.drop('URL', axis=1)
        df = df.drop('Image1URL', axis=1)
        df = df.drop('Image2URL', axis=1)
        df = df.drop('Image3URL', axis=1)
        df = df.drop('Image4URL', axis=1)
        df = df.drop('Image5URL', axis=1)
        df = df.drop('TECHNICAL_SPECIFICATIONS', axis=1)

        df.loc[df['AVAILABILITY_M'] == 'B', 'AVAILABILITY_M'] = 0
        df.loc[df['AVAILABILITY_S'] == 'B', 'AVAILABILITY_S'] = 0

        df['AVAILABILITY_M'] = pd.to_numeric(df['AVAILABILITY_M'], errors='coerce')
        df['AVAILABILITY_S'] = pd.to_numeric(df['AVAILABILITY_S'], errors='coerce')
        df['AVAILABILITY_S'] = df.loc[:,['AVAILABILITY_S','AVAILABILITY_M']].sum(axis=1)
        
        df['AVAILABILITY_S'] = df['AVAILABILITY_S'].astype(int)
        df['AVAILABILITY_M'] = df['AVAILABILITY_M'].astype(int)

        df.loc[df["UPC"] == '','UPC'] = df["EAN"]
        df.loc[df["UPC"] == '','UPC'] = df["APN"]

        df.to_csv(feed, index=False)
        logger.debug("SYNNEX: Successfully Updated Feed")
    except Exception as e:
        logger.critical(e)
    
def update_ingram():
    print("------------------------------")
    logger.warning("INGRAM: Updating Feed")
    
    try:
        feed = datafeedDir+"/ingram.csv"
        df = pd.read_csv(feed, na_filter=False)

        df['Customer Price'] = df['Customer Price'].replace(' ', '', regex=True)
        df['Customer Price'] = pd.to_numeric(df['Customer Price'], errors='coerce')
        df['Available Quantity'] = df['Available Quantity'].replace('-', '', regex=True)
        df['Available Quantity'] = df['Available Quantity'].astype(int)

        df.to_csv(feed, index=False)
        logger.debug("INGRAM: Successfully Updated Feed")
    except Exception as e:
        logger.critical(e)

'''
def update_auscomp():
    print("------------------------------")
    logger.warning("AUSCOMP: Updating Feed")

    try:
        feed = datafeedDir+'/auscomp.csv'
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')

        df['AvailableQty'] = df['AvailableQty'].astype(int)

        df['Rocklea'] = 0
        df['Sydney'] = 0

        df['LQ Price'] = pd.to_numeric(df['LQ Price'], errors='coerce')

        df = df[df['LQ Price'] > 0]
 
        df.to_csv(feed, index=False)
        logger.debug("AUSCOMP: Successfully Updated Feed")
    except:
        logger.critical("AUSCOMP: Error Updating Feed - Please do it manually")
'''

def update_auscomp():
    print("------------------------------")
    logger.warning("AUSCOMP: Updating Feed")

    try:
        feed = datafeedDir+'/auscomp.csv'
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')

        df['AvailableQty'] = df.AvailableQty.str.replace(r'\+', '', regex=True)
        df['AvailableQty'] = df['AvailableQty'].astype(int)

        df['Rocklea'] = 0
        df['Sydney'] = 0

        df['Price'] = df.Price.str.replace(r'\,', '', regex=True)
 
        df.to_csv(feed, index=False)
        logger.debug("AUSCOMP: Successfully Updated Feed")
    except:
        logger.critical("AUSCOMP: Error Updating Feed - Please do it manually")


def update_thermaltake():
    print("------------------------------")
    logger.warning("THERMALTAKE: Updating Feed")

    try:
        feed = datafeedDir+'/pricelist.csv'
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')

        df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
        df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)

        df.loc[df['PRICE (EX GST)'] < 500, ['STOCK']] = 0
        df.loc[df['STOCK'] < 0, 'STOCK'] = 0

        df['PRICE (EX GST)'].round(2)
        df['RRP (INC GST)'].round(2)
 
        df.to_csv(feed, index=False)
        os.rename(datafeedDir+'/pricelist.csv', datafeedDir+'/thermaltake.csv')
        logger.debug("THERMALTAKE: Successfully Updated Feed")
    except Exception as e:
        logger.critical("THERMALTAKE: Error Updating Feed - Please do it manually")

def update_leader_yealink():
    print("------------------------------")
    logger.warning("LEADER-YEALINK: Updating Feed")

    try:
        feed = datafeedDir+'/leader-yealink.csv'
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')

        df.drop(df.columns[0], axis=1, inplace=True)
        df.drop(df.columns[0], axis=1, inplace=True)
        df.drop(df.columns[1], axis=1, inplace=True)
        
        df['Cost'] = df.Cost.str.replace(r',', '', regex=True)
        df['Cost'] = df.Cost.str.replace(r'\$', '', regex=True)
        
        df['Syd'] = df.Syd.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Ade'] = df.Ade.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Bris'] = df.Bris.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Melb'] = df.Melb.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Perth'] = df.Perth.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)

        df['Syd'] = df.Syd.str.replace(r'10\+', '15', regex=True)
        df['Ade'] = df.Ade.str.replace(r'10\+', '15', regex=True)
        df['Bris'] = df.Bris.str.replace(r'10\+', '15', regex=True)
        df['Melb'] = df.Melb.str.replace(r'10\+', '15', regex=True)
        df['Perth'] = df.Perth.str.replace(r'10\+', '15', regex=True)

        df['Syd'] = df.Syd.str.replace(r'null', '', regex=True)
        df['Ade'] = df.Ade.str.replace(r'null', '', regex=True)
        df['Bris'] = df.Bris.str.replace(r'null', '', regex=True)
        df['Melb'] = df.Melb.str.replace(r'null', '', regex=True)
        df['Perth'] = df.Perth.str.replace(r'null', '', regex=True)
        df['Cost'] = df.Cost.str.replace(r'null', '999', regex=True)

        df.replace('', 0, inplace=True)

        df['Syd'] = pd.to_numeric(df['Syd'], errors='coerce')
        df['Ade'] = pd.to_numeric(df['Ade'], errors='coerce')
        df['Bris'] = pd.to_numeric(df['Bris'], errors='coerce')
        df['Melb'] = pd.to_numeric(df['Melb'], errors='coerce')
        df['Perth'] = pd.to_numeric(df['Perth'], errors='coerce')


        df['Syd'] = df.loc[:,['Syd','Ade', 'Bris', 'Melb', 'Perth']].sum(axis=1)

        df[['ProductLink','SKU']] = df['ProductLink'].str.split('              Man. sku: ',expand=True)
        df = df[['ProductLink', 'SKU', 'Cost', 'Syd', 'Ade', 'Bris', 'Melb', 'Perth']]
        
        df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True, inplace=True)
        
        df.to_csv(feed, index=False)
        logger.debug("LEADER-YEALINK: Successfully Updated Feed")
    except Exception as e:
        logger.critical("LEADER-YEALINK: Error Updating Feed - Please do it manually")

def update_leader_plantronics():
    print("------------------------------")
    logger.warning("LEADER-PLANTRONICS: Updating Feed")

    try:
        feed = datafeedDir+'/leader-plantronics.csv'
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')

        df.drop(df.columns[0], axis=1, inplace=True)
        df.drop(df.columns[0], axis=1, inplace=True)
        df.drop(df.columns[1], axis=1, inplace=True)
        
        df['Cost'] = df.Cost.str.replace(r',', '', regex=True)
        df['Cost'] = df.Cost.str.replace(r'\$', '', regex=True)
        
        df['Syd'] = df.Syd.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Ade'] = df.Ade.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Bris'] = df.Bris.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Melb'] = df.Melb.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Perth'] = df.Perth.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)

        df['Syd'] = df.Syd.str.replace(r'10\+', '15', regex=True)
        df['Ade'] = df.Ade.str.replace(r'10\+', '15', regex=True)
        df['Bris'] = df.Bris.str.replace(r'10\+', '15', regex=True)
        df['Melb'] = df.Melb.str.replace(r'10\+', '15', regex=True)
        df['Perth'] = df.Perth.str.replace(r'10\+', '15', regex=True)

        df['Syd'] = df.Syd.str.replace(r'null', '', regex=True)
        df['Ade'] = df.Ade.str.replace(r'null', '', regex=True)
        df['Bris'] = df.Bris.str.replace(r'null', '', regex=True)
        df['Melb'] = df.Melb.str.replace(r'null', '', regex=True)
        df['Perth'] = df.Perth.str.replace(r'null', '', regex=True)
        df['Cost'] = df.Cost.str.replace(r'null', '999', regex=True)

        df.replace('', 0, inplace=True)

        df['Syd'] = pd.to_numeric(df['Syd'], errors='coerce')
        df['Ade'] = pd.to_numeric(df['Ade'], errors='coerce')
        df['Bris'] = pd.to_numeric(df['Bris'], errors='coerce')
        df['Melb'] = pd.to_numeric(df['Melb'], errors='coerce')
        df['Perth'] = pd.to_numeric(df['Perth'], errors='coerce')


        df['Syd'] = df.loc[:,['Syd','Ade', 'Bris', 'Melb', 'Perth']].sum(axis=1)

        df[['ProductLink','SKU']] = df['ProductLink'].str.split('              Man. sku: ',expand=True)
        df = df[['ProductLink', 'SKU', 'Cost', 'Syd', 'Ade', 'Bris', 'Melb', 'Perth']]
        
        df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True, inplace=True)

        df.to_csv(feed, index=False)
        logger.debug("LEADER-PLANTRONICS: Successfully Updated Feed")
    except Exception as e:
        logger.critical("LEADER-PLANTRONICS: Error Updating Feed - Please do it manually")

def update_leader_cygnett():
    print("------------------------------")
    logger.warning("LEADER-CYGNETT: Updating Feed")

    try:
        feed = datafeedDir+'/leader-cygnett.csv'
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')

        df.drop(df.columns[0], axis=1, inplace=True)
        df.drop(df.columns[0], axis=1, inplace=True)
        df.drop(df.columns[1], axis=1, inplace=True)
        
        df['Cost'] = df.Cost.str.replace(r',', '', regex=True)
        df['Cost'] = df.Cost.str.replace(r'\$', '', regex=True)
        
        df['Syd'] = df.Syd.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Ade'] = df.Ade.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Bris'] = df.Bris.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Melb'] = df.Melb.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Perth'] = df.Perth.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)

        df['Syd'] = df.Syd.str.replace(r'10\+', '15', regex=True)
        df['Ade'] = df.Ade.str.replace(r'10\+', '15', regex=True)
        df['Bris'] = df.Bris.str.replace(r'10\+', '15', regex=True)
        df['Melb'] = df.Melb.str.replace(r'10\+', '15', regex=True)
        df['Perth'] = df.Perth.str.replace(r'10\+', '15', regex=True)

        df['Syd'] = df.Syd.str.replace(r'null', '', regex=True)
        df['Ade'] = df.Ade.str.replace(r'null', '', regex=True)
        df['Bris'] = df.Bris.str.replace(r'null', '', regex=True)
        df['Melb'] = df.Melb.str.replace(r'null', '', regex=True)
        df['Perth'] = df.Perth.str.replace(r'null', '', regex=True)
        df['Cost'] = df.Cost.str.replace(r'null', '999', regex=True)

        df.replace('', 0, inplace=True)

        df['Syd'] = pd.to_numeric(df['Syd'], errors='coerce')
        df['Ade'] = pd.to_numeric(df['Ade'], errors='coerce')
        df['Bris'] = pd.to_numeric(df['Bris'], errors='coerce')
        df['Melb'] = pd.to_numeric(df['Melb'], errors='coerce')
        df['Perth'] = pd.to_numeric(df['Perth'], errors='coerce')


        df['Syd'] = df.loc[:,['Syd','Ade', 'Bris', 'Melb', 'Perth']].sum(axis=1)

        df[['ProductLink','SKU']] = df['ProductLink'].str.split('              Man. sku: ',expand=True)
        df = df[['ProductLink', 'SKU', 'Cost', 'Syd', 'Ade', 'Bris', 'Melb', 'Perth']]
        
        df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True, inplace=True)

        df.to_csv(feed, index=False)
        logger.debug("LEADER-CYGNETT: Successfully Updated Feed")
    except Exception as e:
        logger.critical("LEADER-CYGNETT: Error Updating Feed - Please do it manually")

def update_leader_brateck():
    print("------------------------------")
    logger.warning("LEADER-BRATECK: Updating Feed")

    try:
        feed = datafeedDir+'/leader-brateck.csv'
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')

        df.drop(df.columns[0], axis=1, inplace=True)
        df.drop(df.columns[0], axis=1, inplace=True)
        df.drop(df.columns[1], axis=1, inplace=True)
        
        df['Cost'] = df.Cost.str.replace(r',', '', regex=True)
        df['Cost'] = df.Cost.str.replace(r'\$', '', regex=True)
        
        df['Syd'] = df.Syd.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Ade'] = df.Ade.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Bris'] = df.Bris.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Melb'] = df.Melb.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)
        df['Perth'] = df.Perth.str.replace(r'^(([0-9])|([0-2][0-9])|([3][0-1]))(nd|st|rd|th)\ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\ \d{2}$', '0', regex=True)

        df['Syd'] = df.Syd.str.replace(r'10\+', '15', regex=True)
        df['Ade'] = df.Ade.str.replace(r'10\+', '15', regex=True)
        df['Bris'] = df.Bris.str.replace(r'10\+', '15', regex=True)
        df['Melb'] = df.Melb.str.replace(r'10\+', '15', regex=True)
        df['Perth'] = df.Perth.str.replace(r'10\+', '15', regex=True)

        df['Syd'] = df.Syd.str.replace(r'null', '', regex=True)
        df['Ade'] = df.Ade.str.replace(r'null', '', regex=True)
        df['Bris'] = df.Bris.str.replace(r'null', '', regex=True)
        df['Melb'] = df.Melb.str.replace(r'null', '', regex=True)
        df['Perth'] = df.Perth.str.replace(r'null', '', regex=True)
        df['Cost'] = df.Cost.str.replace(r'null', '999', regex=True)

        df.replace('', 0, inplace=True)

        df['Syd'] = pd.to_numeric(df['Syd'], errors='coerce')
        df['Ade'] = pd.to_numeric(df['Ade'], errors='coerce')
        df['Bris'] = pd.to_numeric(df['Bris'], errors='coerce')
        df['Melb'] = pd.to_numeric(df['Melb'], errors='coerce')
        df['Perth'] = pd.to_numeric(df['Perth'], errors='coerce')


        df['Syd'] = df.loc[:,['Syd','Ade', 'Bris', 'Melb', 'Perth']].sum(axis=1)

        df[['ProductLink','SKU']] = df['ProductLink'].str.split('              Man. sku: ',expand=True)
        df = df[['ProductLink', 'SKU', 'Cost', 'Syd', 'Ade', 'Bris', 'Melb', 'Perth']]
        
        df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True, inplace=True)

        df.to_csv(feed, index=False)
        logger.debug("LEADER-BRATECK: Successfully Updated Feed")
    except Exception as e:
        logger.critical(e)

def update_anixter():
    print("------------------------------")
    logger.warning("ANIXTER: Updating Feed")

    try:
        feed = datafeedDir+'/anixter.csv'
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')

        df.drop(df.columns[0], axis=1, inplace=True)
        df.drop(df.columns[0], axis=1, inplace=True)
        df.drop(df.columns[0], axis=1, inplace=True)
        df.drop(df.columns[0], axis=1, inplace=True)
        
        df['Price'] = df.Price.str.replace(r'A\$', '', regex=True)

        df['Stock'] = df.Stock.str.replace(r' Each in stock', '', regex=True)
        df['Stock'] = df.Stock.str.replace(r' Pack in stock', '', regex=True)
        
        df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True, inplace=True)
 
        df.to_csv(feed, index=False)
        logger.debug("ANIXTER: Successfully Updated Feed")
    except:
        logger.critical("ANIXTER: Error Updating Feed - Please do it manually")

def update_dynamicsupplies():
    print("------------------------------")
    logger.warning("DYNAMIC SUPPLIES: Updating Feed")

    try:
        feed = datafeedDir+'/dynamicsupplies.csv'
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')

        df.columns = ["DS Code", "Description", "Cost Ex", "Manufacturer Name", "Category Description", "Product Weight", 
                    "OEM Code", "Printer Compatibility", "Cartridge Yield", "Cartridge Type", "Cubic", "Region Code", "Length", 
                    "Width", "Height", "SOH Brisbane", "SOH Melbourne", "SOH Perth", "SOH Adelaide", "SOH Sydney", "GTIN", "RRP",
                    "Warranty", "Active", "Date Added"
                ]

        df.drop(df.columns[7], axis=1, inplace=True)
        df.drop(df.columns[7], axis=1, inplace=True)
        df.drop(df.columns[7], axis=1, inplace=True)

        df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
        df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
        df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)

        df.loc[df['SOH Brisbane'] == ">100", 'SOH Brisbane'] = 150
        df.loc[df['SOH Melbourne'] == ">100", 'SOH Melbourne'] = 150
        df.loc[df['SOH Perth'] == ">100", 'SOH Perth'] = 150
        df.loc[df['SOH Adelaide'] == ">100", 'SOH Adelaide'] = 150
        df.loc[df['SOH Sydney'] == ">100", 'SOH Sydney'] = 150

        df['SOH Brisbane'] = pd.to_numeric(df['SOH Brisbane'], errors='coerce')
        df['SOH Melbourne'] = pd.to_numeric(df['SOH Melbourne'], errors='coerce')
        df['SOH Perth'] = pd.to_numeric(df['SOH Perth'], errors='coerce')
        df['SOH Adelaide'] = pd.to_numeric(df['SOH Adelaide'], errors='coerce')
        df['SOH Sydney'] = pd.to_numeric(df['SOH Sydney'], errors='coerce')

        df['Cost Ex'] = pd.to_numeric(df['Cost Ex'], errors='coerce')

        df['SOH Sydney'] = df.loc[:,['SOH Brisbane','SOH Melbourne', 'SOH Perth', 'SOH Adelaide', 'SOH Sydney']].sum(axis=1)
 
        df.to_csv(feed, index=False)
        logger.debug("DYNAMIC SUPPLIES: Successfully Updated Feed")
    except Exception as e:
        logger.critical(e)

def update_newmagic():
    print("------------------------------")
    logger.warning("NEWMAGIC: Updating Feed")

    try:
        feed = datafeedDir+'/newmagic.csv'
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')
        
        df['DealerEx'] = df['DealerEx'].str.replace('$', '')
        df['DealerEx'] = pd.to_numeric(df['DealerEx'], errors='coerce')

        df['UPC'] = df.UPC.str.replace(r'[^0-9]', '', regex=True)

        df['Stock'] = 1
 
        df.to_csv(feed, index=False)
        logger.debug("NEWMAGIC: Successfully Updated Feed")
    except Exception as e:
        logger.critical(e)

def update_streakwave():
    print("------------------------------")
    logger.warning("STREAKWAVE: Updating Feed")

    try:
        feed = datafeedDir+'/streakwave.csv'
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')
        
        df['stock_on_hand'] = df['stock_on_hand'].astype(int)
 
        df.to_csv(feed, index=False)
        logger.debug("STREAKWAVE: Successfully Updated Feed")
    except Exception as e:
        logger.critical(e)

def update_hyka():
    print("------------------------------")
    logger.warning("HYKA: Updating Feed")

    try:
        feed = datafeedDir+'/hyka.csv'
        df = pd.read_csv(feed, na_filter=False, encoding='unicode_escape')
        
        df.loc[df['Stock'] < 0, 'Stock'] = 0
 
        df.to_csv(feed, index=False)
        logger.debug("HYKA: Successfully Updated Feed")
    except Exception as e:
        logger.critical(e)
    

def update():
   update_auscomp()
   update_ingram()
   update_synnex()
   update_dicker()
   update_alloys()
   update_force()
   update_powerhouse()
   update_multimedia()
   update_bluechip()
   update_compuworld()
   update_leader()
   update_leader_m()
   update_mittoni()
   update_dynamicsupplies()
   update_newmagic()
   update_streakwave()
   update_hyka()
   update_leader_yealink()
   update_leader_plantronics()
   update_leader_cygnett()
   update_leader_brateck()
   update_anixter()
   update_thermaltake()
   
   
