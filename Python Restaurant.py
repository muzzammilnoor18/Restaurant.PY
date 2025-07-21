# Define the menu of the restaurant
menu = {
    'Pizza': 600,
    'Pasta': 500,
    'Burger': 450,
    'Salad': 70,
    'Cold Drink': 80,
    'Coffee': 250,
    'Tea': 200,
    'Water': 60
}

# Greet
print("Welcome to PYTHON Restaurant")
print("\nHere is our menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0

while True:
    item = input("\nEnter the name of the item you want to order: ").strip()
    if item in menu:
        order_total += menu[item]
        print(f"Your item '{item}' has been added to your order.")
    else:
        print(f"Ordered item '{item}' is not available!")

    another = input("Do you want to order another item? (Yes/No): ").strip().lower()
    if another != 'yes':
        break

print("\nThe total amount to pay is Rs", order_total)