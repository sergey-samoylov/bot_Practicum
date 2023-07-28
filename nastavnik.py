import json
import os
import requests
import sys
import telegram

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TOKEN_TELEGRAM")
HOBBY_TEXT = json.loads(os.environ['hobby_text'])
LINKS = json.loads(os.environ['links'])

updater = Updater(token=TELEGRAM_TOKEN)

my_git_link = LINKS[0]
main_photo = LINKS[1]
hat_old_photo = LINKS[2]
gpt_m4a = LINKS[3]
sql_m4a = LINKS[4]
love_m4a = LINKS[5]

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup(
        [
        ['/start', '/photo'],
        ['/hobby', '/old_photo'],
        ['/GPT', '/SQL'],
        ['/love_story',]
        ], resize_keyboard=True)

    context.bot.send_message(
        chat_id = chat.id,
        text = f'Привет, {name}!\nСегодня дежурит наставник Сергей',
        reply_markup = buttons
    )

def help(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id = chat.id,
        text = 'ℹ️ /info - информация о боте'
    )
    context.bot.send_message(
        chat_id = chat.id,
        text = '🐍 /git - код бота на GitHub'
    )
    context.bot.send_message(
        chat_id = chat.id,
        text = '🌻 /hobby - об увлечениях'
    )
    context.bot.send_message(
        chat_id = chat.id,
        text = '📷 /photo - узнай наставника в лицо'
    )
    context.bot.send_message(
        chat_id = chat.id,
        text = '➡️ Исследуй кнопки! Познай силу, Люк! 🚀'
    )


def info(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id = chat.id,
        text = 'Ботом можно управлять через меню, кнопки или команды'
    )

def git(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id = chat.id,
        text = my_git_link
    )

def my_current_photo(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, main_photo)

def my_old_photo(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, hat_old_photo)

def love_audio(update, context):
    chat = update.effective_chat
    context.bot.send_audio(chat.id, love_m4a)

def gpt_audio(update, context):
    chat = update.effective_chat
    context.bot.send_audio(chat.id, gpt_m4a)

def sql_audio(update, context):
    chat = update.effective_chat
    context.bot.send_audio(chat.id, sql_m4a)

def my_hobby(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id = chat.id,
        text = HOBBY_TEXT[0]
    )
    context.bot.send_message(
        chat_id = chat.id,
        text = HOBBY_TEXT[1]
    )
    context.bot.send_message(
        chat_id = chat.id,
        text = HOBBY_TEXT[2]
    )

updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(CommandHandler('info', info))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('git', git))
updater.dispatcher.add_handler(CommandHandler('photo', my_current_photo))
updater.dispatcher.add_handler(CommandHandler('old_photo', my_old_photo))
updater.dispatcher.add_handler(CommandHandler('hobby', my_hobby))
updater.dispatcher.add_handler(CommandHandler('GPT', gpt_audio))
updater.dispatcher.add_handler(CommandHandler('SQL', sql_audio))
updater.dispatcher.add_handler(CommandHandler('love_story', love_audio))

updater.start_polling()
updater.idle()
