Prism
A info bot. Currently, works based on keywords. NLP capabilities to be added.

Commands:
Greet
Goodbye
Time
News (Latest, World, Business, Sports, Tech, Entertainment, ...)
Covid updates


Deploying on AWS using PM2:

sudo apt install npm
npm install pm2@latest -g
pm2 start app.py --interpreter python3

Progress:

11-07-2021
made basic voicebot using speech recognition and pytts libraries

12-07-2021
set up flask server and deployed on aws to make it public
modified code to be suitable for web chatbot

13-07-2021

added covid updates from https://covid19.who.int/region/searo/country/in
displayed yt link for playing
added hardcoded general responses