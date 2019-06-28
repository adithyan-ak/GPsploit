import requests
from src.api import macvendor

def macLookup():

    mac = input("Enter the mac address : ")
    url =  "https://api.macvendors.com/v1/lookup/"+mac
    api_key = "Bearer "+macvendor()
    resp = requests.get(url,headers={"Authorization":api_key})
    result = resp.json()
    print('')
    if resp.status_code == 200:
        final = result['data']
        print("Manufacturer : "+ final['organization_name'])
        print("Manufacturer Address : " + final['organization_address'])
    elif resp.status_code == 404:
        print('Error 404 : Mac Address Not Found')
    else:
        print("Unexpected Error")
        pass