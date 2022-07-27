# List is a data type in python almost same like an array
from torch import le


myList = [1, 2, "10", "90"];
anotherList = [21, 100];

print(myList);
print(myList[0]); # Output --> 1
print(myList[:3]) # Output --> All elements excluding 3rd one
print(myList + anotherList); # Concatenation of 2 lists

myList[0] = "Pi"; # Changes the value at 1st index
print(myList);

# List Methods
myList.append(100); # Adds 100 at the end of list
print(myList);

copy = myList.copy(); # Returns copy 

myList.clear() # Removes all elements from the list
print(myList);

# More Methods --> https://www.w3schools.com/python/python_ref_list.asp