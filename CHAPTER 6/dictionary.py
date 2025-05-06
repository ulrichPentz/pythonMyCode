print("Exercise 6.1")
person={
    "first_name":"Ulrich",
    "last_name":"Pentz",
    "age":"44",
    "city":"Roodepoort"
}

for key, value in person.items():
    print(f"Key: {key}, Value: {value}")
print("")
# ########################################
print("Exercise 6.2")
favourite_numbers={
    "John":"1",
    "Joe":"2",
    "Jack":"3"
}
for key, value in favourite_numbers.items():
    print(f"Key: {key}, Value: {value}")
print("")
# ########################################
print("Exercise 6.3")
words={
    "def":"start of function",
    "for":"start of for loop",
    "while":"start of while loop"
}
for key, value in words.items():
    print(f"Word: {key} - Definition: {value}")
print("")
# ########################################
print("Exercise 6.6")
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 'john':'',
 'jack':'',
 'joe':''
 }

for key, value in favorite_languages.items():
    if value=='':
        print(f"{key}, please take our poll")
    else:
        print(f"{key} thank you for taking our poll")    
print("")
########################################
print("Exercise 6.7")
person1={
    "first_name":"Ulrich",
    "last_name":"Pentz",
    "age":"44",
    "city":"Roodepoort"
}

person2={
    "first_name":"John",
    "last_name":"Doe",
    "age":"56",
    "city":"NY"
}

person3={
    "first_name":"Anne",
    "last_name":"Smith",
    "age":"21",
    "city":"Moscow"
}

people=[person1, person2, person3]
for pers in people:
        for key, value in pers.items():
            print(f"{key}:{value}")
            
print("")
########################################
print("Exercise 6.9")
favorite_places={
      "john":["NY", "Paris", "Joburg"],
      "joe":["NY", "Paris", "Joburg"],
      "jane":["NY", "Paris", "Joburg"],
}

for key, value in favorite_places.items():
      print(f"{key} likes:")
      for place in value:
            print(place)
print("")
########################################
print("Exercise 6.11")
cities={
      "NY":{
            "country":"USA",
            "population":"2",
            "fact":"far"
      },
      "Paris":{
            "country":"France",
            "population":"7",
            "fact":"stinks"
      },
      "Moscow":{
            "country":"Russia",
            "population":"10",
            "fact":"cold"
      }
}

for key, value in cities.items():
      print(f"{key}")
      for key1, value1 in value.items():
            print(f"{key1}:{value1}")
