############################################################
print("Exercise 9.3")

class User:
    def __init__(self, first_name, last_name, age, location, height):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.location=location
        self.height=height

    def describe_self(self):
        print(f"Name: {self.first_name}")
        print(f"Surname: {self.last_name}")
        print(f"Height: {self.height}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")


myself=User("Ulrich", "Pentz", "44", "Joburg", "1.91m")

myself.describe_self()
myself.greet_user()

print("")
###################################################
print("Exercise 9.4")
        