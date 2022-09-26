import asyncio
from aiogram.utils import executor
from maindata import dp, bot, URL_APP
from handlers.bot_start import set_default_commands
from handlers import admin_commands, user_commands, buttons
import os

async def on_startup(dp):
    await set_default_commands(dp)
    #await bot.set_webhook(URL_APP)

#async def on_shutdown(dp):
    #await bot.delete_webhook()


admin_commands.register_handlers_admin_commands(dp)
user_commands.register_handlers_user(dp)
buttons.register_handlers_buttons(dp)



if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.create_task(run_notify())
    # executor.start_webhook(
    # dispatcher=dp, 
    # webhook_path="", 
    # skip_updates=True, 
    # on_startup=on_startup, 
    # on_shutdown=on_shutdown, 
    # host="0.0.0.0", 
    # port = int(os.environ.get("PORT", 5000)))
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)