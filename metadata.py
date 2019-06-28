import webbrowser
from PIL import Image
from PIL.ExifTags import TAGS


def get_exif(fn):
    try:
        ret = {}
        i = Image.open(fn)
        info = i._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
        return ret
    except FileNotFoundError as e:
        print('')
        print("File not found")
        exit()

def gps_analyzer():
    img_path = input("Enter the image path to analyze : ")
    a = get_exif(img_path)

    for x,y in a.items():
        print("%s : %s" %(x, y))

    if "GPSInfo" in a:
        lat = [float(x) / float(y) for x, y in a['GPSInfo'][2]]
        latref = a['GPSInfo'][1]
        lon = [float(x) / float(y) for x, y in a['GPSInfo'][4]]
        lonref = a['GPSInfo'][3]

        lat = lat[0] + lat[1] / 60 + lat[2] / 3600
        lon = lon[0] + lon[1] / 60 + lon[2] / 3600
        if latref == 'S':
            lat = -lat
        if lonref == 'W':
            lon = -lon
        map_it(lat, lon)

    else:
        print('')
        print("GPS location not found")


def map_it(lat, lon):
    # Prints latitude and longitude values
    print('')
    print("Accurate Latitude  : %s" % lat)
    print("Accurate Longitude : %s" % lon)
    print('')
    # Creates the URL for the map using the latitude and longitude values
    maps_url = "https://maps.google.com/maps?q=%s,+%s" % (lat, lon)
    # Prompts the user to launch a web browser with the map
    openWeb = input("Open GPS location in web broser? (Y/N) ")
    if openWeb.upper() == 'Y':
        webbrowser.open(maps_url, new=2)




if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   gps_analyzer()