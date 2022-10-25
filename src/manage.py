""" Telegram Bot server. """

import logging
import settings
from aiogram import Bot, Dispatcher, executor
from src.middlewares import AccessMiddleware
from src.db.core import database_state, fetchall_explain
from src.categories import Categories

print(fetchall_explain())
print(Categories().get_categories())


print("Checking database state: ")
database_state()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(settings.ACCESS_ID))


@dp.message_handler(commands=["start", "help"])
async def start_help_command(message) -> None:
    """ Shows /start and /help message. """

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
async def add_expenses(message) -> None:
    """ Function which adds expense. """

    pass


@dp.message_handler(commands=["categories"])
async def categories(message) -> None:
    """ Shows all categories. """

    pass


@dp.message_handler(commands=["today"])
async def today_expenses(message) -> None:
    """ Shows expenses summary for today. """

    pass


@dp.message_handler(commands=["month"])
async def month_expenses(message) -> None:
    """ Shows expenses summary for this month. """

    pass


@dp.message_handler(lambda message: message.text.startwith("/delete"))
async def delete_expenses(message) -> None:
    """ Deletes chosen expense. """

    pass


@dp.message_handler(commands=["last"])
async def last_expenses(message) -> None:
    """ Shows last 5 expenses. """

    pass


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
