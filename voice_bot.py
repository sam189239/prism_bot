import speech_recognition as sr
import pyttsx3
import pywhatkit as kt
import datetime
import pytz
import wikipedia
from wikipedia.wikipedia import search
# from newsfetch.news import newspaper
import feedparser
import json
import re

with open('toi_feed_links.json', 'r') as myfile:
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
            

    
    if 'play' in command:
        song  = command.replace('play','')
        word = 'playing' + song
        talk(word)
        # print(word)
        kt.playonyt(song)
    
    elif 'time' in command:
        
        ti = datetime.datetime.now().strftime('%I:%M:%p')
        
        talk('The time right now is ' + ti )
    
    # elif 'who is' or 'give info on' in command:
    #     person = command.replace('who is','')
    #     person = command.replace('info on','')
    #     data = wikipedia.summary(person,1)
    #     print("From Wikipedia:")
    #     print(data)
    #     talk(data)

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
    

    elif 'who is' or 'give info on' in command:
        person = command.replace('who is','')
        person = command.replace('info on','')
        if person!="":
            data = wikipedia.summary(person,1)
            print("From Wikipedia:")
            talk(data)
    
    else:
        talk("Going to sleep!")

command = give_command()
run_alexa()
