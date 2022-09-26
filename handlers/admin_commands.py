from aiogram import Dispatcher
from aiogram.types import Message
from maindata import dp, bot 
from keyboard.admin_keyboard import admin_kb

ID = 'None' 
#@dp.message_handler(commands=['start'], is_chat_admin=True)
async def command_start(message: Message):
    global ID                 #Way to check if the user who is using commands is an admin
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, text = "Hi", reply_markup=admin_kb)
    

def register_handlers_admin_commands(dp:Dispatcher):
    dp.register_message_handler(command_start, commands=['start'], is_chat_admin=True)
    
    