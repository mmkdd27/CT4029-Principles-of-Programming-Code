print("Menu:")
print("1. View Promotion 1")
print("2. View Promotion 2")
print("3. View Promotion 3")
print("4. Quit")

choice = input("Enter your choice: ")
if choice == "1":
    print("Title: Promotion 1")
    print("Description: Get 20% off on all electronics.")
    print("Expiry Date: 2023-12-31")
elif choice == "2":
    print("Title: Promotion 2")
    print("Description: Buy one, get one free on selected clothing items.")
    print("Expiry Date: 2023-11-30")
elif choice == "3":
    print("Title: Promotion 3")
    print("Description: Free shipping on orders over $50.")
    print("Expiry Date: 2023-12-15")
elif choice == "4":
    print("Quitting the program.")
else:
    print("Invalid choice. Please select a valid option.")
