
author_list = []
class AuthorOperations:
    def __init__(self, author):
        self.author = author

    def add_new_author(self):
        if self.author not in author_list:
            author_list.append(self.author)
            print(f"{self.author} has been added.")
        else:
            print("That author is already in the system.")

    def view_author_details(self, author):
        if author in author_list:
            print(author)
        else:
            print("That author is not registered.")

    def view_all_authors(self):
        if len(author_list) > 0:
            for author in author_list:
                print(author)
        else:
            print("There are no authors registered.")


    