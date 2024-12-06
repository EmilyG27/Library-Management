library = []
borrow_book = []
class BookOperations:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def add_book(self):
        if self.title not in library:
            library.append(self.title)
            print(f"Added {self.title} to the library.")
        else:
            print("That book is already in the library.")

    def borrow_book(self):
        borrow_title = input("Enter the title of the book to borrow: ")
        if borrow_title in library and borrow_title not in borrow_book:
            borrow_book.append(borrow_title)
            print(f"{borrow_title} has been checked out.")
        else:
            print("That book is not available.")

    def return_book(self):
        return_title = input("Enter the book to return: ")
        borrow_book.pop(return_title)
        print(f"{return_title} has been returned.")

    def search_for_book(self, title):
        if title in library:
            print(title)
        else:
            print("That book is not in the library.")

    def display_all_books(self):
        if len(library) > 0:
            for title in library:
                print(title)
        else:
            print("Your library is empty.")



