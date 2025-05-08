from random import randint, choice

############################################################
# print("Exercise 9.3")

# class User:
#     def __init__(self, first_name, last_name, age, location, height):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#         self.location=location
#         self.height=height

#     def describe_self(self):
#         print(f"Name: {self.first_name}")
#         print(f"Surname: {self.last_name}")
#         print(f"Height: {self.height}")

#     def greet_user(self):
#         print(f"Hello {self.first_name} {self.last_name}")


# myself=User("Ulrich", "Pentz", "44", "Joburg", "1.91m")

# myself.describe_self()
# myself.greet_user()

# print("")
###################################################
# print("Exercise 9.4")

# class Restaurant:
#     def __init__(self, name, cuisine):
#         self.name=name
#         self.cuisine=cuisine
#         self.number_served=0

#     def print_number_served(self):
#         print(self.number_served)

# new_restaurant=Restaurant("Joe's", "burgers")
# new_restaurant.print_number_served()
# new_restaurant.number_served=7
# new_restaurant.print_number_served()
# print("")
############################################################
# print("Exercise 9.5")

# class User:
#     def __init__(self, first_name, last_name, age, location, height, login_attempts):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#         self.location=location
#         self.height=height
#         self.login_attempts=login_attempts

#     def increment_login_attempts(self):
#         self.login_attempts+=1

#     def reset_login_attempts(self):
#         self.login_attempts=0


# myself=User("Ulrich", "Pentz", "44", "Joburg", "1.91m", 0)
# myself.increment_login_attempts()
# myself.increment_login_attempts()
# myself.increment_login_attempts()
# print(myself.login_attempts)
# myself.reset_login_attempts()
# print(myself.login_attempts)

# print("")
############################################################
# print("Exercise 9.6")

# class IceCreamStand(Restaurant):
#     def __init__(self, name, cuisine, flavour):
#         super().__init__(name, cuisine)
#         self.flavour=flavour

#     def display_flavours(self):
#         for flavour in self.flavour:
#             print(flavour)


# my_ice_cream=IceCreamStand("Corner Ice", "Ice Cream", ["choc", "strawberry", "vanilla"])
# my_ice_cream.display_flavours()

# print("")
############################################################
# print("Exercise 9.13")

# class Die:
#     def __init__(self):
#         self.sides=6

#     def roll_die(self):
#         print(randint(1, self.sides))

# my_die=Die()
# my_die.roll_die()
# my_die.roll_die()
# my_die.roll_die()
# print("")
# my_die.sides=10
# my_die.roll_die()
# my_die.roll_die()
# my_die.roll_die()
# print("")
# my_die.sides=20
# my_die.roll_die()
# my_die.roll_die()
# my_die.roll_die()

# print("")
############################################################
# print("Exercise 9.14")    

# lottery_elements=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"a", "b", "c", "d", "e"]

# element1=choice(lottery_elements)
# element2=choice(lottery_elements)
# element3=choice(lottery_elements)
# element4=choice(lottery_elements)
# element5=choice(lottery_elements)

# print(f"{element1} {element2} {element3} {element4} {element5}")

# print("")
############################################################
# print("Exercise 9.14")    

# lottery_elements=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"a", "b", "c", "d", "e"]

# element1=choice(lottery_elements)
# element2=choice(lottery_elements)
# element3=choice(lottery_elements)
# element4=choice(lottery_elements)
# element5=choice(lottery_elements)

# winning_ticket=f"{element1}{element2}{element3}{element4}{element5}"

# print(winning_ticket)

# print("")
############################################################
print("Exercise 9.14")    
winner="c789d"
lottery_elements=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"a", "b", "c", "d", "e"]
winning_ticket=""
counter=0
def get_winner():
    element1=choice(lottery_elements)
    element2=choice(lottery_elements)
    element3=choice(lottery_elements)
    element4=choice(lottery_elements)
    element5=choice(lottery_elements)

    winning_ticket=f"{element1}{element2}{element3}{element4}{element5}"
    return winning_ticket

while winner!=winning_ticket:
    winning_ticket=get_winner()
    print(f"winning_ticket: {winning_ticket}")
    counter+=1
    print(f"roll: {counter}")