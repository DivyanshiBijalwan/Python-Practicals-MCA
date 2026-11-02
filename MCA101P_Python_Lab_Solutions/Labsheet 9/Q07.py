# Menu-driven CRUD operations on a list of books.
books = [{"id": 1, "title": "Python Basics", "author": "A. Sharma"}]
while True:
    print("\\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    choice = input("Choose: ")
    if choice == "1":
        books.append({"id": int(input("Book ID: ")), "title": input("Title: "), "author": input("Author: ")})
    elif choice == "2":
        for book in books: print(book)
    elif choice == "3":
        book_id = int(input("Book ID: "))
        for book in books:
            if book["id"] == book_id:
                book["title"], book["author"] = input("New title: "), input("New author: ")
                break
        else: print("Book not found.")
    elif choice == "4":
        book_id = int(input("Book ID: "))
        old = len(books)
        books = [b for b in books if b["id"] != book_id]
        print("Deleted." if len(books) < old else "Book not found.")
    elif choice == "5": break
    else: print("Invalid choice.")
