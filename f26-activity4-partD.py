# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 4
# Author Name: GABE
# Date: 07 October 2026

# SCENARIO
# A restauraunt wants a simple ordering system that allows customers to browse a menu, select items, and calculate their total bill.

menu  = {
    "Burger" : 12.00,
    "Pizza" : 15.00,
    "Salad" : 9.00,
    "Fries" : 5.00,
    "Drink" : 3.00
}

order = []

# TODO 1: Print out the entire menu and the price of each item
menu_items = menu.items()
for item, price in menu_items:
    print(f"{item} - ${price:.2f}")

# TODO 2: Start a loop, asking the customer which item they would like to order
while True:
    choice = input("What would you like to order? (type Done to finish): ").strip().title()

    # TODO 5: If the customer types "Done", end the loop and move to end of order
    if choice == "Done":
        break

    # TODO 3: If the customer types a word, check whether the requested item exists
    if choice in menu:
        # TODO 4: Add valid items to the customer's order and let the loop continue
        order.append(choice)
        print(f"Added {choice} to your order.")
    else:
        print(f"Sorry, {choice} isn't on the menu.")

# TODO 6: Print out an itemized receipt for the user showing item and cost
subtotal = 0
for i in range(len(order)):
    item = order[i]
    price = menu[item]
    subtotal += price
    if i == 0:
        label = "Order: "
    else:
        label = "       "
    print(f"{label}{item:<6} - {price:5.2f}")

# TODO 7: Print out the subtotal of the entire order
print(f"        TOTAL: ${subtotal:.2f}")


# EXPECTED OUTPUT
# Order: Burger - 12.00
#        Fries  -  5.00
#        Drink  -  3.00
#         TOTAL: $20.00
