# CRUD operations for product details.
products = [{"id": 1, "name": "Keyboard", "price": 800, "quantity": 10}]
while True:
    print("\\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    choice = input("Choose: ")
    if choice == "1":
        products.append({"id": int(input("Product ID: ")), "name": input("Name: "), "price": float(input("Price: ")), "quantity": int(input("Quantity: "))})
    elif choice == "2":
        for product in products: print(product)
    elif choice == "3":
        pid = int(input("Product ID: "))
        for product in products:
            if product["id"] == pid:
                product["price"], product["quantity"] = float(input("New price: ")), int(input("New quantity: "))
                break
        else: print("Product not found.")
    elif choice == "4":
        pid = int(input("Product ID: "))
        old = len(products)
        products = [p for p in products if p["id"] != pid]
        print("Deleted." if len(products) < old else "Product not found.")
    elif choice == "5": break
    else: print("Invalid choice.")
