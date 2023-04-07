from download import *
from update import *

def individual():
    subMenu = True
    while subMenu:
        create_directory()
        print(10*"-")
        print("SELECT SUPPLIER TO DOWNLOAD")
        print(10*"-")
        print("1. Download Leader-M")
        print("2. Download Leader")
        print("3. Download Compuworld")
        print("4. Download Bluechip")
        print("5. Download Multimedia")
        print("6. Download Mittoni")
        print("7. Download Powerhouse")
        print("8. Download IJK")
        print("9. Download Force")
        print("10. Download 4Cabling")
        print("11. Download Alloy")
        print("12. Download Alloys")
        print("13. Download Dicker")
        print("14. Download Synnex")
        print("15. Download Ingram")
        print("16. Download Auscomp")
        print("17. Update Leader-Yealink")
        print("18. Update Leader-Plantronics")
        print("19. Update Anixter")
        print("20. Download Moki")
        print("21. Update Thermaltake")
        print("22. Download Dynamic Supplies")
        print("23. Update Leader-Brateck")
        print("24. Download Newmagic")
        print("25. Download Streakwave")
        print("26. Download Hyka")
        print("27. Download Seltec")
        print("28. Exit")

        subChoice=int(input("Enter your choice [1-28]:"))

        if subChoice==1:
            download_leader_m()
            update_leader_m()
        elif subChoice==2:
            download_leader()
            update_leader()
        elif subChoice==3:
            download_compuworld()
            update_compuworld()
        elif subChoice==4:
            download_bluechip()
            update_bluechip()
        elif subChoice==5:
            download_multimedia()
            update_multimedia()
        elif subChoice==6:
            download_mittoni()
            update_mittoni()
        elif subChoice==7:
            download_powerhouse()
            update_powerhouse()
        elif subChoice==8:
            download_ijk()
        elif subChoice==9:
            download_force()
            update_force()
        elif subChoice==10:
            download_4cabling()
        elif subChoice==11:
            download_alloy()
        elif subChoice==12:
            download_alloys()
            update_alloys()
        elif subChoice==13:
            download_dicker()
            update_dicker()
        elif subChoice==14:
            download_synnex()
            update_synnex()
        elif subChoice==15:
            download_ingram()
            update_ingram()
        elif subChoice==16:
            download_auscomp()
            update_auscomp()
        elif subChoice==17:
            update_leader_yealink()
        elif subChoice==18:
            update_leader_plantronics()
        elif subChoice==19:
            update_anixter()
        elif subChoice==20:
            download_moki()
        elif subChoice==21:
            update_thermaltake()
        elif subChoice==22:
            download_dynamicsupplies()
            update_dynamicsupplies()
        elif subChoice==23:
            update_leader_brateck()
        elif subChoice==24:
            download_newmagic()
            update_newmagic()
        elif subChoice==25:
            download_streakwave()
            update_streakwave()
        elif subChoice==26:
            download_hyka()
            update_hyka()
        elif subChoice==27:
            download_seltec()
        elif subChoice==28:
            subMenu = False
        else:
            print("Wrong Choice")
