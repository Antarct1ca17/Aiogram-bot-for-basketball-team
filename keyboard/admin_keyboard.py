from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Set training')
b2 = KeyboardButton('Set match')
#b3 = KeyboardButton('Hide')

admin_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(b1).add(b2)