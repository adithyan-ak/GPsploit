
#importing libraries
import requests
from bs4 import BeautifulSoup


def NameUser():

    #username is input through user and search string is formed
    username= input("Enter the username !!!")
    search_string = "https://en-gb.facebook.com/" + username

    #response is stored after request is made
    response = requests.get(search_string)

    #Response is stored and parsed to implement beautifulsoup
    soup = BeautifulSoup(response.text, 'html.parser')

    #List that will store the data that is to be fetched
    data = {'Name': "null",
            'Photo_link': "null",
            'Work':{'Company': "null", 'Position': "null", 'time_period': "null", 'Location': "null"},
            'Education': {'Institute': "null", 'time_period': "null", 'Location': "null"},
            'Address': {'Current_city': "null", 'Home_town': "null"},
            'Favouriate': {},
            'Contact_info': {}
            }





    ###Finding Name of the user
    #Min div element is found which contains all the information
    main_div = soup.div.find(id="globalContainer")

    #finding name of the user
    def find_name():
        name = main_div.find(id="fb-timeline-cover-name").get_text()
        print(name)

    #finding profile pic of the user
    #link = main_div.find_all(name="img")





    ###Finding About the user details
    #finding work details of the user
    def find_eduwork_details():
        education = soup.find(id="pagelet_eduwork")
        apple=education.find(attrs={"class":"_4qm1"})
        if (apple.get_text() != " "):
            for category in education.find_all(attrs={"class":"_4qm1"}):
                print(category.find('span').get_text() + " : ")
                for company in category.find_all(attrs={"class":"_2tdc"}):
                    if (company.get_text() != " "):
                        print(company.get_text())
                    else:
                        continue
        else:
            print("No work details found")

    #finding home details of the user
    def find_home_details():
        if(soup.find(id="pagelet_hometown") !=" "):
                home = soup.find(id="pagelet_hometown")
                for category in home.find_all(attrs={"class":"_4qm1"}):
                    print(category.find('span').get_text() + " : ")
                    for company in category.find_all(attrs={"class":"_42ef"}):
                        if (company.get_text() != " "):
                            print(company.get_text())
                        else:
                            continue
        else:
            print("No Home details found")

    #finding contact details of the user
    def find_contact_details():
        contact = soup.find(id="pagelet_contact")
        orange = contact.find(attrs={"class":"_4qm1"})
        if (orange.get_text() !=" "):
            for category in contact.find_all(attrs={"class":"_4qm1"}):
                print(category.find('span').get_text() + " : ")
                for company in category.find_all(attrs={"class":"_2iem"}):
                    if (company.get_text() != " "):
                        print(company.get_text())
                    else:
                        continue
        else:
             print("No Contact details found")






    ###Logic for finding the status of the response
    if ("200" in str(response)):
        find_name()
        find_eduwork_details()
        find_home_details()

    elif ("404" in str(response)):
        print("profile not found")
    else:
        print("some other response")

