# print("Exercise 8.1")

# def display_message():
#     print("Python rocks!")

# display_message()    

# print("")
#################################################
# print("Exercise 8.2")

# def favourite_book(name):
#     print(f"My favourite book is {name}")

# favourite_book("Icarus")

# print("")
#################################################
# print("Exercise 8.3")

# def make_shirt(shirt_size, print_message):
#     print(f"You ordered a {shirt_size} t-shirt")
#     print(f"The print is: {print_message}")

# # make_shirt('medium', 'Python rocks')

# make_shirt(print_message="Java rocks", shirt_size="large")

# print("")
#################################################
# print("Exercise 8.3")

# def make_shirt(print_message, shirt_size="large"):
#     print(f"You ordered a {shirt_size} t-shirt")
#     print(f"The print is: {print_message}")

# make_shirt("Python rocks")

# print("")
#################################################
# print("Exercise 8.4")

# def make_shirt(print_message="Python rocks", shirt_size="large"):
#     print(f"You ordered a {shirt_size} t-shirt")
#     print(f"The print is: {print_message}")

# make_shirt()
# make_shirt(shirt_size="medium")
# make_shirt("Java is cool", "small")

# print("")
#################################################
# print("Exercise 8.7")

# def make_album(name, title, number_of_songs=None):
#     artist={"name":name,
#             "title":title}
#     if number_of_songs:
#         artist["number"]=number_of_songs
#     return artist

# print(make_album("Metallica", "Black"))
# print(make_album("Tool", "Green"))
# print(make_album("FFDP", "White"))
# print(make_album("FFDP", "White", 4))

# print("")
#################################################
# print("Exercise 8.8")

# artist=input("Enter artist\t")
# album=input("Enter album")

# def make_album(name, title, number_of_songs=None):
#     artist={"name":name,
#             "title":title}
#     if number_of_songs:
#         artist["number"]=number_of_songs
#     return artist

# while artist!="quit" or album!="quit":
#     album1={
#         "artist":artist,
#         "album":album
#     }
#     print(make_album(artist, album))
#     artist=input("Enter artist\t")
#     album=input("Enter album")

# print("")
#################################################
# print("Exercise 8.9")

# messages=["howzit", "how are you", "enjoy your day"]

# def display_messages(list):
#     for message in list:
#         print(message)

# display_messages(messages)

# print("")
#################################################
# print("Exercise 8.10")

# messages=["howzit", "how are you", "enjoy your day"]
# sent_messages=[]

# def send_messages(list, empty_list):
#     for message in list:
#         empty_list.append(message)

# send_messages(messages, sent_messages)

# print(messages)
# print(sent_messages)       

# print("")
#################################################
# print("Exercise 8.12")

# def make_sandwich(*stuff):
#     print(stuff)

# make_sandwich("cheese", "ham")
# make_sandwich("butter", "bacon", "tomato") 
# make_sandwich("jam", "cheddar", "stuff", "more stuff")   

# print("")
#################################################
print("Exercise 8.13")

def build_car(make, model, **car_info):
    car_info["make"]=make
    car_info["model"]=model
    return car_info

car_profile=build_car("BMW", "M3", 
                      colour="yellow",
                      acc="3s")

print(car_profile)