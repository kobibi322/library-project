books_list = [{"id": 1, "name": "Harry Potter", "author": "J.K. Rowling", "year": 1997, "available": True},
    {"id": 2, "name": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "available": True},
    {"id": 3, "name": "Clean Code", "author": "Robert Martin", "year": 2008, "available": False},
    {"id": 4,"name": "Atomic Habits", "author": "James Clear", "year": 2018, "available": True},
    {"id": 5,"name": "The Pragmatic Programmer", "author": "David Thomas", "year": 1999, "available": False}
    ]

"""functions"""
def display_books(books_list)->None:
    print(books_list)

def search_book(books_list, name)->dict | None:
    for book in books_list:
        book_slice = book["name"][:len(name)]
        if name == book_slice:
            return book

def add_book(books_list, name, author, year)->bool:
    book_id = get_next_book_id(books_list)   
    books_list.append({"id":book_id, "name":name, "author":author, "year":year, "available":True})
    return True

def borrow_book(books_list, book_id)->bool:
    for book in books_list:
        if book_id == book["id"]:
            book_to_borrow = validate_book_to_borrow(book)
            book_to_borrow["available"] = False
            return True
    raise ValueError(f"book not exist")

def return_book(books_list, book_id)->bool:
    for book in books_list:
        if book["id"] == book_id:
            book_to_return = validate_book_to_return(book)
            book["available"] = True
            return True
    raise ValueError(f"book already returned")

def get_available_books(books_list)->list:
    available_books = []
    for book in books_list:
        if book["available"]:
            available_books.append(book)
    return available_books 

def display_available_books(books_list):
    print(get_available_books(books_list))     

def get_books_by_author(books_list, author)->list:
    author_books = []
    for book in books_list:
        if book["author"] == author:
            author_books.append(book)
    return author_books

def get_next_book_id(books_list)->int:
    book = max(books_list, key=lambda b:b["id"])
    book_id = book["id"] + 1
    return book_id

"""get inputs"""
def get_book_to_add(books_list)->tuple:
    name = get_book_name()
    author = get_book_author()
    validate_book_and_author(books_list, name, author)
    year = input("book year: ").strip()
    validate_integer(year)
    return name, author, year

def get_book_name()->str:
    book_name = input("book name: ").strip()
    return book_name

def get_book_author()->str:
    book_author = input("book author: ").strip()
    return book_author

def get_book_id()->str:
    book_id = input("book ID: ").strip()
    validate_integer(book_id)
    return book_id

def get_input_menu()->str:
    user_choice = input("""
    ================================
        LIBRARY MANAGEMENT
    ================================

    1. Display all books
    2. Search book by name
    3. Add new book
    4. Borrow a book
    5. Return a book
    6. Display available books
    7. Display books by author
    8. Exit
    Choose an option: """).strip()
    validate_integer(user_choice)
    return user_choice

"""validations"""
def validate_integer(val):
    try:
        int_val = int(val)
    except ValueError:
        raise ValueError("must be integer!")
    else:
        if int_val <= 0:
            raise ValueError("must be positive")

def validate_book_and_author(books_list, name, author):
    if not name or not author:
        raise ValueError(f"name or author cannot be empty!")
    for book in books_list:
        if book["name"] == name and book["author"] == author:
            raise ValueError(f"{name} and {author} already exist!")

def validate_book_to_borrow(book):
    if not book["available"]:
        raise ValueError(f"book already borrowed")
    return book

def validate_book_to_return(book):
    if book["available"]:
        raise ValueError(f"book already returned")
    return book

"""main"""
def main():
    user_choice = ""
    while user_choice != "8":
        try:
            user_choice = get_input_menu()
        except ValueError as e:
            print(f"Error: {e}")
        if user_choice == "1":
            display_books(books_list)
        elif user_choice == "2":
            try:
                name = get_book_name()
                search_book(books_list, name)
            except ValueError as e:
                print(f"Error: {e}")
        elif user_choice == "3":
            try:
                name, author, year = get_book_to_add()
                add_book(books_list, name, author, int(year))
            except ValueError as e:
                print(f"Error: {e}")
        elif user_choice == "4":
            try:
                book_id = int(get_book_id())
                borrow_book(books_list, book_id)
            except ValueError as e:
                print(f"Error: {e}")
        elif user_choice == "5":
            try:
                book_id = int(get_book_id())
                return_book(books_list, book_id)
            except ValueError as e:
                print(f"Error: {e}")
        elif user_choice == "6":
            available_books = get_available_books(books_list)
            display_books(available_books)
        elif user_choice == "7":
            try:
                author = get_book_author()
                display_books_by_author(books_list, author)
            except ValueError as e:
                print(f"Error: {e}")
        elif user_choice != "8":
            print("must be 1-8")
    

if __name__ == "__main__":
    main()
