# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 4
# Author Name: GABE 
# Date: 07 October 2026

# SCENARIO
# You are developing a registration system for a small event
# The organizers have a list of registered attendees and need to check whether someone is permitted to enter.

registered_guests = [
    "Alice",
    "Bob"
]
# TODO 1: Create a while loop that continues until all guests are checked in.
checked_in_guests = []
print(registered_guests)

while len(checked_in_guests) < len(registered_guests):

    # TODO 2: Ask the user to enter their name
    name = input("What is your name: ")

    # TODO 3: Iterate through guest list and check whether their name appears in the registered guests list
    is_registered = False
    for guest in registered_guests:
        if guest == name:
            is_registered = True

    # TODO 4: If registered and they're not already checked in, add them and print a welcome message
    if is_registered and name not in checked_in_guests:
        checked_in_guests.append(name)
        print(f"Welcome {name}!")
    elif is_registered:
        print(f"{name}, you're already checked in.")

    # TODO 5: Otherwise, display an appropriate message for unregistered guests
    else:
        print(f"Sorry {name}, your name isn't on the list.")

    # TODO 6: Print the updated checked-in list
    print(f"Checked In Guests: {checked_in_guests}")

# TODO 7: Print a message telling us that all guests have successfully checked in!
print("All guests have been checked in!")

# EXPECTED OUTPUT:
# [ "Alice", "Bob"]
# What is your name:  "Alice"
#    Welcome Alice!
#    Checked In Guests: [ Alice ]
# What is your name:  "Fred"
#    Sorry Fred, your name isn't on the list.
#    Checked In Guests: [ Alice ]
# What is your name:  "Bob"
#    Welcome Bob!
#    Checked In Guests: [ Alice, Bob ]
# All guests have been checked in!
