import feedparser

link = "https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/1264527"
feed = feedparser.parse(link)
print(feed.entries[0].title[:-34])
print(feed.entries[0].summary)

print(feed.entries[1].title[:-67])
print(feed.entries[1].summary)