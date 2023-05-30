import os

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import requests
import coloredlogs, logging
import time
from pathlib import Path
import glob
import numpy as np
import re
import tkinter as tk
from tkinter import filedialog

import getenv

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

today = time.strftime("%d%m%Y")
downloadDir = str(Path.home() / "Downloads")
datafeedDir = downloadDir+'/'+today

newProdPattern = time.strftime("%Y%m%d")

def update_missing():
    os.chdir(datafeedDir)

    missingFile = today+'-missing.csv'
    files = glob.glob(newProdPattern+'-*')
    newSKU = np.empty((0,1))
    supplier = np.empty((0,1))

    try:
        os.remove(missingFile)
        logger.critical("Deleted previous link file")
        print(30*"-")
    except:
        logger.debug("Previous missing file does not exist")
    
    try:
        for file in files:
            df = pd.read_csv(file, na_filter=False, encoding = 'unicode_escape', header=None)
            count = len(df.index)-1

            supplierSearch = re.search("([A-Za-z]+)", file)
            supplierName = supplierSearch.group(1)
            print(supplierName,": " , count , " Products")

            for i in range(count):
                supplier = np.append(supplier, supplierName)

            newSKU = np.append(newSKU, df[4])
            index = np.argwhere(newSKU=="Product Code/SKU")
            newSKU = np.delete(newSKU, index)
    
        df = pd.DataFrame(data=newSKU, columns=["Product Code/SKU"])
        df["Missing Supplier Code"] = newSKU
        df["Supplier"] = supplier
        df.to_csv(missingFile, index=False)
        logger.debug("Successfully created CSV to bulk link products: "+missingFile)
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def download_all_missing(folder):
    try:
        files = glob.glob(folder+'/*')
        for f in files:
            os.remove(f)
        logger.critical("Deleted Previous Files")
    except Exception as e:
        logger.critical(e)

    print(30*"-")
    logger.critical("Downloading all Missing Products")
    print(30*"-")
    print(30*"-")

    loginURL = getenv.BCM_URL + 'login.php'

    headers = {
        'authority': 'auspc.tcsys.com.au',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': getenv.BCM_URL,
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': getenv.BCM_URL + 'index.html',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'PHPSESSID=l9e3i2lifqnmb3aebl44juphv1',
    }

    data = {
        'userName': getenv.BCM_USERNAME,
        'password': getenv.BCM_PASSWORD
    }

    s = requests.Session()

    s.post(loginURL, headers=headers, data=data)

    feedArray = [
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=113",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=108",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=116",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=118",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=112",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=88",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=90",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=122",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=41",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=91",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=124",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=94",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=123",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=110",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=119",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=86",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=3",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=97",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=120",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=111",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=102",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=98",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=125",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=126",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=128",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=129",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=130",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=131",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=132",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=134",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=135",
        getenv.BCM_URL + "AusPC/supplier-missing-product-export.php?id=136"
    ]

    try:
        logger.warning("Trying to Download all Missing Product Feeds")
        print(30*"-")
        for feed in feedArray:
            try:
                r = s.get(feed)
                d = r.headers['content-disposition']
                fname = re.findall("filename=(.+)", d)[0]
                open(folder+'/'+fname, 'wb').write(r.content)
                logger.debug("Successfully downloaded: "+fname)
            except Exception as e:
                logger.critical(e)
        logger.debug("Successfully downloaded all feeds to: " + folder)
        print(30*"-")
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def update_all_missing(removeSpecial):
    root = tk.Tk()
    root.withdraw()
    folderPath = filedialog.askdirectory()

    os.chdir(folderPath)

    download_all_missing(folderPath)

    missingFile = today+'-missing.csv'
    files = glob.glob('*')

    
    try:
        os.remove(missingFile)
        logger.critical("Deleted previous link file")
        print(30*"-")
    except:
        logger.debug("Previous missing file does not exist")
    
    try:
        for file in files:
            newSKU = np.empty((0,1))
            supplier = np.empty((0,1))

            df = pd.read_csv(file, na_filter=False, encoding = 'utf-8', header=None, low_memory=False)
            count = len(df.index)-1

            supplierSearch = re.search("([0-9A-Za-z]+)", file)
            supplierName = supplierSearch.group(1)
            print(supplierName,": " , count , " Products")

            for i in range(count):
                supplier = np.append(supplier, supplierName)

            newSKU = np.append(newSKU, df[4])
            index = np.argwhere(newSKU=="Product Code/SKU")
            newSKU = np.delete(newSKU, index)

            df = pd.DataFrame(data=newSKU, columns=["Product Code/SKU"])
            df["Missing Supplier Code"] = newSKU
            df["Supplier"] = supplier

            if removeSpecial:
                df['Product Code/SKU'] = df['Product Code/SKU'].str.replace(r'[^a-zA-Z0-9]', '')
                df['Product Code/SKU'] = df['Product Code/SKU'].str.replace(r' ', '')

            df['Product Code/SKU'].replace('', np.nan, inplace=True)
            df.dropna(subset=['Product Code/SKU'], inplace=True)

            df.to_csv(missingFile, mode='a', index=False, header=not os.path.exists(missingFile))
            os.remove(file)

        logger.debug("Successfully created CSV to bulk link products: "+missingFile)
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def update_all_missing_gtin(removeSpecial):
    root = tk.Tk()
    root.withdraw()
    folderPath = filedialog.askdirectory()

    os.chdir(folderPath)

    download_all_missing(folderPath)

    missingFile = today+'-missing-GTIN.csv'
    files = glob.glob('*')

    
    try:
        os.remove(missingFile)
        logger.critical("Deleted previous link file")
        print(30*"-")
    except:
        logger.debug("Previous missing file does not exist")
    
    try:
        for file in files:
            newSKU = np.empty((0,1))
            supplier = np.empty((0,1))
            gtin = np.empty((0,1))

            df = pd.read_csv(file, na_filter=False, encoding = 'utf-8', header=None, low_memory=False)
            count = len(df.index)-1

            supplierSearch = re.search("([0-9A-Za-z]+)", file)
            supplierName = supplierSearch.group(1)
            print(supplierName,": " , count , " Products")

            for i in range(count):
                supplier = np.append(supplier, supplierName)

            newSKU = np.append(newSKU, df[4])
            index = np.argwhere(newSKU=="Product Code/SKU")
            newSKU = np.delete(newSKU, index)

            gtin = np.append(gtin, df[53])
            index2 = np.argwhere(gtin=="GPS Global Trade Item Number")
            gtin = np.delete(gtin, index2)

            df = pd.DataFrame(data=newSKU, columns=["Product Code/SKU"])
            df["Missing Supplier Code"] = newSKU
            df["Supplier"] = supplier
            df["GTIN"] = gtin

            if removeSpecial:
                df['Product Code/SKU'] = df['Product Code/SKU'].str.replace(r'[^a-zA-Z0-9 +]', '')
                df['Product Code/SKU'] = df['Product Code/SKU'].str.replace(r' ', '')

            df['Product Code/SKU'].replace('', np.nan, inplace=True)
            df.dropna(subset=['Product Code/SKU'], inplace=True)

            df['GTIN'].replace('', np.nan, inplace=True)
            df.dropna(subset=['GTIN'], inplace=True)

            df.to_csv(missingFile, mode='a', index=False, header=not os.path.exists(missingFile))
            os.remove(file)

        logger.debug("Successfully created CSV to bulk link products: "+missingFile)
    except Exception as e:
        logger.critical(e)
        print(30*"-")

