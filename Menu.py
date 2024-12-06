from Book_Operations import BookOperations
from User_Operations import UserOperations
from Author_Operations import AuthorOperations



def main():
    print("Main Menu\n1. Book Operations \n2. User Operations \n3. Author Operations \n4.Quit")
    action = input("Please choose a number from the list above: ")
    my_book = BookOperations("test")
    my_user = UserOperations("test")
    my_author = AuthorOperations("test")
    while True:
        try:
            if action == "1":

                print("1. add \n2. borrow \n3. return \n4. search \n5. display \n6. quit")
                choice = input("Please choose a number from the list above: ")
                if choice == "1":
                    title = input("Enter the book name. ")
                    my_book = BookOperations(title)
                    my_book.add_book()
                elif choice == "2":
                    my_book.borrow_book()
                elif choice == "3":
                    my_book.return_book()
                elif choice == "4":
                    search_title = input("Enter the book to search for: ")
                    my_book.search_for_book(search_title)
                elif choice == "5":
                    my_book.display_all_books()
                else:
                    break
            elif action == "2":
                print("1. add a new user \n2. view user details \n3. display all users \n4. quit")
                choice = input("Choose a number from the list above: ")
                if choice == "1":
                    user = input("Enter the users name. ")
                    my_user = UserOperations(user)
                    my_user.add_user()
                elif choice == "2":
                    user_details = input("Enter the name of the user: ")
                    my_user.view_user_details(user_details)
                elif choice == "3":
                    my_user.display_all_users()
                else:
                    break
            elif action == "3":
                print("1. add new author \n2. view author details \n3. view all authors")
                choice = input("Choose a number from the list above: ")
                if choice == "1":
                    author = input("Enter the authors name.")
                    my_author = AuthorOperations(author)
                    my_author.add_new_author()
                elif choice == "2":
                    author_details = input("Enter the name of the author you want to view: ")
                    my_author.view_author_details(author_details)
                elif choice == "3":
                    my_author.view_all_authors()
                else:
                    quit
            else:
                break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()