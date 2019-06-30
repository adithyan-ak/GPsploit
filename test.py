from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

def ScrapTweets():

    username = input("Enter the user_id of the person -->   ")
    link = "https://twitter.com/" + username
    the_client = uReq(link)
    page_html = the_client.read()
    the_client.close()

    #print(link)

    soup = BeautifulSoup(page_html, 'html.parser')

    ######################################################################
    try:
        full_name = soup.find('a', attrs={"class":"ProfileHeaderCard-nameLink u-textInheritColor js-nav"})
        print("User Name --> " + full_name.text)
    except:
            print("User Name --> Not Found")
    print()

    try:
        user_id = soup.find('b', attrs={"class":"u-linkComplex-target"})
        print("User Id --> " + user_id.text)
    except:
        print("User Id --> Not Found")
    print()


    try:
        decription = soup.find('p', attrs={"class":"ProfileHeaderCard-bio u-dir"})
        print("Description --> " + decription.text)
    except:
        print("Decription not provided by the user")
    print()

    try:
        user_location = soup.find('span', attrs={"class":"ProfileHeaderCard-locationText u-dir"})
        print("Location -->  " + user_location.text.strip())
    except:
        print("Location not provided by the user")
    print()

    try:
        connectivity = soup.find('span', attrs={"class":"ProfileHeaderCard-urlText u-dir"})
        tittle = connectivity.a["title"]
        print("Link provided by the user --> " + tittle)
    except:
        print("No contact link is provided by the user")
    print()

    try:
        join_date = soup.find('span', attrs={"class":"ProfileHeaderCard-joinDateText js-tooltip u-dir"})
        print("The user joined twitter on --> " + join_date.text)
    except:
        print("The joined date is not provided by the user")
    print()

    try:
        birth = soup.find('span', attrs={"class":"ProfileHeaderCard-birthdateText u-dir"})
        birth_date = birth.span.text
        print(birth_date.strip())
    except:
        print("Birth Date not provided by the user")
    print()

    ###########################################################################
    try:
        span_box = soup.findAll('span', attrs={"class":"ProfileNav-value"})
        print("Total tweets --> " + span_box[0].text)
    except:
        print("Total Tweets --> Zero")
    print()

    try:
        print("Following --> " + span_box[1].text)
    except:
        print("Following --> Zero")
    print()

    try:
        print("Followers --> " + span_box[2].text)
    except:
        print("Followers --> Zero")
    print()

    try:
        print("Likes send by him --> " + span_box[3].text)
    except:
        print("Likes send by him --> Zero")
    print()

    try:
        if span_box[4].text != "More ":
            print("No. of parties he is Subscribed to --> " + span_box[4].text)
        else:
            print("No. of parties he is Subscribed to --> Zero")
    except:
        print("No. of parties he is Subscribed to --> Zero")
    print()


    spana = soup.findAll('span', attrs={"class":"ProfileNav-value"})


    ###########################################################################
    print("Tweets by " + username + " are --> ")
    #TweetTextSize TweetTextSize--normal js-tweet-text tweet-text
    for tweets in soup.findAll('p', attrs={"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}):
        print(tweets.text)
        print()


