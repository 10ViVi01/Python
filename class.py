from email.policy import default
from random import choice
from re import S
import sys
from turtle import update
from unicodedata import name
import json
from types import SimpleNamespace
from webbrowser import get


class Items (object):
    items: list

    def __init__(self) -> None:
        with open("items.json", "r") as f:
            self.items = json.loads(f.read())

    def __repr__(self) -> str:
        return f"""
        ---------------------
        Product list:
        ---------------------
        {[f'{x["name"]} _____ {x["price"]}' for x in self]}
        """

    def __iter__(self):
        return iter(self.items)

    def add_item(self):
        dc = dict(name=input("Input item name "), price=int(input("Input item price ")))
        for item in self:
            if item["name"] == dc["name"]:
                item.update(dc)
                break
        else:
            self.items.append(dc)
        self.update_items()

    def update_items(self):
        with open("items.json", "w") as f:
            f.write(json.dumps(self.items, indent=4))

    def del_item(self):
        dc = dict(name=input("""
        ---------------------
        Enter name of product
        to delete (items):
        ---------------------
123
        =>  """))

        for item in self.items:
            if item["name"] == dc["name"]:
                self.items.remove(item)
                break
        else:
            print("Not found")
        self.update_items()

class ShoppingCart(object):
    cart: list
    items: Items

    def __init__(self, items: Items):
        self.cart = []
        self.items = items

    def add_in_cart(self):
        while True:
            choice_client = int(input("""
            ---------------------
            Add in cart?
            (1 - Yes, else - No)
            ---------------------

            =>  """))
            match choice_client:
                case 1:
                    dc = dict(name=input("Input item name "))
                    for item in self.items:
                        if item["name"] == dc["name"]:
                            self.cart.append(dict(name=item["name"], price=item["price"]))
                            break
                    else:
                        print("\nSorry, product not found! Try again?\n")
                case _:
                    break

    def __repr__(self) -> str:
        return f"""
        ---------------------
        Your cart:
        ---------------------
        {[f'{x["name"]} _____ {x["price"]}' for x in self.cart]}
        ---------------------
        Purchase price:
        {self.total}
        ---------------------
        """

    def del_from_cart(self):
        pass

    @property
    def total(self):
        return sum([p["price"] for p in self.cart])


def exit():
    sys.exit()

if __name__ == "__main__":
    items = Items()
    cart = ShoppingCart(items)


    dc = {1: items.add_item, 2: items.del_item, 3: items.__repr__, 4: cart.add_in_cart, 5: cart.del_from_cart, 6: cart.__repr__, 7: exit}

    while True:
        choice_client = int(input("""
        ---------------------
        МЕНЮ
        ---------------------
        Add product to base - 1
        Del product from base -2
        Print products from base - 3
        Add product to cart - 4
        Del product from cart - 5
        Print cart - 6
        Exit - 7
        ---------------------

        =>  """))
        if funс := dc.get(choice_client):
            funс()
        else:
            print("You write bad value, try again")
