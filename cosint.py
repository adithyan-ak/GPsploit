import username, EmailScan
from username import NameUser
from EmailScan import GetEmail
from phonenum import carrierlookup
from web import Web
from metadata import gps_analyzer
from reverseimg import reverseImg
from multipleip import get_ip
from maclookup import macLookup
from sentinment import GetTweet

MainFunctions={
 1: NameUser,
 2: carrierlookup,
 3: GetEmail,
 4: Web,
 5: gps_analyzer,
 6: reverseImg,
 7: get_ip,
 8: macLookup,
 9: GetTweet
}


def Menu():
    Selection = 1
    while True:
        print('')
        print("1. Username")
        print("2. Phone Number")
        print("3. Email")
        print("4. Domain")
        print("5. Metadata Analyzer")
        print("6. Reverse Image Search")
        print("7. IP Heatmap")
        print("8. Mac Address Lookup")
        print("9. Sentiment Analysis")
        print("10. Exit")
        print('')
        Selection = int(input(">> "))
        print('')
        if (Selection == 1):
            MainFunctions[Selection]()
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
