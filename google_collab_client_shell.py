!pip3 install python-telegram-bot==13
from telegram.ext import *
import subprocess as ss

telegram_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

updater = Updater(telegram_token, use_context=True)
dispatcher = updater.dispatcher

def message_handler(update, context):
    message = update.message
#    subs = ss.getoutput("subfinder -d {} -silent -t 100".format(message.text))
    print(message.text)
    cc = message.text
    cmd = cc.lower().split(' ')
    print(cmd)
    output = ss.Popen(cmd,stdout=ss.PIPE, stderr=ss.PIPE)
    o, e = output.communicate()
    update.message.reply_text(o.decode('ascii'))


#print('Error: '  + e.decode('ascii'))
#print('code: ' + str(b.returncode))
#    if subs:
#           data = subs.split("\n")
#           for i in data:
#               update.message.reply_text(i)

def start(update, context):
  name = update.effective_user.first_name
  update.message.reply_text("Hi!! {}".format(name))
  update.message.reply_text('Hello! Welcome to h311a BOT! Enjoy the resource!')
  update.message.reply_text('Happy Hacking!')

def contact(update, context):
  update.message.reply_text('Twitter Follow: https://twitter.com/Dheerajmadhukar')

###############Lastly, we need to update the functionalities with the commands we need to give it in BOT###############
dispatcher = updater.dispatcher
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('contact',contact))
updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
updater.start_polling()  # Start the bot
updater.idle() # Wait for the script to be stopped; this will stop the bot#!/usr/bin/python3
