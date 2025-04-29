
# Urb-Ex App (Improved Version)
# Final Project
# Created by Oyindamola Bade-Ojo

import time

def welcome_message():
    print("\n--- Welcome to Urb-Ex! ---")
    print("Explore abandoned places. Drop pins. Earn points. Unlock avatar items.\n")

# User data
user = {
    "name": "",
    "points": 0,
    "pins": [],
    "avatar_items": []
}

# Avatar store (item: cost)
avatar_store = {
    "Explorer Hat": 15,
    "Backpack Upgrade": 10,
    "Camera Accessory": 20
}

# Add a new location
def add_pin():
    location = input("Enter the name of the location: ")
    description = input("Enter a short description: ")
    hazard = input("Enter any hazard warnings (or type 'None'): ")
    
    pin = {
        "Location": location,
        "Description": description,
        "Hazard": hazard
    }
    user["pins"].append(pin)
    user["points"] += 10

    print(f"\n✅ You dropped a new pin at {location}! (+10 points)")
    print(f"You now have {user['points']} points.")

# View all pins
def view_pins():
    if not user["pins"]:
        print("\nYou haven't added any pins yet.")
    else:
        print("\n--- Your Added Pins ---")
        for i, pin in enumerate(user["pins"], 1):
            print(f"{i}. {pin['Location']} - {pin['Description']} (Hazard: {pin['Hazard']})")

# Buy an avatar item
def buy_avatar_item():
    print("\n--- Avatar Store ---")
    for item, cost in avatar_store.items():
        print(f"{item}: {cost} points")
    
    choice = input("\nEnter the name of the item you want to buy: ").title()
    if choice in avatar_store:
        if user["points"] >= avatar_store[choice]:
            user["points"] -= avatar_store[choice]
            user["avatar_items"].append(choice)
            print(f"🎉 You bought {choice}!")
            print(f"You now have {user['points']} points.")
        else:
            print("❌ You don't have enough points for that item.")
    else:
        print("❌ Item not found. Check spelling and try again.")

# View profile
def view_profile():
    print("\n--- Your Profile ---")
    print(f"Name: {user['name']}")
    print(f"Points: {user['points']}")
    print(f"Pins Added: {len(user['pins'])}")
    print(f"Avatar Items: {user['avatar_items']}")

# Main menu
def main_menu():
    while True:
        print("\nWhat would you like to do?")
        print("1. Drop a new pin")
        print("2. View all pins")
        print("3. Buy avatar items")
        print("4. View profile")
        print("5. Exit app")
        
        choice = input("Enter your choice (1-5): ")
        time.sleep(0.5)
        
        if choice == "1":
            add_pin()
        elif choice == "2":
            view_pins()
        elif choice == "3":
            buy_avatar_item()
        elif choice == "4":
            view_profile()
        elif choice == "5":
            print("\nThank you for exploring with Urb-Ex. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please select a valid option.")

# Run the app
def start_app():
    welcome_message()
    user["name"] = input("Enter your explorer name: ")
    print(f"\nWelcome, {user['name']}! Let's start exploring.")
    time.sleep(1)
    main_menu()

# Start everything
start_app()
