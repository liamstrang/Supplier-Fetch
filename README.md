<a href="https://github.com/liamstrang/Supplier-Fetch/actions/workflows/test.yaml">
  <img src="https://github.com/liamstrang/Supplier-Fetch/actions/workflows/test.yaml/badge.svg" alt="Workflow status badge" height="20">
</a>

# Supplier Fetch for AusPCMarket Backend System

This Python Script pulls various files from different suppliers, modifies them and stores them in a folder.

## Instructions

1. Download or Clone this repository
2. Edit `src/.env.example` and fill in the details. Save the file and rename to `.env`
3. Install pip packages with `pip install -r requirements.txt` **(Requirements Python >3.6)**
4. Run `fetch.bat` in the home directory

## Usage

### Automatic Download
1. Open `fetch.bat`
2. Type `1` and press Enter
3. The feeds will start downloading to ~/Downloads/{DATE}

### Manual Download
1. Open `fetch.bat`
2. Type `2` and press Enter
3. Type the number corresponding to the suppllier
4. The file will be downloaded

### Bulk Link Supplier Products
1. Type `3` to create a missing.csv file

### Bulk Link All Products
1. Type `4` to download all the missing products and create a bulk link from these products
