def generateReceipt(pizzaOrder):
    total = 0.00  # establish variables
    ans = 0
    extra = 0.00
    cost = 0.00
    sizePrice = []
    extraPrice = []
    if 0 == len(pizzaOrder):
        ans = 1  # used later to skip out of an if/else statement
        print("You did not order anything")
    else:
        for pizza in pizzaOrder:
            if pizza[0] == "S":
                cost = 7.99
                total += cost
            elif pizza[0] == "M":
                cost = 9.99
                total += cost
            elif pizza[0] == "L":
                cost = 11.99
                total += cost
            elif pizza[0] == "XL":
                cost = 13.99
                total += cost
            sizePrice.append(cost)  # collects the price of each pizza base ordered
            if 3 >= len(pizza[1]):  # if there are no extra toppings
                extra = 0.00
                total += extra
            elif 3 < len(pizza[1]):  # if there are extra toppings
                amt = len(pizza[1]) - 3
                if pizza[0] == "S":
                    extra = 0.50
                    total += extra * amt
                elif pizza[0] == "M":
                    extra = 0.75
                    total += extra * amt
                elif pizza[0] == "L":
                    extra = 1.00
                    total += extra * amt
                elif pizza[0] == "XL":
                    extra = 1.25
                    total += extra * amt
            extraPrice.append(extra)  # collects the price of extras toppings for each pizza
    if ans != 1:
        print("Your order:")
        num = 0
        count = 0
        for pizza in pizzaOrder:
            amt = len(pizza[1]) - 3
            num += 1

            if pizza[0] != "XL":  # to prevent the extra letter from causing misalignment
                print("Pizza %d: %s%20.2f" % (num, pizza[0], sizePrice[count]))
            else:
                print("Pizza %d: %s%19.2f" % (num, pizza[0], sizePrice[count]))

            for topping in pizza[1]:  # loops through and prints each topping for each order
                print("-", topping)

            if extraPrice[count] > 0.00:
                if pizza[0] != "XL":
                    for times in range(amt):  # prints the statement for the amount of extra toppings there are
                        print("Extra Topping (%s)%13.2f" % (pizza[0], extraPrice[count]))
                else:
                    for times in range(amt):
                        print("Extra Topping (%s)%12.2f" % (pizza[0], extraPrice[count]))

            count += 1

        tax = total * .13
        withTax = total + tax
        print("Tax:%26.2f" % tax)
        print("Total:%24.2f" % withTax)
