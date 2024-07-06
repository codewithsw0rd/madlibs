# String concatenation is the method of combining strings
# few ways to do this
# yt = "goodman"

# print("Subscribe:- " + yt )
# print("subscribe to  {}".format(yt))
# print(f"subscribe to {yt}")

# For this purpose we are going to use fstring

print("Enter the following details about yourself:-\n")

name = input("Name:- ")
age = input("Age:- ")
gender = input("Gender:- ")
character = input("Character:- ")
hobby = input("Hobby:- ")
sport = input("Sport:- ")
superhero = input("Superhero:- ")

madlibs = f"\n My name is {name}. I am {age} years old {gender}. I am {character} person \
when I am with the right people. My hobby is {hobby}. My favourite sport is {sport}.\
and my favourite superhero is {superhero}. Thats it!"

print(madlibs)
