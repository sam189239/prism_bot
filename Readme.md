# Prism: A info bot. 

Project yet to be completed. Currently, works based on keywords. NLP capabilities to be added.
Deployed on AWS EC2, Herokuapp, PI (exposed using localtunnel).
https://prism-chat.herokuapp.com/

If exposed using below localtunnel commands:
https://prism.loca.lt/

Commands:

Greet,  
Goodbye, 
Time, 
News (Latest, World, Business, Sports, Tech, Entertainment, ...), 
Covid updates


Deploying in background using PM2: (AWS and PI)
 
sudo apt install npm

sudo npm install pm2@latest -g

pm2 start app.py --interpreter python3

for voice bot, 
sudo apt install espeak


Running ngrok: (not used)

ngrok http 5000

Using localtunnel on Pi:

sudo npm install -g localtunnel

nohup lt -p 5000 -s prism

Progress:

11-07-2021: 
made basic voicebot using speech recognition and pytts libraries

12-07-2021: 
set up flask server and deployed on aws to make it public
modified code to be suitable for web chatbot

13-07-2021: 
added covid updates from https://covid19.who.int/region/searo/country/in
displayed yt link for playing
added hardcoded general responses

14-07-2021:
Set up Raspberry Pi to use as a server, ran app on localhost.
Fixed errors in previoius methods.

15-07-2021:
Used Ngrok to set up public server.
Used https://vatsalyagoel.com/setting-up-a-public-web-server-using-a-raspberry-pi-3/ to set up ngrok.
Exposed port and accessed remotely.
Setting up background process to close terminal after running.

16-07-2021:
Made yt links clickable.
Should look into metrics and alerts.


http://rss.accuweather.com/rss/liveweather_rss.asp?locCode=VOMM
https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/1264527
