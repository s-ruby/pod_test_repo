# Welcome to Gary Browns survey

# start of the age input
age = int(input("What is your age?"))
if age <= 21:
    print(f"{age} is to young to drink")
else:
    print("It's time to drink! --drink responsibly")

# start of the name input
name = input("what is you first and last?")
if name == "":
    print("no name , no problem")
else:
    print(f"{name} is a great name")

 # start of the gender input
gender = input(
    "What is your gender? Type 'f' for female, 'm' for male, 'n' for non-binary, 't' for Transgender.")
if gender == "f":
    gender = "female"
    print("You go girl!")
elif gender == "m":
    gender = "male"
    print("man you better get you a uber driver!")
elif gender == "n":
    gender = "non-binary"
    print("drive safe!")
elif gender == "t":
    gender = "transgender"
    print("party time!")
else:
    gender = "Im a alien"
    print("You must be an alien.")

 # start of the language input
languages = input(
    "What language do you understand? Type 'eng' for english, 'span' for spanish.")
if languages == "eng":
    print("english is the language to know")
if languages == "span":
    print("gran idioma para saber! Hola")
else:
    print("We need an interpreter!")

# start of the city input
state = input("What state do you live in? Type 'c' for cali, 'n' for new york")
if state == "c":
    state = "california"
    print(f"{state} is a big state, your age is {age} so your good to go")
elif state == "n":
    state = "newyork"
    print(f"{state} is a big state, your age is {age} so your good to go")
elif name == "":
    print("You must live in a cave!")
    state = "i live underground!"
else:
    print(f"{state} is a great place to live")


# start of the zipcode input
zip_code = int(input("Enter your zipcode"))
if zip_code == zip_code:
    print("That is super awesome")

# start of the city input
drink = input(
    "What is you favorite color alcohol drink? Type 'd' for dark liqour, 'w' for white liqour.")
if drink == "d":
    drink = "dark liqour"
    print(f"{drink} is a great choice")
elif drink == "w":
    drink = "white liqour"
    print(f"{drink} is a great choice")
else:
    print("I've never drank that type before")
    drink = "I like it all"

 # start of the how often input
how_many_drinks = int(input("how many drinks per day?"))
if not how_many_drinks >= 2:
    print("Your not a drunk  ,")
elif (2 >= how_many_drinks >= 4):
    print("slow down a little ,")
else:
    print("your a drunk")
# start of the what time?  input
what_time_drink = int(input("what time your drink in the day time?"))
if what_time_drink <= 11:
    print("Your a morning drinker")
else:
    print("your a night time drinker or afternoon drinker")
 # start of the drink with friends input
drink_with_friend = input(
    "do you drink with friends? type 'y' for yes, 'n' for no")
if drink_with_friend == "y":
    drink_with_friend = "drink with my friends"
    print("Its buddy time")
elif drink_with_friend == "n":
    drink_with_friend = "drink alone"
    print("Its me time")
else:
    print("I guess your undecided")

print(f"My name is {name} and I am {age} old, My gender is {gender}, I live in the state of {state}. I like {drink}, I like to drink {drink_with_friend}")

print("Thank your for taking my survey!")
