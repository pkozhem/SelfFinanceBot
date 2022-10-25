from typing import NamedTuple, Optional


class Message(NamedTuple):
    """ Layout of message in Python data. """

    category_message: str
    amount: int


class Expense(NamedTuple):
    """ Layout of expense in Python data. """

    id: Optional[int]
    amount: int
    category_name: str
