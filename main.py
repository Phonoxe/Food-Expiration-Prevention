import src.registeredItems as registeredItems
import src.modifyItems as modifyItems

ended = False

while not ended:
    print("What do you want to do ?")
    print("1. Add an item")
    print("2. See the list of items")
    print("3. Delete an item")
    print("4. Exit")
    choice = input("Enter your choice (1, 2, 3 or 4): ")
    if choice == "1":
        modifyItems.RegisterNewProduct()
    elif choice == "2":
        registeredItems.PrintItems()
    elif choice == "3":
        modifyItems.DeleteExistingProduct()
    elif choice == "4":
        ended = True
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
