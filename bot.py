import telegram
from telegram.ext import Updater, CommandHandler
from botCommands import startupCommands, shutdownCommands, sendText
import requests
import random


#get botID
botToken = '1108396137:AAGzh9VfPibPY0ZBIKWMvIC0zkdPiV9ZKp0'

#open file
helpFile = open("files/help.text", "r")

#METHODS
def chatMenu(chatName, chatID, keyboard, botToken):
	print()
	keyboard = "foobar"
	while keyboard != 'back':
		keyboard = input(chatName + ' [' + chatID + '] : ')

		if keyboard == 'exit':
			shutdown()

		if keyboard != 'back':
			sendText(keyboard, chatID)
	print()

def menu():
	print()
	keyboard = "foobar"
	while keyboard != 'back':
		currentChat = ''
		keyboard = input("Where would you like to go? : ")
		print()

		if keyboard == 'dm':
			chatMenu('Personal DM', '1087229419', keyboard, botToken)

		if keyboard == 'sm':
			chatMenu('Snapple Mango Teaquel', '-1001162072529', keyboard, botToken)

		if keyboard == 'help':
			print(helpFile.read())

		if keyboard == 'exit' or keyboard == 'back':
			shutdown()

def shutdown():
	print("SHUTTING DOWN BOT")
	shutdownCommands()

	helpFile.close()
	exit();

def startup():
	startupCommands()
	menu()

startup()
