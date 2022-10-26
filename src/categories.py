""" Logic with categories. """

import db.core
from typing import NamedTuple


class CategoryLayout(NamedTuple):
    """ Layout of category in Python data. """

    id_category: str
    name: str
    aliases: list[str]


class Categories:
    def __init__(self):
        self._categories = self._get_categories_instances()

    def _get_categories_instances(self) -> list[CategoryLayout]:
        """ Returns a list of categories. """

        categories = db.core.fetchall_data("Category", "id_category name aliases".split())
        categories = self._create_categories_instances(categories)
        return categories

    @staticmethod
    def _create_categories_instances(categories: list[dict]) -> list[CategoryLayout]:
        """ Transforms list of dictionaries of data into
            a list of Category Layout with data. """

        categories_instances = []

        for index, category in enumerate(categories):
            aliases = category["aliases"].split(",")
            aliases = list(filter(None, map(str.strip, aliases)))
            aliases.append(category["name"])
            categories_instances.append(CategoryLayout(
                id_category=category['id_category'],
                name=category['name'],
                aliases=aliases
            ))

        return categories_instances

    def get_categories(self) -> list[CategoryLayout]:
        """ Returns a list of categories. """

        return self._categories

    def get_category(self, category_name: str) -> CategoryLayout:
        """ Returns a single category by name or its alias. """

        category_or_alias = None
        other = None

        for category in self._categories:
            if category.name == "others":
                other = category
            for alias in category.aliases:
                if category_name in alias:
                    category_or_alias = category

        if not category_or_alias:
            category_or_alias = other

        return category_or_alias
