user_list = []
class UserOperations:
    def __init__(self, user):
        self.user = user

    def add_user(self):
        if self.user not in user_list:
            user_list.append(self.user)
            print(f"{self.user} has been added.")
        else:
            print(f"{self.user} is already registered.")

    def view_user_details(self, user):
        if user in user_list:
            print(user)
        else:
            print("That user is not registered.")

    def display_all_users(self):
        if len(user_list) > 0:
            for user in user_list:
                print(user)
        else:
            print("There are no users registered.")
