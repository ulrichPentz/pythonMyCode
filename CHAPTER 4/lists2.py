print("Exercise 4.1")
pizzas=["Pineapple", "Ham", "Salami"]

for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("I really like pizza")
print("")
######################################
print("Exercise 4.2")
animals=["dog", "cat", "sheep"]

for animal in animals:
    if animal=="dog":
        print("Dogs are cool")
    elif animal=="cat":
        print("Cats suck")
    elif animal=="sheep":
        print("Lamb is good meat")

print("They are all mammals")
print("")
######################################
print("Exercise 4.3")
for number in range(0,21):
    print(number)
print("")
######################################
print("Exercise 4.4")
numbers = list(range(1, 1_000_001))
for number in numbers:
     print(number)
print("")
######################################
print("Exercise 4.5")
numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print("")
######################################
print("Exercise 4.6")
odd_numbers=list(range(1, 20, 2))
for odd_number in odd_numbers:
    print(odd_number)
print("")
######################################
print("Exercise 4.7")
threes=list(range(3, 31, 3))
for three in threes:
    print(three)
print("")
######################################
print("Exercise 4.8")  
cubes=list(range(1, 11))
for cube in cubes:
    print(cube**3)  
print("")
######################################
print("Exercise 4.9")  
cubes = [cube**3 for cube in range(1, 11)]
print(cubes)
print("")
######################################
print("Exercise 4.10") 
print(f"First 3 items: {cubes[:3]}")
print(f"Middle 3 items: {cubes[3:6]}")
print(f"Last 3 items: {cubes[7:]}")
print("")
######################################
print("Exercise 4.11")
friend_pizzas=pizzas[:]
pizzas.append("Seafood")
friend_pizzas.append("Rib")
for pizza in pizzas:
    print(f"My pizza are: {pizza}")

for friend_pizza in friend_pizzas:
    print(f"Friend pizzas: {friend_pizza}")  
print("")
######################################
print("Exercise 4.13")   
food_tuple=("steak", "burger", "pizza", "sandwich", "wrap")
for food in food_tuple:
    print(food)

food_tuple=("steak", "burger", "pizza", "samoosa", "sushi")
for food in food_tuple:
    print(food)
