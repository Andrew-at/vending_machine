# Author: Andrew-at
# GitHub username: Andrew-at
# Date 5.21.24
# Description: console program imitating a vending machine using classes and objects

# Error/exception handling
class InvalidSalesItemError(Exception):
    pass


class MenuItem:
    """
    represents items in machine with:
    'name', 'cost' and 'price' values
    """
    def __init__(self, name: str, cost: int, price: float):
        self._name = name
        self._cost = cost
        self._price = price

    # return name str value
    def get_name(self):
        return self._name

    # return cost float value
    def get_cost(self):
        return self._cost

    # return selling price float value
    def get_price(self):
        return self._price


class SalesForDay:
    """
    represents sales for day;
    days open > name of items > number sold
    a dictionary whose keys are name of items and qty sold.
    """
    def __init__(self, number_of_days: int, sales_dictionary: dict):
        self._number_of_days = number_of_days
        self._sales_dictionary = sales_dictionary

    # returns number of days operating
    def get_day(self):
        return self._number_of_days

    # returns the sales dictionary
    def get_sales_dict(self):
        return self._sales_dictionary


class VendingMachine():
    """
    represents a vending machine with a name(str),
    the current day(int), a dictionary of menu items
    and a list of the sales for the day.
    """

    def __init__(self, name: str):
        self._name = name
        self._current_day = 0
        self._menu_items = {}
        self._sales_record = []

    # returns menu items
    def get_menu_items(self):
        machine = self._menu_items
        return machine

    # returns name of item
    def get_name(self):
        return self._name

    # adds menu items by updating the dictionary via assigning 'menu_object' as an object
    def add_menu_item(self, menu_object: MenuItem):
        self._menu_items.update({menu_object.get_name(): menu_object.get_price()})


def main():
    pass

# main function
if __name__ == "__main__":
    main()

# implement input later
