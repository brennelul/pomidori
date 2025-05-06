import asyncio
from datetime import datetime
import random
from telebot.types import Message
from telebot.async_telebot import AsyncTeleBot
from telebot.util import types

bot = AsyncTeleBot("7753488518:AAHNpI8ljiAtWpikvGARPrbYreQ80kbFoA0")
paths = ["img/img1.jpg", "img/img2.jpg", "img/img3.jpg"] 

async def init_bot():
    await bot.set_my_commands([
        types.BotCommand(command="help", description="Помощь")
    ])

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(types.KeyboardButton(text="О боте"))
kb.add(types.KeyboardButton(text="Помощь"))

markup = types.InlineKeyboardMarkup()
markup.add(
    types.InlineKeyboardButton("сколько время", callback_data="get_date"),
    types.InlineKeyboardButton("/dev/urandom", callback_data="get_random"),
    types.InlineKeyboardButton("паблик чтобы листать пока какаешь", callback_data="get_meme")
)

@bot.message_handler(commands=['start'])
async def handle_start(message: Message):
    await bot.send_message(message.chat.id, "ботяра майнкрафт", reply_markup=kb)
    # await bot.send_message(message.chat.id, "", reply_markup=kb)

@bot.message_handler(func=lambda message: message.text == "О боте")
async def handle_any(message: Message):
    await bot.send_message(message.chat.id, "нормальный такой бот", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Помощь")
async def handle_any(message: Message):
    await bot.send_message(message.chat.id, "не чето не хочу пока", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
async def handle_any(message: Message):
    await bot.send_message(message.chat.id, "не понял, повтори пожалуйста", reply_markup=kb)

@bot.callback_query_handler(func=lambda call: True)
async def callback_handler(call):
    if call.data == "get_date":
        await bot.send_message(call.message.chat.id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    elif call.data == "get_random":
        await bot.send_message(call.message.chat.id, random.randint(1, 100))

    elif call.data == "get_meme":
        with open(random.choice(paths), "rb") as meme:
            await bot.send_photo(call.message.chat.id, meme)

async def main():
    await bot.polling()
    await init_bot()
    
if __name__ == "__main__":
    asyncio.run(main())