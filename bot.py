import pywhatkit as kt
import datetime
import pytz
import wikipedia
from wikipedia.wikipedia import search
import feedparser
import json
import re
import webbrowser


print(__name__)
with open('data/toi_feed_links.json', 'r') as myfile:
    data = myfile.read()
feed_links = json.loads(data)

def run_alexa(command):
       
    if 'play' in command:
        song  = command.replace('play','')
        # word = 'playing' + song
        # talk(word)
        #msg = 'playing' + song
        link = kt.playonyt(song, open_video = False)
        msg = "Playing: "+link
        webbrowser.open_new_tab(link)

    elif 'time' in command:
        ti = datetime.datetime.now(pytz.timezone("Asia/Calcutta")).strftime('%I:%M:%p')
        
        # talk('The time right now is ' + ti )
        msg = "The time right now is " + ti

    elif 'search on google' in command:
        sear = command.replace('search on google','')
        kt.search(sear) 

    
    elif 'news' in command:
        type = "top stories"
        for a in feed_links.keys():
            if a in command:
                type = a      
        NewsFeed = feedparser.parse(feed_links[type])
        if len(NewsFeed.entries)<2:
            msg = "Sorry, couldn't find any entries."
        else:
            msg = "Found " + str(len(NewsFeed.entries)) + " entries\n"
        
        for i in range(2):
            entry = NewsFeed.entries[i]
            msg += entry.title + "\n" + entry.summary + "\n\n"
            

    elif 'covid' in command:
        import urllib.request as ul
        from bs4 import BeautifulSoup as soup
        import regex as re

        url = 'https://covid19.who.int/region/searo/country/in'
        req = ul.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        client = ul.urlopen(req)
        htmldata = client.read()
        client.close()

        pagesoup = soup(htmldata, "html.parser")
        headings = pagesoup.findAll('span', {"class":"sc-fzoYHE dZCNaz"})
        values = pagesoup.findAll('span', {"class":"sc-fznAgC jiWVsa"})

        flag=1
        msg = "In India: "
        for a,b in headings, values:   
            a = (re.sub('<[^>]*>', '', str(a)))
            b = (re.sub('<[^>]*>', '', str(b))) 
            if flag:
                msg += (a +",\t"+ b + "\n = ")
                flag -= 1
            else:
                msg += (a +",\t"+ b + "\n")
        

    elif 'who is' in command:
        person = command.replace('who is','')
        person = command.replace('info on','')
        if person!="":
            data = wikipedia.summary(person,1)
            # print("From Wikipedia:")
            # talk(data)
            msg = "From Wikipedia: \n"+ data
    else:
        # talk("Going to sleep!")
        msg = "Going to sleep!"

    return msg
if __name__ == "__main__":
    command = "" #give_command()
    run_alexa(command)
