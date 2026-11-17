
inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

print("=" * 39)
print("        INVENTORY CONTROL SYSTEM")
print("=" * 39)
print()

while True:
    print("Select an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")
    print()

    choice = input("Enter your choice (1-5): ")
    print()

    if choice == "1":
        print("--- Current Inventory ---")
        for i in range(len(inventory)):
            print(f"{i + 1}. {inventory[i]}")
        print()


    elif choice == "2":
        item = input("Enter item name to add: ")
        inventory.append(item)
        print(f'[SUCCESS] "{item}" added to inventory.')
        print()


    elif choice == "3":
        item = input("Enter item name to remove: ")
        if item in inventory:
            inventory.remove(item)
            print(f'[SUCCESS] "{item}" removed from inventory.')
        else:
            print(f'[ERROR] "{item}" not found in inventory.')
        print()


    elif choice == "4":
        inventory.sort()
        print("[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")
        for i in range(len(inventory)):
            print(f"{i + 1}. {inventory[i]}")
        print()

    elif choice == "5":
        print("Exiting Inventory Control System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number from 1 to 5.")
        print()