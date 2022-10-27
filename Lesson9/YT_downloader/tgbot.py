from dowloader import *
from aiogram import *
from config import *
from pytube import YouTube

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Hi! I'm a bot to download video from YouTube.\n"
                                    " Just send me link to the video")


@dp.message_handler()
async def get_link(message: types.Message):
    chat_id = message.chat.id
    link = message.text
    if link.__contains__('youtube.com') or link.__contains__('youtu.be'):
        video = YouTube(link)
        await bot.send_message(chat_id, f'Starting download video [{video.title}] from channel [{video.author}]')
        await download(link, message, bot)
    else:
        await bot.send_message(chat_id, "Can't recognize your url, please send me the link from Youtube")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
