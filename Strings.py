from torch import true_divide


print("Hello World");

print("Hello \n World"); # \n --> To leave a line
print("Hello \t World"); # \t --> To give tab space

print('Hello World my \name is python'); # --> \n here is leaving line
print(r"Hello World my \name is python"); # --> r --> Putting "r" before quotes will help to solve above problem

print('Hello "World"'); # "World" in Quotes

print("Hello" + " World") # String concatination

word = "Hello World";
print(word[0]); # Gives you H
print(word[-1]); # Gives you last character

# Note how the start is always included, and the end always excluded
print(word[:2]); # Gives you characters starting from 0 till 2 (2 IS EXCLUDED)
print(word[2:5]); # Gives you characters starting from 2 (2 IS INCLUDED) till 5 (5 IS EXCLUDED)
print(word[:2] + word[1:5]); # Joins characters from 0 - 2 with 1 to 5

# String Functions & Methods
people = "people like Linus, Dennis, Van, etc. are real life superheroes";
print(len(people)); # Gives length of Sring
print(people.endswith("superheroes")); # Gives True/False
print(people.endswith("snake"));
print(people.capitalize()); # Make 1st character uppercase
print(people.casefold()) # Makes whole string lowercase

people[0] = 1;
print(people); # Strings are immutable

# More Methods --> https://www.w3schools.com/python/python_ref_string.asp