menu = {
    'Pizza' : 50,
    'Pasta' : 50,
    'Burger' : 60,
    'Coffee' : 80,
    'Burrito' : 100,
}

print("Welcome the my restraunt")

print("--------------------------")

print("Pizza:50\n Pasta:50\n Burger:60\n Coffee:80\n Burrito:100\n")

orderBill = 0

item1 = input("What you want to order?")

if item1 in menu:
    orderBill+= menu[item1]
    print(f"Your item {item1} is added to your order")
else:
    print(f"{item1} is not available now")


another_order = input("Do you want to order another item? (Yes/No)")
if another_order == "Yes" or another_order == "yes":
    item2 = input("Enter the name of second item")
    if item2 in menu:
        orderBill+= menu[item2]

    else:
        print(f"Not available pls order something else")


print(f"your total order is {orderBill}")