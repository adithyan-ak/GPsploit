import requests

def search():
    num = input("Enter the Number : ")
    URL = "https://www.google.com/search?q="+num
    r = requests.get(url=URL)
    resp = r.text
    f = open('src/dispnumbers',"r")
    f1 = f.read()
    if f1 in resp:
        print('Virtual Number Identified')
    else:
        pass

search()