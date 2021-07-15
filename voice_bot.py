import speech_recognition as sr
import pyttsx3
import pywhatkit as kt
import datetime
import pytz
import wikipedia
from wikipedia.wikipedia import search
import feedparser
import json
import random
import re

with open('data/toi_feed_links.json', 'r') as myfile:
    data = myfile.read()
feed_links = json.loads(data)

listener = sr.Recognizer()
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
engine = pyttsx3.init()
voices = engine.getProperty('voices')
newVoiceRate = 178
engine.setProperty('rate',newVoiceRate)
engine.setProperty('voice','english-us')


greeting = ["Hello, thanks for asking", "Good to see you again", "Hi there, how can I help?"]
noanswer = ["Sorry, can't understand you", "Please give me more info", "Not sure I understand", "Try again", "Going to sleep!"]
goodbye = ["See you!", "Have a nice day", "Bye! Come back again soon.", "Bye", "Cya!"]


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
    


def give_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('listening...')
            
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'alexa' in command:
                command = command.replace('alexa','')
                
                
            
    except:
        pass
    return command


def give_sec_command():
    sec_command = ""
    try:
        with sr.Microphone() as source:
            print('listening...')
            
            voice = listener.listen(source)
            sec_command = listener.recognize_google(voice) 
            sec_command = sec_command.lower()
            print(sec_command)            
    except:
        pass
    return sec_command


def run_alexa(command):
    
    # command = give_command()
    greet = False
    bye = False
    for a in ["hi", "how are you", "is anyone there?","hey","hola", "hello", "good day"]:
        if a in command:
            talk(greeting[(random.randint(0,len(greeting)-1))])
            greet = True
            
    for a in ["bye", "see you later", "goodbye", "nice chatting to you, bye", "till next time"]:
        if a in command :
            talk(goodbye[(random.randint(0,len(goodbye)-1))])
            bye = True
            
#     greet = True
#     bye = True
#     if greet:
#         for a in ["hi", "how are you", "is anyone there?","hey","hola", "hello", "good day"]:
#             if a in command:
#                 talk(greeting[(random.randint(0,len(greeting)-1))])
#                 greet = False

#     if bye:
#         for a in ["bye", "see you later", "goodbye", "nice chatting to you, bye", "till next time"]:
#             if a in command:
#                 talk(goodbye[(random.randint(0,len(goodbye)-1))])
#                 bye = False

    
    if 'play' in command:
        song  = command.replace('play','')
        word = 'playing' + song
        talk(word)
        # print(word)
        link = kt.playonyt(song)
        print(link)
    
    elif 'time' in command:
        
        ti = datetime.datetime.now(pytz.timezone("Asia/Calcutta")).strftime('%I:%M:%p')
        
        talk('The time right now is ' + ti )


    elif 'search on google' in command:
        sear = command.replace('search on google','')
        kt.search(sear)

    
    elif 'news' in command:
        type = "top stories"
        for a in feed_links.keys():
            if a in command:
                type = a      
        NewsFeed = feedparser.parse(feed_links[type])
        if len(NewsFeed.entries)==0:
            out = "Sorry, couldn't find any entries."
        else:
            out = "Found " + str(len(NewsFeed.entries)) + " entries\n"
        talk(out)
        for i in range(len(NewsFeed.entries)):
            entry = NewsFeed.entries[i]
            talk(entry.title)
            if i == len(NewsFeed.entries) - 1:
                out = "Do you want to know more?"
            else:
                out = "Do you want to know more or go to the next topic or stop?"
            talk(out)
            command_news = give_sec_command()
            if "more" in command_news:
                if re.sub('<[^>]*>', '', entry.summary)!="":
                    talk(re.sub('<[^>]*>', '', entry.summary)) 
                    talk("Next in line, ")        
                else:
                    talk("Could't find sumamry.")
            elif "next" in command_news:
                continue
            elif "stop" or "no" in command_news:
                talk("Okay!")
                break
            else:
                 break
    
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
        

    elif 'who is' or 'give info on' in command:
        person = command.replace('who is','')
        person = command.replace('info on','')
        if person!="":
            data = wikipedia.summary(person,1)
            print("From Wikipedia:")
            talk(data)
    
    else:
        talk(noanswer[(random.randint(0,len(noanswer)-1))])

command = give_command()
run_alexa(command)
