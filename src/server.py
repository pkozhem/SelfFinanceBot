""" Telegram Bot server. """

import logging
from aiogram import Bot, Dispatcher, types

from src import settings
from src.middlewares import AccessMiddleware
from src.categories import Categories
from src import expenses


logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(settings.ACCESS_ID))


@dp.message_handler(commands=["start", "help"])
async def start_command(message: types.Message) -> None:
    """ Shows /start and /help message. """

    await message.answer(
        "Welcome to Self Finance Bot!\n\n"
        "Add expense: amount category_name\n"
        "Categories: /categories\n"
        "Today expenses: /today\n"
        "Last month expenses: /month\n"
        "Last 5 expenses: /last\n"
        "Delete expense: /delete{id}"
    )


@dp.message_handler(commands="categories")
async def show_categories(message: types.Message) -> None:
    """ Shows all categories. """

    categories = Categories().get_categories()
    answer = "{}{}".format(
        "Categories of expenses:\n\n*",
        "\n* ".join(["{}{}{}{}".format(c.name, " (", ", ".join(c.aliases), ")") for c in categories]))
    await message.answer(answer)


@dp.message_handler(commands="today")
async def today_expenses(message: types.Message) -> None:
    """ Shows expenses summary for today. """

    answer = expenses.today_expenses()
    await message.answer(answer)


@dp.message_handler(commands="month")
async def month_expenses(message: types.Message) -> None:
    """ Shows expenses summary for this month. """

    answer = expenses.month_expenses()
    await message.answer(answer)


@dp.message_handler(commands="last")
async def last_expenses(message: types.Message) -> None:
    """ Shows last 5 expenses. """

    last = expenses.last_expenses()

    if not last:
        await message.answer("No expenses yet")
        return

    last_rows = [
        f"{expense.price} on {expense.expense_category} — press "
        f"/delete{expense.id_expense} to delete"
        for expense in last]

    answer = "{}{}".format(
        "Latest expenses:\n\n*",
        "\n*".join(last_rows)
    )

    await message.answer(answer)


@dp.message_handler(lambda message: message.text.startswith('/delete'))
async def delete_expenses(message: types.Message) -> None:
    """ Deletes chosen expense. """
    pk = int(message.text[7:])
    expenses.delete_expense(pk)
    await message.answer("Expense deleted")


@dp.message_handler()
async def add_expenses(message: types.Message) -> None:
    """ Function which adds expense. """

    try:
        expense = expenses.add_expense(message.text)
    except Exception as E:
        await message.answer(str(E))
        return

    answer = (
        f"Added expenses: {expense.price} on {expense.expense_category}.\n\n"
        f"{expenses.today_expenses()}")
    await message.answer(answer)
