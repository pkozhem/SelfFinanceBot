import os
import logging
import aiohttp
import settings
from aiogram import Bot, Dispatcher, executor

from src.middlewares import AccessMiddleware
from src.database import state_database

print("Checking database state: ")
state_database()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(settings.ACCESS_ID))


@dp.message_handler(commands=["start", "help"])
async def start_help_command(message):
    await message.answer(
        "Welcome to Self Finance Bot!\n\n"
        "Add expense: 5 food\n"
        "Categories: /categories\n"
        "Today expenses: /today\n"
        "Last month expenses: /month\n"
        "Last 5 expenses: /last\n"
        "Delete expense: /delete expense_id"
    )


@dp.message_handler()
async def add_expenses(message):
    pass


@dp.message_handler(commands=["categories"])
async def categories(message):
    pass


@dp.message_handler(commands=["today"])
async def today_expenses(message):
    pass


@dp.message_handler(commands=["month"])
async def month_expenses(message):
    pass


@dp.message_handler(lambda message: message.text.startwith("/delete"))
async def delete_expenses(message):
    pass


@dp.message_handler(commands=["last"])
async def last_expenses(message):
    pass


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
