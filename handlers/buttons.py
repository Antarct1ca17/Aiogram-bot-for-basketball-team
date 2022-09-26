from maindata import dp, bot, GROUP_ID
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from datetime import datetime, timedelta

class FSMAdmin(StatesGroup):
    training_data = State()
    match_data = State()

#@dp.message_handler(Text(equals=['Set training', 'Set match']), state = None)
async def set_action(message: Message):
    if message.text == 'Set training':
        await message.answer("Set training time (format 11 01 2022 11:11)")
        await FSMAdmin.training_data.set()
        await message.delete()
    elif message.text == 'Set match':
        await message.answer("Set match time (format 11 01 2022 11:11)")
        await FSMAdmin.match_data.set()
        await message.delete()

#@dp.message_handler(regexp="([0-2]{1}[0-9]{1})\s([0-1]{1}[0-9]{1})\s(\d{4})\s[0-2][0-9]:[0-5][0-9]", state = FSMAdmin.training_data)
async def training_info(message:Message, state:FSMContext):
    await message.reply(f"You've set training on {message.text}")
    await state.finish()
    def get_dif():
        data_info = datetime.strptime(message.text, "%d %m %Y %H:%M")
        today = datetime.now()
        delta = timedelta(hours=26, minutes = 0)
        difference = data_info - delta - today
        return difference.seconds 
    await asyncio.sleep(get_dif())
    await bot.send_message(chat_id=GROUP_ID, text= f"REMINDER! TRAINING IS ON {message.text}")
    

#@dp.message_handler(regexp="([0-2]{1}[0-9]{1})\s([0-1]{1}[0-9]{1})\s(\d{4})\s[0-2][0-9]:[0-5][0-9]", state = FSMAdmin.match_data)   
async def match_info(message:Message, state:FSMContext):
    await message.reply(f"You've set match on {message.text}")
    await state.finish()
    def get_dif():
        data_info = datetime.strptime(message.text, "%d %m %Y %H:%M")
        today = datetime.now()
        delta = timedelta(hours=26, minutes = 0)
        difference = data_info - delta - today
        return difference.seconds     
    await asyncio.sleep(get_dif())
    await bot.send_message(chat_id=GROUP_ID, text= f"REMINDER! MATCH IS ON {message.text}")

# #@dp.message_handler(commands="Hide")
# async def hide_keyboard(message:Message):
#     await bot.send_message(reply_markup=ReplyKeyboardRemove())
     

def register_handlers_buttons(dp:Dispatcher):
    dp.register_message_handler(set_action, Text(equals=['Set training', 'Set match']), state = None)  
    dp.register_message_handler(training_info, regexp="([0-2]{1}[0-9]{1})\s([0-1]{1}[0-9]{1})\s(\d{4})\s[0-2][0-9]:[0-5][0-9]", state = FSMAdmin.training_data)
    dp.register_message_handler(match_info, regexp="([0-2]{1}[0-9]{1})\s([0-1]{1}[0-9]{1})\s(\d{4})\s[0-2][0-9]:[0-5][0-9]", state = FSMAdmin.match_data)
    # dp.register_message_handler(hide_keyboard, commands='Hide')