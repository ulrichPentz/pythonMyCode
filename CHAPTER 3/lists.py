print("Exercise 3.1")
my_friends=["Tom", "Dick", "Harry"]
print(my_friends[0])
print(my_friends[1])
print(my_friends[2])
print("")
###############################
print("Exercise 3.2")
print(f"Good morning {my_friends[0]}")
print(f"Good morning {my_friends[1]}")
print(f"Good morning {my_friends[2]}")
print("")
###############################
print("Exercise 3.3")
cars=["Honda", "BMW", "Audi"]
print(f"A {cars[0]} is nice")
print(f"A {cars[1]} is cool")
print(f"A {cars[0]} is kak")
print("")
###############################
print("Exercise 3.4")
guests=["Hitler", "Ghandi", "Hussein"]
print(f"Hi {guests[0]}, would you like to come to dinner?")
print(f"Hi {guests[1]}, would you like to come to dinner?")
print(f"Hi {guests[2]}, would you like to come to dinner?")
print("")
###############################
print("Exercise 3.5")
print(f"Guest who can't make it: {guests[1]}")
del guests[1]
guests.append("Jock")
print(f"Hi {guests[0]}, would you like to come to dinner?")
print(f"Hi {guests[1]}, would you like to come to dinner?")
print(f"Hi {guests[2]}, would you like to come to dinner?")
print("")
###############################
print("Exercise 3.6")
print(f"Hi {guests[0]}, would you like to come to dinner?")
print(f"Hi {guests[1]}, would you like to come to dinner?")
print(f"Hi {guests[2]}, would you like to come to dinner?")
print(f"{guests[0]}, {guests[1]}, {guests[2]} we found a bigger table and will be inviting more people.")
guests.insert(0, "A Recce")
guests.insert(2, "A policeman")
guests.append("Thatcher")
print(f"Hi {guests[0]}, would you like to come to dinner?")
print(f"Hi {guests[1]}, would you like to come to dinner?")
print(f"Hi {guests[2]}, would you like to come to dinner?")
print(f"Hi {guests[3]}, would you like to come to dinner?")
print(f"Hi {guests[4]}, would you like to come to dinner?")
print(f"Hi {guests[5]}, would you like to come to dinner?")
print("")
###############################
print("Exercise 3.7")
print("Table's gonna be too small, can only invite two people")
two_guests=[]
two_guests=guests[0:2]
print(f"Hi {two_guests[0]}, you can still come")
print(f"Hi {two_guests[1]}, you can still come")
del two_guests[0]
del two_guests[0]
print(f"two_guests: {two_guests}")
print("")
###############################
print("Exercise 3.8")
places=["Paris", "Scotland", "New York", "Windhoek", "Moscow"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.reverse()
print(places)
print("")
###############################
print("Exercise 3.9")
print(len(guests))