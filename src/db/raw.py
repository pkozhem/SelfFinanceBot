import datetime
from src.db.core import get_cursor


cursor = get_cursor()


def today_expenses_query() -> str:
    """ Returns expenses summary for today from result query. """

    cursor.execute(
        "SELECT SUM(price) "
        "FROM Expense "
        "WHERE date(date_created) = date('now', 'localtime')"
    )
    result = cursor.fetchall()[0][0]

    if not result:
        return f"No expenses this day"

    return result


def month_expenses_query(time_now: datetime.datetime) -> str:
    """ Returns expenses summary for this month from result query. """

    first_day_month = f'{time_now.year:04d}-{time_now.month:02d}-01'

    cursor.execute(
        "SELECT SUM(price) "
        "FROM Expense "
        f"WHERE date(date_created) >= {first_day_month}"
    )
    result = cursor.fetchall()[0][0]

    if not result:
        return f"No expenses this month"

    return result


def last_expenses_query() -> list:
    """ Returns query of 5 last expenses. """

    cursor.execute(
        "SELECT E.id_expense, E.price, C.name "
        "FROM Expense E LEFT JOIN Category C "
        "ON E.id_category = C.id_category "
        "ORDER BY date_created DESC "
        "LIMIT 5")
    rows = cursor.fetchall()

    return rows
