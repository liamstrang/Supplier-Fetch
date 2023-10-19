import requests
import time
import os
import zipfile
import io
import pandas as pd
from imap_tools import MailBox, A
import datetime
import ftplib
from pathlib import Path
import coloredlogs, logging
from dateutil import parser

import getenv

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

today = time.strftime("%d%m%Y")
downloadDir = str(Path.home() / "Downloads")
datafeedDir = downloadDir+'/'+today

def create_directory():
    if not os.path.exists(datafeedDir):
        os.makedirs(datafeedDir)
        logger.debug("Created new directory: "+datafeedDir)
        print(30*"-")
    else:
        logger.critical("Directory already exists")
        print(30*"-")

def create_missing_supplier():
    try:
        try:
            os.remove(datafeedDir+'/'+today+'-missing.csv')
            logger.critical("Deleted previous link file")
            print(30*"-")
        except:
            logger.debug("Previous missing file does not exist")
            print(30*"-")
        df = pd.DataFrame(columns = ["Product Code/SKU", "Missing Supplier Code", "Supplier"])
        df.to_csv(datafeedDir+'/'+today+'-missing.csv', index=False)
        logger.debug("Created missing supplier file: "+datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_leader_m():
    print(30*"-")
    logger.critical("LEADER - M")
    print(30*"-")
    print(30*"-")

    feed = getenv.LEADER_M_FEED
    try:
        logger.warning("Trying to Download Leader - M Feed")
        print(30*"-")
        r = requests.get(feed)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        fileName = ''.join(z.namelist())
        z.extractall(datafeedDir)
        try:
            os.remove(datafeedDir+'/leader-m.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        os.rename(datafeedDir+"/"+fileName, datafeedDir+'/leader-m.csv')
        logger.debug("Successfully downloaded Leader-M to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_leader():
    print(30*"-")
    logger.critical("LEADER")
    print(30*"-")
    print(30*"-")

    feed = getenv.LEADER_FEED
    try:
        logger.warning("Trying to Download Leader Feed")
        print(30*"-")
        r = requests.get(feed)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        fileName = ''.join(z.namelist())
        z.extractall(datafeedDir)
        try:
            os.remove(datafeedDir+'/leader.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        os.rename(datafeedDir+"/"+fileName, datafeedDir+'/leader.csv')
        logger.debug("Successfully downloaded Leader to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_compuworld():
    print(30*"-")
    logger.critical("COMPUWORLD")
    print(30*"-")
    print(30*"-")

    feed = getenv.CW_FEED
    try:
        logger.warning("Trying to Download Compuworld Feed")
        print(30*"-")
        r = requests.get(feed)
        try:
            os.remove(datafeedDir+'/compuworld.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        open(datafeedDir+'/compuworld.csv', 'wb').write(r.content)
        logger.debug("Successfully downloaded Compuworld to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_bluechip():
    print(30*"-")
    logger.critical("BLUECHIP")
    print(30*"-")
    print(30*"-")

    feed = getenv.BL_FEED
    try:
        logger.warning("Trying to Download Bluechip Feed")
        print(30*"-")
        r = requests.get(feed)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        fileName = ''.join(z.namelist())
        z.extractall(datafeedDir)
        try:
            os.remove(datafeedDir+'/bluechip.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        os.rename(datafeedDir+"/"+fileName, datafeedDir+'/bluechip.csv')
        logger.debug("Successfully downloaded Bluechip to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_multimedia():
    print(30*"-")
    logger.critical("MULTIMEDIA TECHNOLOGY")
    print(30*"-")
    print(30*"-")

    feed = getenv.MMT_FEED
    try:
        logger.warning("Trying to Download MMT Feed")
        print(30*"-")
        r = requests.get(feed)
        try:
            os.remove(datafeedDir+'/multimedia.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        open(datafeedDir+'/multimedia.csv', 'wb').write(r.content)
        logger.debug("Successfully downloaded MMT to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_mittoni():
    print(30*"-")
    logger.critical("MITTONI")
    print(30*"-")
    print(30*"-")

    loginURL = "https://www.mittoni.com.au/login.php/action/process"
    feed = "https://www.mittoni.com.au/download_price.php"

    s = requests.Session()
    loginheaders = {
        'authority': 'www.mittoni.com.au',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://www.mittoni.com.au',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.mittoni.com.au/login.php',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'cookie_test=please_accept_for_session; layout=classic; sid=35a09821dc3a20109444556b8d53e07e',
    }

    data = {
        'email_address': getenv.MITTONI_USERNAME,
        'password': getenv.MITTONI_PASSWORD,
        'x': '40',
        'y': '13'
    }

    r = s.post(loginURL, headers=loginheaders, data=data)

    headers = {
        'authority': 'www.mittoni.com.au',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.mittoni.com.au/account.php',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'cookie_test=please_accept_for_session; layout=classic; sid='+s.cookies.get_dict()['sid'],
    }

    params = (
        ('f', 'Mittoni_Pricelist.csv'),
    )

    try:
        logger.warning("Trying to Download Mittoni Feed")
        print(30*"-")
        r = requests.get(feed, headers=headers, params=params)
        try:
            os.remove(datafeedDir+'/mittoni.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        open(datafeedDir+'/mittoni.csv', 'wb').write(r.content)
        logger.debug("Successfully downloaded Mittoni to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_powerhouse():
    print(30*"-")
    logger.critical("POWERHOUSE PC")
    print(30*"-")
    print(30*"-")

    feed = getenv.PHPC_FEED
    try:
        logger.warning("Trying to Download the Powerhouse Feed")
        print(30*"-")
        r = requests.get(feed)
        try:
            os.remove(datafeedDir+'/powerhouse.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        open(datafeedDir+'/powerhouse.csv', 'wb').write(r.content)
        logger.debug("Successfully downloaded Powerhouse to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_ijk():
    print(30*"-")
    logger.critical("IJK")
    print(30*"-")
    print(30*"-")

    loginURL = "https://www.ijk.com.au/branch/ijk/login.php?action=process"
    feed = "https://www.ijk.com.au/branch/ijk/price_list_xls.php"

    headers = {
        'authority': 'www.ijk.com.au',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.ijk.com.au/branch/ijk/price_list.php',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'cookie_test=please_accept_for_session; osCsid=44e9c9b4ba1f8c9bbdbbbe3864338db9; __utma=243892573.1799448952.1627459111.1627459111.1627459111.1; __utmz=243892573.1627459111.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    }

    s = requests.Session()
    data = {
        "email_address": getenv.IJK_USERNAME,
        "password": getenv.IJK_PASSWORD,
        "x": 42,
        "y": 4
    }
    s.post(loginURL, headers=headers, data=data)

    try:
        logger.warning("Trying to Download IJK Feed")
        print(30*"-")
        r = s.get(feed)
        try:
            os.remove(datafeedDir+'/ijk.xls')
            os.remove(datafeedDir+'/ijk.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        open(datafeedDir+'/ijk.xls', 'wb').write(r.content)
        data_xls = pd.read_html(datafeedDir+'/ijk.xls', index_col=None)
        data_xls[0].to_csv(datafeedDir+'/ijk.csv', encoding='utf-8', sep=',', index=False, header=None)
        os.remove(datafeedDir+'/ijk.xls')
        logger.debug("Successfully downloaded IJK to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_force():
    print(30*"-")
    logger.critical("FORCE TECHNOLOGY")
    print(30*"-")
    print(30*"-")

    loginURL = "https://fti.com.au/Account/Login"
    feed = "https://fti.com.au/Products/ExportProducts"

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://fti.com.au',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://fti.com.au/',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    s = requests.Session()
    data = {
        'ReturnUrl': '',
        'Email': getenv.FORCE_USERNAME,
        'Password': getenv.FORCE_PASSWORD
    }
    s.post(loginURL, headers=headers, data=data)

    try:
        logger.warning("Trying to Download Force Feed")
        print(30*"-")
        r = s.get(feed)
        try:
            os.remove(datafeedDir+'/force.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        open(datafeedDir+'/force.csv', 'wb').write(r.content)
        logger.debug("Successfully downloaded Force to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_4cabling():
    print(30*"-")
    logger.critical("4CABLING")
    print(30*"-")
    print(30*"-")

    feed = getenv.FEED_4CABLING
    try:
        logger.warning("Trying to Download 4Cabling Feed")
        print(30*"-")
        r = requests.get(feed)
        try:
            os.remove(datafeedDir+'/4cabling.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        open(datafeedDir+'/4cabling.csv', 'wb').write(r.content)
        logger.debug("Successfully downloaded 4Cabling to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_alloy():
    print(30*"-")
    logger.critical("ALLOY")
    print(30*"-")
    print(30*"-")

    feed = getenv.ALLOY_FEED
    try:
        logger.warning("Trying to Download Alloy Feed")
        print(30*"-")
        r = requests.get(feed)
        try:
            os.remove(datafeedDir+'/alloy.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        open(datafeedDir+'/alloy.csv', 'wb').write(r.content)
        logger.debug("Successfully downloaded Alloy to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_alloys():
    print(30*"-")
    logger.critical("ALLOYS")
    print(30*"-")
    print(30*"-")

    feed = getenv.ALLOYS_FEED
    try:
        logger.warning("Trying to Download Alloys Feed")
        print(30*"-")
        r = requests.get(feed)
        try:
            os.remove(datafeedDir+'/alloys.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        open(datafeedDir+'/alloys.csv', 'wb').write(r.content)
        logger.debug("Successfully downloaded Alloys to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_dicker():
    print(30*"-")
    logger.critical("DICKER DATA")
    print(30*"-")
    print(30*"-")

    feed = getenv.DICKER_FEED
    try:
        logger.warning("Trying to Download Dicker Feed")
        print(30*"-")
        r = requests.get(feed)
        try:
            os.remove(datafeedDir+'/dicker.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        open(datafeedDir+'/dicker.csv', 'wb').write(r.content)
        logger.debug("Successfully downloaded Dicker to: " + datafeedDir)
        print(30*"-")

        # Remove problematic lines from the file
        with open(datafeedDir+'/dicker.csv', 'r') as file:
            lines = file.readlines()
        with open(datafeedDir+'/dicker_temp.csv', 'w') as file:
            for line in lines:
                if '63B2MAR6AU-DASHCAM,1' not in line:
                    file.write(line)
        os.remove(datafeedDir+'/dicker.csv')
        os.rename(datafeedDir+'/dicker_temp.csv', datafeedDir+'/dicker.csv')

    except Exception as e:
        logger.critical(e)
        print(30*"-")

"""
def download_synnex():
    print(30*"-")
    logger.critical("SYNNEX")
    print(30*"-")
    print(30*"-")

    host = getenv.EMAIL_HOST
    username = getenv.EMAIL_USERNAME
    password = getenv.EMAIL_PASSWORD
    
    now = datetime.datetime.now()

    today = datetime.date.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)

    if(now.day == 1):
        day = int(lastMonth.strftime("%d"))
        month = int(lastMonth.strftime("%m"))
    else:
        day = now.day
        month = now.month

    query = A(subject='Reseller Product Report', date_gte=datetime.date(now.year, month, day))
    with MailBox(host).login(username, password, 'Inbox') as mailbox:
        logger.warning("Logged in")
        for msg in mailbox.fetch(query):
            for att in msg.attachments:
                try:
                    logger.warning("Trying to Download Synnex Feed - "+msg.date_str)
                    print(30*"-")
                    try:
                        os.remove(datafeedDir+'/synnex.csv')
                        logger.critical("Deleted previous datafeed")
                        print(30*"-")
                    except:
                        logger.debug("Previous datafeed doesn't exist - nothing to delete")
                        print(30*"-")
                    open(datafeedDir+'/synnex.csv', 'wb').write(att.payload)
                    dataframe = pd.read_csv(datafeedDir+'/synnex.csv',delimiter="\t")
                    os.remove(datafeedDir+'/synnex.csv')
                    dataframe.to_csv(datafeedDir+'/synnex.csv', encoding='utf-8', index=False)
                    logger.debug("Successfully downloaded Synnex to: " + datafeedDir)
                    print(30*"-")
                except Exception as e:
                    logger.critical(e)
                    print(30*"-")
"""
def download_ingram():
    print(30*"-")
    logger.critical("INGRAM MICRO")
    print(30*"-")
    print(30*"-")

    host = getenv.EMAIL_HOST
    username = getenv.EMAIL_USERNAME
    password = getenv.EMAIL_PASSWORD
    
    now = datetime.datetime.now()

    today = datetime.date.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)

    if(now.day == 1):
        day = int(lastMonth.strftime("%d"))
        month = int(lastMonth.strftime("%m"))
    else:
        day = now.day-1
        month = now.month

    query = A(subject='Price File Requested', date_gte=datetime.date(now.year, month, day))
    
    with MailBox(host).login(username, password, 'Inbox') as mailbox:
        logger.warning("Logged in")
        for msg in mailbox.fetch(query):
            for att in msg.attachments:
                try:
                    logger.warning("Trying to Download Ingram Feed - "+msg.date_str)
                    print(30*"-")
                    try:
                        os.remove(datafeedDir+'/ingram.csv')
                        os.remove(datafeedDir+'/CXCOMPUTING.txt')
                        logger.critical("Deleted previous datafeed")
                        print(30*"-")
                    except:
                        logger.debug("Previous datafeed doesn't exist - nothing to delete")
                        print(30*"-")
                    z = zipfile.ZipFile(io.BytesIO(att.payload))
                    fileName = ''.join(z.namelist())
                    z.extractall(datafeedDir)
                    os.rename(datafeedDir+"/"+fileName, datafeedDir+'/ingram.csv')
                    logger.debug("Successfully downloaded Ingram to: " + datafeedDir)
                    print(30*"-")
                except Exception as e:
                    logger.critical(e)
                    print(30*"-")

def download_moki():
    print(30*"-")
    logger.critical("MOKI")
    print(30*"-")
    print(30*"-")

    host = getenv.EMAIL_HOST
    username = getenv.EMAIL_USERNAME
    password = getenv.EMAIL_PASSWORD
    
    now = datetime.datetime.now()

    today = datetime.date.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)

    if(now.day == 1):
        day = int(lastMonth.strftime("%d"))
        month = int(lastMonth.strftime("%m"))
    else:
        day = now.day
        month = now.month

    query = A(subject='Moki Inventory Report', date_gte=datetime.date(now.year, month, day))
    
    with MailBox(host).login(username, password, 'Inbox') as mailbox:
        logger.warning("Logged in")
        for msg in mailbox.fetch(query):
            for att in msg.attachments:
                try:
                    logger.warning("Trying to Download Moki Feed - "+msg.date_str)
                    print(30*"-")
                    try:
                        os.remove(datafeedDir+'/moki.csv')
                        os.remove(datafeedDir+'/searchresults.csv')
                        logger.critical("Deleted previous datafeed")
                        print(30*"-")
                    except:
                        logger.debug("Previous datafeed doesn't exist - nothing to delete")
                        print(30*"-")
                    open(datafeedDir+'/moki.csv', 'wb').write(att.payload)
                    logger.debug("Successfully downloaded Moki to: " + datafeedDir)
                    print(30*"-")
                except Exception as e:
                    logger.critical(e)
                    print(30*"-")

"""
def download_auscomp():
    print(30*"-")
    logger.critical("AUSCOMP COMPUTERS")
    print(30*"-")
    print(30*"-")

    feed = getenv.AUSCOMP_FEED
    port = int(getenv.AUSCOMP_PORT)
    filename = getenv.AUSCOMP_FILENAME

    ftp = ftplib.FTP()
    ftp.connect(feed, port) 
    ftp.login(getenv.AUSCOMP_USERNAME, getenv.AUSCOMP_PASSWORD) 
    ftp.cwd('/')
    
    try:
        logger.warning("Trying to Download Auscomp Feed")
        print(30*"-")
        try:
            os.remove(datafeedDir+'/auscomp.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        ftp.retrbinary("RETR " + filename, open(datafeedDir+'/auscomp.csv', 'wb').write)
        
        timestamp = ftp.voidcmd("MDTM /"+filename)[4:].strip()
        time = parser.parse(timestamp).strftime("%d-%m-%Y %H:%M:%S")               
        logger.debug("Fetched Auscomp Feed: " + time)
        print(30*"-")
        
        logger.debug("Successfully downloaded Auscomp to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")
    
    ftp.quit()
"""

def download_auscomp():
    print(30*"-")
    logger.critical("AUSCOMP")
    print(30*"-")
    print(30*"-")

    feed = getenv.AUSCOMP_FEED_URL
    try:
        logger.warning("Trying to Download Auscomp Feed")
        print(30*"-")
        r = requests.get(feed)
        try:
            os.remove(datafeedDir+'/auscomp.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        open(datafeedDir+'/auscomp.csv', 'wb').write(r.content)
        logger.debug("Successfully downloaded Auscomp to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")



def download_synnex():
    print(30*"-")
    logger.critical("SYNNEX")
    print(30*"-")
    print(30*"-")

    feed = getenv.SYNNEX_HOST
    port = int(getenv.SYNNEX_PORT)
    filename = getenv.SYNNEX_FILENAME

    ftp = ftplib.FTP()
    ftp.set_pasv(False)
    ftp.connect(feed, port) 
    ftp.login(getenv.SYNNEX_USER, getenv.SYNNEX_PASS) 
    ftp.cwd('/')
    
    try:
        logger.warning("Trying to Download Synnex Feed")
        print(30*"-")
        try:
            os.remove(datafeedDir+'/synnex.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
            
        ftp.retrbinary("RETR " + filename, open(datafeedDir+'/synnex.csv', 'wb').write)
        
        timestamp = ftp.voidcmd("MDTM /"+filename)[4:].strip()
        time = parser.parse(timestamp).strftime("%d-%m-%Y %H:%M:%S")               
        logger.debug("Fetched Synnex Feed: " + time)
        dataframe = pd.read_csv(datafeedDir+'/synnex.csv',delimiter="\t")
        dataframe.to_csv(datafeedDir+'/synnex.csv', encoding='utf-8', index=False)
        print(30*"-")
        
        logger.debug("Successfully downloaded Synnex to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")
    
    ftp.quit()

def download_dynamicsupplies():
    print(30*"-")
    logger.critical("DYNAMIC SUPPLIES")
    print(30*"-")
    print(30*"-")

    host = getenv.EMAIL_HOST
    username = getenv.EMAIL_USERNAME
    password = getenv.EMAIL_PASSWORD
    
    now = datetime.datetime.now()

    today = datetime.date.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)

    if(now.day == 1):
        day = int(lastMonth.strftime("%d"))
        month = int(lastMonth.strftime("%m"))
    else:
        day = now.day
        month = now.month

    query = A(subject='Datafeed from Dynamic Supplies', date_gte=datetime.date(now.year, month, day))
    with MailBox(host).login(username, password, 'Inbox') as mailbox:
        logger.warning("Logged in")
        for msg in mailbox.fetch(query):
            for att in msg.attachments:
                try:
                    logger.warning("Trying to Download Dynamic Supplies Feed - "+msg.date_str)
                    print(30*"-")
                    try:
                        os.remove(datafeedDir+'/dynamicsupplies.csv')
                        logger.critical("Deleted previous datafeed")
                        print(30*"-")
                    except:
                        logger.debug("Previous datafeed doesn't exist - nothing to delete")
                        print(30*"-")
                    open(datafeedDir+'/dynamicsupplies.csv', 'wb').write(att.payload)
                    logger.debug("Successfully downloaded Dynamic Supplies to: " + datafeedDir)
                    print(30*"-")
                except Exception as e:
                    logger.critical(e)
                    print(30*"-")

def download_streakwave():
    print(30*"-")
    logger.critical("STREAKWAVE")
    print(30*"-")
    print(30*"-")

    feed = getenv.STREAKWAVE_FEED
    try:
        logger.warning("Trying to Download Streakwave Feed")
        print(30*"-")
        r = requests.get(feed)
        try:
            os.remove(datafeedDir+'/streakwave.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        open(datafeedDir+'/streakwave.csv', 'wb').write(r.content)
        logger.debug("Successfully downloaded Streakwave to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_newmagic():
    print(30*"-")
    logger.critical("NEWMAGIC")
    print(30*"-")
    print(30*"-")

    loginURL = "https://newmagic.com.au/Dealer-section/Login.aspx"
    feed = "https://newmagic.com.au/dealer-section/StdDealerPricelistCSV.aspx"

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'ASPSESSIONIDAESSTBAC=EDPDNNLAEGOFPGNKBODLKGID; ASPSESSIONIDCESTSDDA=INGOMKIBKHJAOKGFABGFBJFA; ASPSESSIONIDCASTSDDA=JNGOMKIBEIEMLADCJBPDKFMP',
        'Origin': 'https://newmagic.com.au',
        'Referer': 'https://newmagic.com.au/Dealer-section/Login.aspx?ReturnUrl=%2fdealer-section%2fpricelist.aspx',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    s = requests.Session()
    data = {
        '__VIEWSTATE': '/JU3lykiI4ehHhV0mCCtkf0GPRNLvRSp0BtrhoaCT2+6SPoT7d9ZS2QulVpwbofAOPw/N83eyCnY2GIFcH3Ri8bttCod2QS2u+B42zi/yYWDiyPDvEuRhed0XQLQjbakPX+AT7kbrkRW1Nvop5sCKp4tM7I=',
        '__VIEWSTATEGENERATOR': 'B1AB4E1A',
        '__EVENTVALIDATION': '30h0W+U9cl2QiTCsDzfo0LseQ95IUQlV3cTczjV9fgG6gXzmvhZt0tHF1qiqMWxqS3YwHZYMS4Cz50w49gNJ2xZtFELRJK68rsK0jx60VpQoptZPE6rrfKMDrxVh/AVg01MY1/44Y4/j8+eP0vHs9BuDigg=',
        'UsernameText': getenv.NEWMAGIC_USERNAME,
        'PasswordText': getenv.NEWMAGIC_PASSWORD,
        'LoginAction.x': '30',
        'LoginAction.y': '23',
    }

    cookies = {
        'ASPSESSIONIDAESSTBAC': 'EDPDNNLAEGOFPGNKBODLKGID',
        'ASPSESSIONIDCESTSDDA': 'INGOMKIBKHJAOKGFABGFBJFA',
        'ASPSESSIONIDCASTSDDA': 'JNGOMKIBEIEMLADCJBPDKFMP',
    }

    s.post(loginURL, cookies=cookies, headers=headers, data=data)

    try:
        logger.warning("Trying to Download Newmagic Feed")
        print(30*"-")
        r = s.get(feed)
        try:
            os.remove(datafeedDir+'/newmagic.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        open(datafeedDir+'/newmagic.csv', 'wb').write(r.content)
        logger.debug("Successfully downloaded Newmagic to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_hyka():
    print(30*"-")
    logger.critical("HYKA TECHNOLOGIES")
    print(30*"-")
    print(30*"-")

    feed = getenv.HYKA_FEED
    try:
        logger.warning("Trying to Download Hyka Feed")
        print(30*"-")
        r = requests.get(feed)
        try:
            os.remove(datafeedDir+'/hyka.csv')
            logger.critical("Deleted previous datafeed")
            print(30*"-")
        except:
            logger.debug("Previous datafeed doesn't exist - nothing to delete")
            print(30*"-")
        open(datafeedDir+'/hyka.csv', 'wb').write(r.content)
        logger.debug("Successfully downloaded hyka to: " + datafeedDir)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_seltec():
    print(30*"-")
    logger.critical("SELTEC")
    print(30*"-")
    print(30*"-")

    host = getenv.EMAIL_HOST
    username = getenv.EMAIL_USERNAME
    password = getenv.EMAIL_PASSWORD
    
    now = datetime.datetime.now()

    today = datetime.date.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)

    if(now.day == 1):
        day = int(lastMonth.strftime("%d"))
        month = int(lastMonth.strftime("%m"))
    else:
        day = now.day
        month = now.month

    query = A(subject='*SELTEC DAILY DATA FEED*', date_gte=datetime.date(now.year, month, day-1))
    with MailBox(host).login(username, password, 'Inbox') as mailbox:
        logger.warning("Logged in")
        for msg in mailbox.fetch(query):
            for att in msg.attachments:
                try:
                    logger.warning("Trying to Download Seltec Feed - "+msg.date_str)
                    print(30*"-")
                    try:
                        os.remove(datafeedDir+'/seltec.csv')
                        logger.critical("Deleted previous datafeed")
                        print(30*"-")
                    except:
                        logger.debug("Previous datafeed doesn't exist - nothing to delete")
                        print(30*"-")
                    open(datafeedDir+'/seltec.csv', 'wb').write(att.payload)
                    logger.debug("Successfully downloaded Seltec to: " + datafeedDir)
                    print(30*"-")
                except Exception as e:
                    logger.critical(e)
                    print(30*"-")

def download():
   create_directory()

   download_leader_m()
   download_leader()
   download_compuworld()
   download_bluechip()
   download_multimedia()
   download_mittoni()
   download_powerhouse()
   download_ijk()
   download_force()
   download_4cabling()
   download_alloys()
   download_dicker()
   download_synnex()
   download_ingram()
   download_streakwave()
   download_moki()
   download_auscomp()
   download_dynamicsupplies()
   download_newmagic()
   download_hyka()
   download_seltec()