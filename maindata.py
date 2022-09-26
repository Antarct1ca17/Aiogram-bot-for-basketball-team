from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


GROUP_ID = "group id"


URL_APP = 'https://newybpbot.herokuapp.com/'
bot = Bot(token = "your token")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

