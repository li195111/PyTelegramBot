'''
1. Go Telegram and Search BotFather with validated account first.
2. enter '/newbot' and choose a name for your bot. must end with 'bot'.
3. get your bot Http API
4. create an .env file and set your env variable 'TOKEN=XXXXXXX'
'''
import os
import telegram.ext
from telegram import Update
from dotenv import load_dotenv

# Extra
import pandas_datareader as web

load_dotenv()
TOKEN = os.getenv('TOKEN')

def start(update:Update, context):
    update.message.reply_text("Hello! Wellcome to QChoice!")
    return

def help(update:Update, context):
    update.message.reply_text("""
    The Following commands are available:
    
        /start -> Welcome Message
        /help -> This Message
        /content -> Information About QChoice
        /contact -> Information About Contact
        /stock ticker -> Information About Ticker
    """)

def content(update:Update, context):
    update.message.reply_text("This is content.")
    
def contact(update:Update, context):
    update.message.reply_text(f"This is contact informations.")
    
# Normal Message
def handle_message(update:Update, context):
    update.message.reply_text(f"You said {update.message.text}")

# Message with parameter
def stock(update:Update, context):
    ticker = context.args[0]
    data = web.DataReader(ticker, 'yahoo')
    price = data.iloc[-1]['Close']
    update.message.reply_text(f"The current price of {ticker} is {price:.2f}$!")

updater = telegram.ext.Updater(TOKEN, use_context=True)

disp = updater.dispatcher

# Command Handler
disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler('help', help))
disp.add_handler(telegram.ext.CommandHandler('content', content))
disp.add_handler(telegram.ext.CommandHandler('contact', contact))
# Message With Parameter
disp.add_handler(telegram.ext.CommandHandler('stock', stock))

# Normal Message Handler
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()