print("Exercise 7.1")

wanted_car=input("What type of car would you like?\t")
print(f"Let me see if we can find you a {wanted_car}")
print("")
#####################################################
print("Exercise 7.2")

number_of_guests=int(input("How many seats do you need?\t"))
if number_of_guests>8:
    print("wait")
elif number_of_guests<=8:
    print("Be seated")

print("")
####################################################
print("Exercise 7.3")

number_input=int(input("Enter a number\t"))
if number_input%10==0:
    print("multiple of 10")
else:
    print("not multiple of 10")

print("")
####################################################
print("Exercise 7.4")

pizza_topping=input("enter pizza topping \nenter quit to exit\t")

while pizza_topping!="quit":
    pizza_topping=input("enter pizza topping \nenter quit to exit\t")

print("")
####################################################
print("Exercise 7.5")

age=int(input("How old are you?\t"))

while age>0:
    if age<3:
        print("free")
        break
    elif 3<=age<=12:
        print("$10")
        break
    elif(age>12):
        print("$15") 
        break

print("")
####################################################
print("Exercise 7.6")

age=int((input("How old are you?\t")))
active=True
while active:
    if 0<age<100:
        print(age)
        age=int((input("How old are you?\t")))
    elif age>100:
        break
    elif age==0:
        active=False

print("")
####################################################
print("Exercise 7.8")

sandwiches=["cheese", "ham", "salami"]
finished_sandwiches=[]

for sandwich in sandwiches:
    print(f"I made you a {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

for sandwich1 in finished_sandwiches:
    print(f"{sandwich1} was made.")

print("")
####################################################
print("Exercise 7.9")

sandwiches=["cheese", "ham", "salami", "pastrami", "pastrami", "pastrami"]

print("Pastrami finished")

while "pastrami" in sandwiches:
    sandwiches.remove("pastrami")

print(sandwiches)   

print("")
#####################################################
print("Exercise 7.10")

prompt = "If you could visit one place in the world, where would you go?"

dream_vacation=input(prompt)

print(dream_vacation)