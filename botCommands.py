import telegram
from telegram.ext import Updater, CommandHandler

from time import sleep

import requests

##########################################################
#get botID
botToken = '1108396137:AAGzh9VfPibPY0ZBIKWMvIC0zkdPiV9ZKp0'

#open files
beeMovie = open("files/Bee-Movie-Script.text", "r")
commandsList = open("files/commandsList.text", "r")

#setup the live queue
updater = Updater(token=botToken, use_context=True)
dispatcher = updater.dispatcher
##########################################################

def sendText(bot_message, bot_chatID):
	send_text = 'https://api.telegram.org/bot' + botToken + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
	response = requests.get(send_text)
	return response.json()

def startupCommands():
	#start updater
	updater.start_polling()

	#initialize commands
	dispatcher.add_handler(CommandHandler('bee', bee))
	dispatcher.add_handler(CommandHandler('help', help))

def shutdownCommands():
	updater.stop()
	beeMovie.close()
	commandsList.close()
	exit();

################################-----COMMANDS-----################################
def bee(update, context):
	for line in beeMovie:
		context.bot.send_message(chat_id=update.effective_chat.id, text=line)
		sleep(3.5)
	beeMovie.seek(0)

def help(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text = commandsList.read())
	commandsList.seek(0)
##################################################################################
