order = input("Welcome to my Restaurant! What would you like to order? Our options are: Burger, Pizza, Pasta: ")

orderItems = []

if order.lower() == "pizza":
    orderItems.append("Pizza")
    print("Pizza Added")
    order2 = input("Your remaining options are: Burger, Pizza. Want to add another? If not please say no.")
    if order2.lower == "no":
        exit()
    else:
        orderItems.append(order2)
        print("Added", order2,"to cart")
        print("The items you ordered are: ", orderItems)
elif order.lower() == "burger":
    orderItems.append("Burger")
    print("Burger Added")
    order2 = input("Your remaining options are: Burger, Pizza. Want to add another? If not please say no.")
    if order2.lower == "no":
        exit()
    else:
        orderItems.append(order2)
        print("Added", order2,"to cart")
        print("The items you ordered are: ", orderItems)
elif order.lower() == "pasta":
    orderItems.append("Pasta")
    print("Pasta Added")
    order2 = input("Your remaining options are: Burger, Pizza. Want to add another? If not please say no.")
    if order2.lower == "no":
        exit()
    else:
        orderItems.append(order2)
        print("Added", order2,"to cart")
        print("The items you ordered are: ", orderItems)
else:
    print("Invalid Item")
    order2 = None