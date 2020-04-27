#===================================================================================
#      ███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗     #
#      ████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗    #
#      ██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║    #
#      ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║    #
#      ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝    #
#      ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝     #
#       ╔╦╗╔═╗═╗ ╦╔═╗  ╔═╗╦═╗╔═╗ ╦╔═╗╔═╗╔╦╗  ╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗  ╔╦╗╔═╗╔═╗╔╦╗      #
#        ║ ║  ╔╩╦╝╚═╗  ╠═╝╠╦╝║ ║ ║║╣ ║   ║   ╠═╣╠═╣║  ╠╩╗║╣ ╠╦╝   ║ ║╣ ╠═╣║║║      #
#        ╩ ╚═╝╩ ╚═╚═╝  ╩  ╩╚═╚═╝╚╝╚═╝╚═╝ ╩   ╩ ╩╩ ╩╚═╝╩ ╩╚═╝╩╚═   ╩ ╚═╝╩ ╩╩ ╩      #
#===================================================================================
#[+] GORPO ORKO DEV  | Telegram: @GorpoOrko  | Github:https://github.com/gorpo  [+]
#===================================================================================

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
app = Flask(__name__)
#cria o chatbot
bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.Portuguese") #treina a desgraça
#alguns corpus que coloquei para dar um upgrade, outros corpus podem ser criados ou inseridos corpus de outras linguas
trainer.train('corpus_portugues/tcxs.yml',)
trainer.train('corpus_portugues/compliment.yml',)
trainer.train('corpus_portugues/conversations.yml')
trainer.train('corpus_portugues/games.yml',)
trainer.train('corpus_portugues/greetings.yml')
trainer.train('corpus_portugues/linguistic_knowledge.yml',)
trainer.train('corpus_portugues/money.yml')
trainer.train('corpus_portugues/proverbs.yml',)
trainer.train('corpus_portugues/suggestions.yml')
trainer.train('corpus_portugues/trivia.yml',)
trainer.train('corpus_portugues/unilab.yml')

#define app routes com o html
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
#função para resposta do bot
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

app.run()  #localhost para ngrok e outros   #ipfixo: port=5000, host='192.168.0.2'