from src.api import phoneapis
import requests

def carrierlookup():
    phonenum = input("Enter Mobile Number with country code : ")
    api_key = phoneapis()
    url = ("http://apilayer.net/api/validate?access_key="+api_key+"&number="+phonenum)
    resp = requests.get(url)
    details = resp.json()
    print('')
    print("Country : "+ details['country_name'])
    print("Location : "+ details['location'])
    print("Carrier : "+ details['carrier'])


