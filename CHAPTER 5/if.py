print("Exercise 5.1")
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("")
#####################################
print("Exercise 5.2")
bike="BMW"
print(bike=="BMW")
print(bike=="Honda")
print(bike.lower()=="bmw")

number_1=50
number_2=10
print(number_1==number_2)
print(number_1!=number_2)
print(number_1>number_2)
print(number_1<number_2)
print(number_1>=number_2)
print(number_1<=number_2)

print(number_1==number_2 and number_1<100)
print(number_1==number_2 or number_1<100)

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print("")
print('pepperoni' not in requested_toppings)
print("")
#####################################
print("Exercise 5.3")
alien_colour="red"
if alien_colour=="green":
    print("You scored 5 points")

if alien_colour=="red":
    print("passed")

if alien_colour!="red":
    print("")
print("")
#####################################
print("Exercise 5.4")
alien_colour="red"
if alien_colour=="green":
    print("You scored 5 points")
else:
    print("You scored 10 points")

alien_colour="green"
if alien_colour=="green":
    print("You scored 5 points")
else:
    print("You scored 10 points")
print("")
#####################################
print("Exercise 5.5")
alien_colour="green"
if alien_colour=="green":
    print("You scored 5 points")
elif(alien_colour=="yellow"):
   print("You scored 10 points") 
elif(alien_colour=="red"):
   print("You scored 15 points") 
print("")
#####################################
print("Exercise 5.6")
age=16

if age<2:
    print("Baby")
elif age>=2 and age<4:
    print("toddler")
elif age>=4 and age<13:
    print("kid") 
elif age>=13 and age<20:
    print("teenager") 
elif age>=20 and age<65:
    print("adult")
elif age>65:
    print("elder")
print("")
#####################################
print("Exercise 5.7")
fruits=["apple", "kiwi", "banana", "mango", "avo"]
if "apple" in fruits:
    print("you like apple")
if "kiwi" in fruits:
    print("you like kiwi")
if "banana" in fruits:
    print("you like banana")
if "mango" in fruits:
    print("you like mango")
if "avo" in fruits:
    print("you like avo")
print("")
####################################
print("Exercise 5.8,9")
users=["Admin", "Tom", "Frank", "Joe", "Hank"]
if len(users)!=0:
    for user in users:
        if user=="admin".lower:
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again")
else:
    print("List is empty")
print("")
#####################################
print("Exercise 5.10")
users=["Admin", "Tom", "Frank", "Joe", "Hank"]
new_users=["Sue", "Tom", "Joe", "Harry", "Mike"]

for user in users:
    for new_user in new_users:
        if user in new_users and new_user in users:
            print(f"{user} this user name has been used")
            continue
        elif user not in new_users and new_user not in users:
            print(f"{user} user name is available")
            continue
print("")
#####################################
print("Exercise 5.11")
numbers=list(range(1,10))
for number in numbers:
    if number==1:
        print(f"{number}st")
    elif number==2:
        print(f"{number}nd")
    elif number==3:
        print(f"{number}rd")
    else:
        print(f"{number}th")