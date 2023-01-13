'''
Lecture: COMPSCI 1026A 002
Name: Jocelyn Chang

This code takes the user's input and generates their pizza order into a receipt.
'''

from pizzaReceipt import generateReceipt
TOPPING = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE",
           "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE")


def ingredients():
    listOfToppings = []  # will be appended to each time a valid topping is given
    toppings = input("Type in one of our toppings to add to your pizza. To see the list of toppings, enter \"LIST\". "
                     "When you are done adding toppings, enter \"X\"\n")
    toppings = toppings.upper()  # prevents code from being case-sensitive

    while toppings != "X":

        if toppings in TOPPING:
            listOfToppings.append(toppings)
            print(f'Added {toppings} to your pizza')
            toppings = input("Type in one of our toppings to add to your pizza. To see the list of toppings, enter \"LIST\". "
                             "When you are done adding toppings, enter \"X\"\n")
            toppings = toppings.upper()

        elif toppings == "LIST":
            print(TOPPING)
            toppings = input("Type in one of our toppings to add to your pizza. To see the list of toppings, enter \"LIST\". "
                             "When you are done adding toppings, enter \"X\"\n")
            toppings = toppings.upper()

        else:
            print("Invalid topping")
            toppings = input("Type in one of our toppings to add to your pizza. To see the list of toppings, enter \"LIST\". "
                             "When you are done adding toppings, enter \"X\"\n")
            toppings = toppings.upper()

    return listOfToppings


def howBig():
    size = input("Choose a size: S, M, L, or XL: ")
    size = size.upper()
    theSizes = ["S", "M", "L", "XL"]

    while size not in theSizes:  # will ask for sizes until a valid input is given
        size = input("Choose a size: S, M, L, or XL: ")
        size = size.upper()

    return size


pizzaOrder = []
ans = input("Do you want to order a pizza: ")
ans = ans.upper()

if ans != "Q" and ans != "NO":
    width = howBig()  # calls the function asking for pizza size
    pizza = ingredients()  # calls the function asking for ingredients on the pizza
    order = (width, pizza)
    pizzaOrder.append(order)

    theEnd = input("Do you want to continue ordering? ")
    theEnd = theEnd.upper()

    while theEnd != "Q" and theEnd != "NO":
        width = howBig()
        pizza = ingredients()
        order = (width, pizza)
        pizzaOrder.append(order)

        theEnd = input("Do you want to continue ordering? ")
        theEnd = theEnd.upper()
    print(pizzaOrder)
    generateReceipt(pizzaOrder)  # calls the other file that will generate receipt
else:
    generateReceipt(pizzaOrder)
