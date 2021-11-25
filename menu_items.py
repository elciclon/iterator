from abc import ABC, abstractmethod


class MenuItem(ABC):
    """
    Abstract class for menu items
    """

    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def is_vegetarian(self):
        return self.vegetarian


class Iterator(ABC):
    """
    Abstract class for iterator
    """

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


class DinerMenuIterator(Iterator):
    """
    Iterator for DinerMenu
    """

    position = 0

    def __init__(self, items):
        self.items = items

    def next(self):
        menu_item = self.items[self.position]
        self.position += 1
        return menu_item

    def has_next(self):
        return self.position < len(self.items)


class PancakeHouseIterator(Iterator):
    """
    Iterator for PancakeHouseMenu
    """

    position = 0

    def __init__(self, items):
        self.items = items

    def next(self):
        menu_item = self.items[self.position]
        self.position += 1
        return menu_item

    def has_next(self):
        return self.position < len(self.items)


class PancakeHouseMenu:
    def __init__(self):
        self.menu_items = []

        self.add_item(
            "K&B's Pancake Breakfast",
            "Pancakes with scrambled eggs, and toast",
            True,
            2.99,
        )

        self.add_item(
            "Regular Pancake Breakfast",
            "Pancakes with fried eggs, sausage",
            False,
            2.99,
        )

        self.add_item(
            "Blueberry Pancakes",
            "Pancakes made with fresh blueberries",
            True,
            3.49,
        )

        self.add_item(
            "Waffles",
            "Waffles, with your choice of blueberries or strawberries",
            True,
            3.59,
        )

    def add_item(self, name, description, vegetarian, price):
        self.menu_item = MenuItem(name, description, vegetarian, price)
        self.menu_items.append(self.menu_item)

    def create_iterator(self):
        return PancakeHouseIterator(self.menu_items)


class DinerMenu:
    def __init__(self):
        self.menu_items = []

        self.add_item(
            "Vegetarian BLT",
            "(Fakin') Bacon with lettuce & tomato on whole wheat",
            True,
            2.99,
        )

        self.add_item(
            "BLT",
            "Bacon with lettuce & tomato on whole wheat",
            False,
            2.99,
        )

        self.add_item(
            "Soup of the day",
            "Soup of the day, with a side of potato salad",
            False,
            3.29,
        )

        self.add_item(
            "Hotdog",
            "A hot dog, with saurkraut, relish, onions, topped with cheese",
            False,
            3.05,
        )

    def add_item(self, name, description, vegetarian, price):
        self.menu_item = MenuItem(name, description, vegetarian, price)
        self.menu_items.append(self.menu_item)

    def create_iterator(self):
        return DinerMenuIterator(self.menu_items)


pancake_house_menu = PancakeHouseMenu()
breakfast_items = pancake_house_menu.get_menu_items()

diner_menu = DinerMenu()
lunch_items = diner_menu.get_menu_items()

for item in breakfast_items:
    print(
        str(item.get_name())
        + " "
        + str(item.get_price())
        + " "
        + str(item.get_description())
    )
