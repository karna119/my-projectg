def add_item(inventory, item_name, quantity):
    if item_name in inventory:
        print("Item already exists in inventory. Updating quantity.")
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    print(f"{quantity} {item_name}(s) added to inventory.")

def remove_item(inventory, item_name):
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from inventory.")
    else:
        print(f"{item_name} not found in inventory.")

def update_quantity(inventory, item_name, new_quantity):
    if item_name in inventory:
        inventory[item_name] = new_quantity
        print(f"Quantity of {item_name} updated to {new_quantity}.")
    else:
        print(f"{item_name} not found in inventory.")

def display_inventory(inventory):
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def main():
    inventory = {}

    # Adding items to inventory
    add_item(inventory, "Apples", 10)
    add_item(inventory, "Bananas", 15)
    add_item(inventory, "Oranges", 20)

    # Displaying inventory
    display_inventory(inventory)

    # Updating quantity of an item
    update_quantity(inventory, "Apples", 5)

    # Removing an item from inventory
    remove_item(inventory, "Bananas")

    # Displaying updated inventory
    display_inventory(inventory)

if __name__ == "__main__":
    main()
