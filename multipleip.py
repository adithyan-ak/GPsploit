import requests
import gmplot
from src.api import ipstackapi
import webbrowser

api_key = ipstackapi()

def get_ip():
    """
    Returns a list of IP addresses from a file containing one IP per line.
    """
    print('''Choose
    1) Trace single IP 
    2) Trace Multiple IPs''')
    choice = input(">> ")

    if choice == '1':
        ip = input("Enter the IP : ")
        read_single_ip(ip)
    elif choice == '2':
        ip_file = input("Enter the IP File Location : ")
        read_multiple_ip(ip_file)
    else:
        print("Please choose an appropriate option")

def read_single_ip(ip):
    print("Processing IP : %s" %ip)
    lats = []
    lons = []
    r = requests.get("http://api.ipstack.com/" + ip + "?access_key=" + api_key)
    resp = r.json()
    print('')
    print("IP :"+resp['ip'])
    print("Location : " + resp['region_name'])
    print("Country : " + resp['country_name'])
    print("Latitude : {longitude}".format(**resp))
    print("Longitude : {longitude}".format(**resp))
    if resp['latitude'] and resp['longitude']:
        lats = resp['latitude']
        lons = resp['longitude']
    maps_url = "https://maps.google.com/maps?q=%s,+%s" % (lats, lons)
    openWeb = input("Open GPS location in web broser? (Y/N) ")
    if openWeb.upper() == 'Y':
        webbrowser.open(maps_url, new=2)
    else:
        pass

def read_multiple_ip(ip_file):
    lats = []
    lons = []
    f = open(ip_file, "r")
    f1 = f.readlines()
    for line in f1:
        r = requests.get("http://api.ipstack.com/" + line + "?access_key=" + api_key)
        resp = r.json()
        if resp['latitude'] and resp['longitude']:
            lats.append(resp['latitude'])
            lons.append(resp['longitude'])
    heat_map(lats,lons)

def heat_map(lats,lons):
    gmap3 = gmplot.GoogleMapPlotter(20.5937, 78.9629, 5)
    # Plot method Draw a line in
    # between given coordinates
    gmap3.heatmap(lats,lons)
    gmap3.scatter(lats,lons, '#FF0000', size=50, marker=False)

    gmap3.plot(lats,lons, 'cornflowerblue', edge_width = 3.0)
    gmap3.apikey = "AIzaSyDmpwQtMwmoWGHX2UBqnAldc8CFDus77RQ"
    save_location = input("Enter a location to save : ")
    location = save_location + "/heatmap.html"
    gmap3.draw(location)
    print("Heatmap saved at " + location)
    openWeb = input("Open Heatmap in web broser? (Y/N) : ")
    if openWeb.upper() == 'Y':
        webbrowser.open(url=("file:///"+location))
    else:
        pass

