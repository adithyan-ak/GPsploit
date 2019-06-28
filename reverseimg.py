import requests,webbrowser

def reverseImg():
    try:
        print("Enter the Image Path to Reverse : ")
        img_path = input(">> ")
        searchUrl = 'https://www.google.co.in/searchbyimage/upload'
        multipart = {'encoded_image': (img_path, open(img_path, 'rb')), 'image_content': ''}
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        fetchUrl = response.headers['Location']
        webbrowser.open(fetchUrl)

    except FileNotFoundError as e:
        print("Error : File not Found")