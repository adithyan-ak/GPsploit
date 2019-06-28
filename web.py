import socket
from webosint.cmsdetect import CMSdetect
from webosint.nslookup import nsLookup
from webosint.portscan import DefaultPort,Customrange
from webosint.reverseip import ReverseIP
from webosint.subdomain import SubDomain
from webvuln.bruteforce import ssh,ftp
from webvuln.clickjacking import ClickJacking
from webvuln.cors import Cors
from webvuln.hostheader import HostHeader

host = None
port = None


# Checking whether the target host is alive or dead
def CheckTarget():

    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host, port))

    if  result == 0:
        return True
    else:
        return False

# Main Method
def Web():
    global host
    host = input("Enter the Target Host : ")
    global port
    port = int(input("Enter the Target port : "))
    print('')
    print("Starting WAVES \n")
    print("Checking whether the Target is reachable \n")
    # calling CheckTarget method
    if CheckTarget()==True:
        print("Target Alive \n")
        print("Host : " + host)
        print("Port : %s" % port)
        Menu()
    else:
        print("The Host is Unreachable \n")
        exit()


NmapFunctions = {
    1: DefaultPort,
    2: Customrange,
}


def nmaprec(host,port):

    Choice = 1
    while True:
        print("1. Scan Default Ports (22-443)")
        print("2. Enter Custom Range")
        print("3. Back to Main Menu")
        print('')
        Choice = int(input(">> "))
        if (Choice >= 0) and (Choice < 3):
            NmapFunctions[Choice](host, port)
        elif Choice == 3:
            Menu()
        else:
            print("Please choose an Appropriate option")

BruteFunctions = {
        1: ssh,
        2: ftp
    }

def BruteForce(host, port):
    Selection = 1
    while True:
        print('')
        print("1. SSH")
        print("2. FTP")
        print("3. Main Menu")
        print('')
        Selection = int(input(">> "))
        print('')
        if (Selection >= 0) and (Selection < 3):
            BruteFunctions[Selection](host, port)
        elif Selection == 3:
            Menu()
        else:
            print("Please choose an Appropriate option")


MainFunctions = {
 1: ReverseIP,
 2: SubDomain,
 3: nsLookup,
 4: CMSdetect,
 5: nmaprec,
 6: BruteForce,
 7: ClickJacking,
 8: Cors,
 9: HostHeader
}

def Menu():
    Selection = 1
    while True:
        print('')
        print("1. ReverseIP")
        print("2. SubDomain")
        print("3. nsLookup")
        print("4. CMSDetect")
        print("5. PortScan")
        print("6. Bruteforce")
        print("7. ClickJacking")
        print("8. CORS")
        print("9. Host Header Injection")
        print("10. Exit")
        print('')
        Selection = int(input(">> "))
        print('')
        if (Selection >= 0) and (Selection < 10):
            MainFunctions[Selection](host, port)
        elif Selection == 10:
            exit()
        else:
            print("Please choose an Appropriate option")