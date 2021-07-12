import feedparser
import json
import re

with open('toi_feed_links.json', 'r') as myfile:
    data = myfile.read()
feed_links = json.loads(data)

type = "chennai"

NewsFeed = feedparser.parse(feed_links[type])
if len(NewsFeed.entries)==0:
    print("Sorry, couldn't find any entries.")
else:
    print('Number of RSS posts :', len(NewsFeed.entries))

    for i in range(len(NewsFeed.entries)):
        entry = NewsFeed.entries[i]
        if re.sub('<[^>]*>', '', entry.summary)!="":
            print(i+1,re.sub('<[^>]*>', '', entry.summary)) 