def nodownload_update(removeSpecial):
    root = tk.Tk()
    root.withdraw()
    folderPath = filedialog.askdirectory()

    os.chdir(folderPath)

    missingFile = today+'-missing.csv'
    files = glob.glob('*')

    
    try:
        os.remove(missingFile)
        logger.critical("Deleted previous link file")
        print(30*"-")
    except:
        logger.debug("Previous missing file does not exist")
    
    try:
        for file in files:
            newSKU = np.empty((0,1))
            supplier = np.empty((0,1))

            df = pd.read_csv(file, na_filter=False, encoding = 'utf-8', header=None, low_memory=False)
            count = len(df.index)-1

            supplierSearch = re.search("([0-9A-Za-z]+)", file)
            supplierName = supplierSearch.group(1)
            print(supplierName,": " , count , " Products")

            for i in range(count):
                supplier = np.append(supplier, supplierName)

            newSKU = np.append(newSKU, df[4])
            index = np.argwhere(newSKU=="Product Code/SKU")
            newSKU = np.delete(newSKU, index)

            df = pd.DataFrame(data=newSKU, columns=["Product Code/SKU"])
            df["Missing Supplier Code"] = newSKU
            df["Supplier"] = supplier

            if removeSpecial:
                df['Product Code/SKU'] = df['Product Code/SKU'].str.replace(r'[^a-zA-Z0-9 +]', '')
                df['Product Code/SKU'] = df['Product Code/SKU'].str.replace(r' ', '')

            df['Product Code/SKU'].replace('', np.nan, inplace=True)
            df.dropna(subset=['Product Code/SKU'], inplace=True)

            df.to_csv(missingFile, mode='a', index=False, header=not os.path.exists(missingFile))
            os.remove(file)

        logger.debug("Successfully created CSV to bulk link products: "+missingFile)
    except Exception as e:
        logger.critical(e)
        print(30*"-")


