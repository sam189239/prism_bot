#imports
from flask import Flask, render_template, request
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
from functions import bot

app = Flask(__name__)
#create chatbot
# englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# trainer = ChatterBotCorpusTrainer(englishBot)
# trainer.train("chatterbot.corpus.english") #train the chatter bot for english

#define app routes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/chatbot/options")
def options():
    return "Instructions\n1.\n2.\n3.\n4."

@app.route("/get")
#function for the bot response 
def get_bot_response(): 
    userText = request.args.get('msg').lower()
    return str(bot.run_alexa(userText))

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = '5000', debug = 'True') 