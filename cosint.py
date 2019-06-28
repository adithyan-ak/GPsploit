import name, username, EmailScan
from username import NameUser
from EmailScan import GetEmail
from phonenum import carrierlookup
from web import Web
from metadata import gps_analyzer
from reverseimg import reverseImg
from multipleip import get_ip
from maclookup import macLookup

MainFunctions={
 1: name,
 2: NameUser,
 3: carrierlookup,
 4: GetEmail,
 5: Web,
 6: gps_analyzer,
 7: reverseImg,
 8: get_ip,
 9: macLookup
}


def Menu():
    Selection = 1
    while True:
        print('')
        print("1. Name")
        print("2. Username")
        print("3. Phone Number")
        print("4. Email")
        print("5. Domain")
        print("6. Metadata Analyzer")
        print("7. Reverse Image Search")
        print("8. IP Heatmap")
        print("9. Mac Address Lookup")
        print("10. Exit")
        print('')
        Selection = int(input(">> "))
        print('')
        if (Selection == 1):
            MainFunctions[Selection](name)
        elif (Selection == 2):
            MainFunctions[Selection]()
        elif (Selection == 3):
            MainFunctions[Selection]()
        elif (Selection == 4):
            MainFunctions[Selection]()
        elif (Selection == 5):
            MainFunctions[Selection]()
        elif Selection == 6:
            MainFunctions[Selection]()
        elif Selection == 7:
            MainFunctions[Selection]()
        elif Selection == 8:
            MainFunctions[Selection]()
        elif Selection == 9:
            MainFunctions[Selection]()
        elif Selection == 10:
            exit()
        else:
            print("Please choose an Appropriate option")



if __name__ == "__main__":
    Menu()