from download import *
from update import *
from missing import *
from individual import individual
import coloredlogs, logging

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

today = time.strftime("%d%m%Y")
downloadDir = str(Path.home() / "Downloads")
datafeedDir = downloadDir+'/'+today

'''
TODO:
* ADD AUTOMATIC AUSPC FEED UPDATE
* UPLOAD AUSPC FEED TO SFTP
* ADD MIA DISTRIBUTION TO DOWNLOAD AND UPDATE
'''

def main():
   menu = True
   while menu:
      print(20*"-","AusPCMarket - Automated Feed Download - Version 1.5",20*"-")
      print("1. Download ALL Feeds")
      print("2. Download Specific Feed")
      print("3. Create Missing Products Feed")
      print("-"*30)
      print("4. Update All Missing Products")
      print("-"*30)
      print("5. Update All Missing Products (WITHOUT DOWNLOADING)")
      print("-"*30)
      print("6. Exit")
      print(79*"-")
      choice=int(input("Enter your choice [1-5]:"))

      if choice==1:
         print("Downloading ALL Feeds")
         download()
         update()

      if choice==2:
         individual()

      elif choice==3:
         if not os.path.exists(datafeedDir):
            logger.critical("Todays folder does not exist yet")
         else:
            print("Updating Missing Products")
            update_missing()
      
      elif choice==4:
         subMenu = True
         while subMenu:
            subChoice=input("Do you want to keep or remove special characters? (Y/N): ")
            if (subChoice == 'N' or subChoice == 'n'):
               print("Not removing special characters")
               update_all_missing(False)
               subMenu = False
            else:
               print("Removing special characters")
               update_all_missing(True)
               subMenu = False

      elif choice==5:
         subMenu = True
         while subMenu:
            subChoice=input("Do you want to keep or remove special characters? (Y/N): ")
            if (subChoice == 'N' or subChoice == 'n'):
               print("Not removing special characters")
               nodownload_update(False)
               subMenu = False
            else:
               print("Removing special characters")
               nodownload_update(True)
               subMenu = False

      elif choice==6:
         menu = False
      else:
         print("Wrong Choice")

if __name__ == "__main__":
    main()
