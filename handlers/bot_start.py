from maindata import dp, bot
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import types



async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            #types.BotCommand("start", "Запустить бота"),
            types.BotCommand("stats", "show leaderboard"),
            types.BotCommand("schedule", "check future matches")
        ]
    )

