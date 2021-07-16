import pywhatkit as kt
import datetime
import pytz
import wikipedia
from wikipedia.wikipedia import search
import feedparser
import json
import re
import webbrowser
import random


with open('data/toi_feed_links.json', 'r') as myfile:
    data = myfile.read()
feed_links = json.loads(data)

with open('data/responses.json', 'r') as myfile:
    data = myfile.read()
responses = json.loads(data)

greeting = ["Hello, thanks for asking", "Good to see you again", "Hi there, how can I help?"]
noanswer = ["Sorry, can't understand you", "Please give me more info", "Not sure I understand", "Try again", "Going to sleep!"]
goodbye = ["See you!", "Have a nice day", "Bye! Come back again soon.", "Bye", "Cya!"]

def run_alexa(command):
    greet = False
    bye = False
    for a in ["hi", "how are you", "is anyone there?","hey","hola", "hello", "good day"]:
        if a in command:
            msg = greeting[(random.randint(0,len(greeting)-1))]
            greet = True
            
    for a in ["bye", "see you later", "goodbye", "nice chatting to you, bye", "till next time"]:
        if a in command :
            msg = goodbye[(random.randint(0,len(goodbye)-1))]
            bye = True
            
    if 'who are you' in command:
        msg = "I am a basic Info Bot. Soon to be an intelligent assistant."
        
    elif 'play' in command:
        song  = command.replace('play','')
        # word = 'playing' + song
        # talk(word)
        #msg = 'playing' + song
        link = kt.playonyt(song, open_video = False)
        msg = 'Click <a href="'+link+'"> here </a> to play on YouTube.'
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
    elif not greet and not bye:
        # talk("Going to sleep!")
        # msg = "Going to sleep!"
        msg = noanswer[(random.randint(0,len(noanswer)-1))]

    return msg
if __name__ == "__main__":
    command = "" #give_command()
    run_alexa(command)
