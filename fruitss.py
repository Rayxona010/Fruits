import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import  Message
from aiogram.filters import Command

from config import TOKEN, ADMIN_ID
from keyboards import menyu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

mevalar = {
    "olma": {
        "name": "Olma 🍎",
        "price": "10,000 so'm / kg",
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg",
    },
    "banan": {
        "name": "Banan 🍌",
        "price": "18,000 so'm / kg",
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Banana-Single.jpg",
    },
    "anor": {
        "name": "Anor ",
        "price": "25,000 so'm / kg",
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/cb/Pomegranate_fruit_-_whole_and_split.jpg",
    },
    "uzum": {
        "name": "Uzum 🍇",
        "price": "9,000 so'm / kg",
        "image": "https://clck.ru/3NodqC",
    },
    "Apelsin": {
        "name": "Apelsin 🍊",
        "price": "47,490 so‘m / 1 kg",
        "image": "clck.ru/3NoeEv",
    },
    "Mandarin": {
        "name": "Mandarin 🍊",
        "price": "9,257.81 so‘m/kg ",
        "image": "clck.ru/3NoePH",
    },
    "Gilos": {
        "name": "Gilos 🍒",
        "price": "17,000 so‘m/kg ",
        "image": "clck.ru/3Noefa",
    },
    "O'rik": {
        "name": "O‘rik 🍑",
        "price": "5,000 so‘m/kg ",
        "image": "clck.ru/3Noeqn",
    },
    "Nok": {
        "name": "Nok 🍐",
        "price": "5,000 so‘m/kg ",
        "image": "clck.ru/3Noeqn",
    },
    "Ananas": {
        "name": "Ananas 🍍",
        "price": "15,000 so‘m/kg",
        "image": "clck.ru/3Nof6e",
    },
}


@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Assalomu aleykum botimizga xush kelibsiz! Bu bot orqali siz:"
        "Mevalarning narxlari haqida bilib olishingiz mumkin \n"
        "Mevalarning tavsifi haqida bilib olishgiz mumkin.\n"
        "Ozingiz tanlagan mevani sotib olishingiz mumkin.\n"
        "Sizga yoqqan mevani yetkazib berish xizmati ham mavjud.\n"
        "Quyidagi mevalardan birini tanlang.\n",
        reply_markup=menyu
    )


@dp.message(F.text)
async def tanlash_handler(message: Message):
    tanlangan = message.text
    info = mevalar[tanlangan]
    matn = f"{tanlangan} \n \n Narx:{info['Narxi']}\n Tavsif: {info['Tavsifi']}"
    await message.answer(text='...')


@dp.message()
async def boshqa_handler(message: Message):
    await message.answer("Iltimos menyudagi mevalardan birini tanlang:")


async def main():
    try:
        await bot.send_message(chat_id=ADMIN_ID, text="Bot ishga tushdi")
    except Exception as e:
        await bot.send_message("Bot xatolik tufayli to'xtadi:\n {str(ex)}")
    finally:
        await bot.send_message("Bot to'xtadi")


if __name__ == "__main__":
    asyncio.run(main())