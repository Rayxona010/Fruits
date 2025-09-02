from aiogram import Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, BotCommand


menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1-tugma'),
            KeyboardButton(text='2-tugma')
        ],

    ]
)