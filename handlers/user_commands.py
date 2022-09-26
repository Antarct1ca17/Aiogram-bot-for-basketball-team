from aiogram import Dispatcher
from aiogram.types import Message
from funcs.get_stat import get_stats
from maindata import dp

#@dp.message_handler(commands=["stats"])
async def command_stats(message: Message):
    await message.answer(get_stats())

#@dp.message_handler(commands="info")
async def get_info(message:Message):
    await message.answer("/stats - get actual statistic \n/schedule - get actual schedule")



#@dp.message_handler(commands='schedule')
async def get_schedule(message:Message):
    await message.answer("Wiśniowa góra | April 12 Tuesday | 19:40 | Court B\nSurchem-Brukland | April 19 Tuesday | 19:40 | Court B")


def register_handlers_user(dp:Dispatcher):
    dp.register_message_handler(command_stats, commands=['stats'])
    dp.register_message_handler(get_schedule, commands='schedule')
    dp.register_message_handler(get_info, commands='info')