# Camille S. Munoz
# Student ID: 2020049
# Section: CPE2A

def display(budget):
    """
                                      FOOD MENU

        DRINKS:                       SNACKS:                 MEALS:
         Soda ----------- P29.95      Bread ---- P15.00      Tapsilog ---- P80.99
         Bottled Water -- P20.00      Apple ---- P20.50      Porksilog --- P80.99
         Coffee --------- P50.00      Banana --- P15.00
         Tea ------------ P35.50      Oranges -- 25.10
    """

    while True:
        import list
        print(display.__doc__)
        budget_049 = str(round(budget, 2))
        print('Type quit if you are done')
        print("Wallet: " + budget_049)
        buy = input("Choose the food you like to buy: ")

        if buy.title() == "Soda":
            worth = str(list.priceitem_049.get("Soda"))
            stock = str(list.stocksoffoods_049.get("Soda"))

            if list.stocksoffoods_049.get("Soda") <= 0:
                print("The food is out of stock")
            else:
                print("Price: " + worth)
                print("Available: " + stock)
                if list.stocksoffoods_049.get("Soda") <= 0:
                    print("The food is out of stock")
                elif list.stocksoffoods_049.get("Soda") > 0:
                    if (budget - list.priceitem_049.get("Soda")) < 0:
                        print("You don't have enough money to buy this")
                    else:
                        list.stocksoffoods_049["Soda"] -= 1
                        budget -= list.priceitem_049.get("Soda")
                        list.uorder_049.append(buy)

        if buy.title() == "Bottle Water":
            worth = str(list.priceitem_049.get("Bottle Water"))
            stock = str(list.stocksoffoods_049.get("Bottle Water"))

            if list.stocksoffoods_049.get("Bottle Water") <= 0:
                print("The food is out of stock")
            else:
                print("Price: " + worth)
                print("Available: " + stock)
                if list.stocksoffoods_049.get("Bottle Water") <= 0:
                    print("The food is out of stock")
                elif list.stocksoffoods_049.get("Bottle Water") > 0:
                    if (budget - list.priceitem_049.get("Bottle Water")) < 0:
                        print("You don't have enough money to buy this")
                    else:
                        list.stocksoffoods_049["Bottle Water"] -= 1
                        budget -= list.priceitem_049.get("Bottle Water")
                        list.uorder_049.append(buy)

        if buy.title() == "Coffee":
            worth = str(list.priceitem_049.get("Coffee"))
            stock = str(list.stocksoffoods_049.get("Coffee"))

            if list.stocksoffoods_049.get("Coffee") <= 0:
                print("The food is out of stock")
            else:
                print("Price: " + worth)
                print("Available: " + stock)
                if list.stocksoffoods_049.get("Coffee") <= 0:
                    print("The food is out of stock")
                elif list.stocksoffoods_049.get("Coffee") > 0:
                    if (budget - list.priceitem_049.get("Coffee")) < 0:
                        print("You don't have enough money to buy this")
                    else:
                        list.stocksoffoods_049["Coffee"] -= 1
                        budget -= list.priceitem_049.get("Coffee")
                        list.uorder_049.append(buy)

        if buy.title() == "Tea":
            worth = str(list.priceitem_049.get("Tea"))
            stock = str(list.stocksoffoods_049.get("Tea"))

            if list.stocksoffoods_049.get("Tea") <= 0:
                print("The food is out of stock")
            else:
                print("Price: " + worth)
                print("Available: " + stock)
                if list.stocksoffoods_049.get("Tea") <= 0:
                    print("The food is out of stock")
                elif list.stocksoffoods_049.get("Tea") > 0:
                    if (budget - list.priceitem_049.get("Tea")) < 0:
                        print("You don't have enough money to buy this")
                    else:
                        list.stocksoffoods_049["Tea"] -= 1
                        budget -= list.priceitem_049.get("Tea")
                        list.uorder_049.append(buy)

        if buy.title() == "Bread":
            worth = str(list.priceitem_049.get("Bread"))
            stock = str(list.stocksoffoods_049.get("Bread"))

            if list.stocksoffoods_049.get("Bread") <= 0:
                print("The food is out of stock")
            else:
                print("Price: " + worth)
                print("Available: " + stock)
                if list.stocksoffoods_049.get("Bread") <= 0:
                    print("The food is out of stock")
                elif list.stocksoffoods_049.get("Bread") > 0:
                    if (budget - list.priceitem_049.get("Bread")) < 0:
                        print("You don't have enough money to buy this")
                    else:
                        list.stocksoffoods_049["Bread"] -= 1
                        budget -= list.priceitem_049.get("Bread")
                        list.uorder_049.append(buy)

        if buy.title() == "Apple":
            worth = str(list.priceitem_049.get("Apple"))
            stock = str(list.stocksoffoods_049.get("Apple"))

            if list.stocksoffoods_049.get("Apple") <= 0:
                print("The food is out of stock")
            else:
                print("Price: " + worth)
                print("Available: " + stock)
                if list.stocksoffoods_049.get("Apple") <= 0:
                    print("The food is out of stock")
                elif list.stocksoffoods_049.get("Apple") > 0:
                    if (budget - list.priceitem_049.get("Apple")) < 0:
                        print("You don't have enough money to buy this")
                    else:
                        list.stocksoffoods_049["Apple"] -= 1
                        budget -= list.priceitem_049.get("Apple")
                        list.uorder_049.append(buy)

        if buy.title() == "Banana":
            worth = str(list.priceitem_049.get("Banana"))
            stock = str(list.stocksoffoods_049.get("Banana"))

            if list.stocksoffoods_049.get("Banana") <= 0:
                print("The food is out of stock")
            else:
                print("Price: " + worth)
                print("Available: " + stock)
                if list.stocksoffoods_049.get("Banana") <= 0:
                    print("The food is out of stock")
                elif list.stocksoffoods_049.get("Banana") > 0:
                    if (budget - list.priceitem_049.get("Banana")) < 0:
                        print("You don't have enough money to buy this")
                    else:
                        list.stocksoffoods_049["Banana"] -= 1
                        budget -= list.priceitem_049.get("Banana")
                        list.uorder_049.append(buy)

        if buy.title() == "Oranges":
            worth = str(list.priceitem_049.get("Oranges"))
            stock = str(list.stocksoffoods_049.get("Oranges"))

            if list.stocksoffoods_049.get("Oranges") <= 0:
                print("The food is out of stock")
            else:
                print("Price: " + worth)
                print("Available: " + stock)
                if list.stocksoffoods_049.get("Oranges") <= 0:
                    print("The food is out of stock")
                elif list.stocksoffoods_049.get("Oranges") > 0:
                    if (budget - list.priceitem_049.get("Oranges")) < 0:
                        print("You don't have enough money to buy this")
                    else:
                        list.stocksoffoods_049["Oranges"] -= 1
                        budget -= list.priceitem_049.get("Oranges")
                        list.uorder_049.append(buy)

        if buy.title() == "Tapsilog":
            worth = str(list.priceitem_049.get("Tapsilog"))
            stock = str(list.stocksoffoods_049.get("Tapsilog"))

            if list.stocksoffoods_049.get("Tapsilog") <= 0:
                print("The food is out of stock")
            else:
                print("Price: " + worth)
                print("Available: " + stock)
                if list.stocksoffoods_049.get("Tapsilog") <= 0:
                    print("The food is out of stock")
                elif list.stocksoffoods_049.get("Tapsilog") > 0:
                    if (budget - list.priceitem_049.get("Tapsilog")) < 0:
                        print("You don't have enough money to buy this")
                    else:
                        list.stocksoffoods_049["Tapsilog"] -= 1
                        budget -= list.priceitem_049.get("Tapsilog")
                        list.uorder_049.append(buy)

        if buy.title() == "Porksilog":
            worth = str(list.priceitem_049.get("Porksilog"))
            stock = str(list.stocksoffoods_049.get("Porksilog"))

            if list.stocksoffoods_049.get("Porksilog") <= 0:
                print("The food is out of stock")
            else:
                print("Price: " + worth)
                print("Available: " + stock)
                if list.stocksoffoods_049.get("Porksilog") <= 0:
                    print("The food is out of stock")
                elif list.stocksoffoods_049.get("Porksilog") > 0:
                    if (budget - list.priceitem_049.get("Porksilog")) < 0:
                        print("You don't have enough money to buy this")
                    else:
                        list.stocksoffoods_049["Porksilog"] -= 1
                        budget -= list.priceitem_049.get("Porksilog")
                        list.uorder_049.append(buy)

        # RECEIPT
        if buy.title() == 'Quit':
            import student_data
            import list

            with open('receipt.html', 'w') as file:
                file.write('\n           Your  Receipt:')
                file.write('<br>')
                file.write('\nCustomer Name: ' + student_data.info['Name'].title() + '\n')
                file.write('<br>')
                file.write('\n')
                file.write('<br>')
                file.write("\n%-20s%-20s" % ('Name:', '    Cost: '))
                for order in list.uorder_049:
                    file.write("\n%-20s%-20s" % (order + '<br>', str(round(list.priceitem_049[order], 2))))
                    list.utotal_049.append(list.priceitem_049[order])

                overall = sum(list.utotal_049)
                file.write('<br>')
                file.write("\n%-20s%-20s" % ('Total:', str(round(overall, 2))))
                file.write('<br>')
                file.write("\n%-20s%-20s" % ('Money:', str(round(float(student_data.info['money']), 2))))
                file.write('<br>')
                change = float(student_data.info['money']) - float(overall)
                file.write('<br>')
                file.write("\n%-20s%-20s" % ('Change:', str(round(float(change), 2))))
                file.write('<br>')
                print("Thank you! Come Again.\n")
                exit()



def studentdata():
    import student_data
    budget = student_data.info.get("money")
    display(budget)


studentdata()