import re
import pytz
import datetime
from typing import NamedTuple, Optional

from src.settings import TIMEZONE
from src.db import core, raw
from src.categories import Categories


class Message(NamedTuple):
    """ Layout of message in Python data. """

    category_message: str
    price_message: int


class Expense(NamedTuple):
    """ Layout of expense in Python data. """

    id_expense: Optional[int]
    expense_category: str
    price: int


def add_expense(incoming_message: str) -> Expense:
    """ Adds new expense to database and returns instance of Expense. """

    parsed_message = _parse_incoming_message(incoming_message)
    category = Categories().get_category(parsed_message.category_message)

    core.insert_data("Expense", {
        "price": parsed_message.price_message,
        "expense_category": parsed_message.category_message,
        "date_created": _get_timezone_date_string(),
        "id_category": category.id_category
    })

    return Expense(
        id_expense=None,
        price=parsed_message.price_message,
        expense_category=category.name
    )


def today_expenses() -> str:
    """ Returns final answer with today expenses. """

    result = raw.today_expenses_query()
    return f"Today expenses: {result}"


def month_expenses() -> str:
    """ Returns final answer with month expenses. """

    result = raw.month_expenses_query(_get_timezone_date())
    return f"Month expenses: {result}"


def last_expenses() -> list[Expense]:
    """ Returns list of last expenses instances. """

    rows = raw.last_expenses_query()

    last = [Expense(
        id_expense=row[0],
        price=row[1],
        expense_category=row[2]) for row in rows]

    return last


def delete_expense(pk: int) -> str:
    """ Deletes an expense by its id. """

    core.delete_data("Expense", pk)
    return "Expense deleted."


def _parse_incoming_message(incoming_message: str) -> Message:
    """ Parses text from message into price and category. """

    regexp_result = re.match(r"([\d ]+) (.*)", incoming_message)
    if not regexp_result or not regexp_result.group(0) or not regexp_result.group(1) or not regexp_result.group(2):
        raise Exception(
            "Can't recognize the message. Type something like: 100 taxi")

    price_message = int(regexp_result.group(1).replace(" ", ""))
    category_message = regexp_result.group(2).strip().lower()
    return Message(
        price_message=price_message,
        category_message=category_message
    )


def _get_timezone_date() -> datetime.datetime:
    """ Returns current time in datetime. """

    timezone = pytz.timezone(TIMEZONE)
    time_now = datetime.datetime.now(timezone)
    return time_now


def _get_timezone_date_string() -> str:
    """ Returns current time in string. """

    return _get_timezone_date().strftime("%Y-%m-%d %H:%M:%S")
