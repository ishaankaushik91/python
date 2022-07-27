firstTuple = () # Empty

myTuple = (1, 2, 3, 4);
print(myTuple[0]); # Gives 1st element there in tuple

# Major difference in list & tuple is that tuple is immutable

myTuple[1] = myTuple[1] + 1; # Throws error

# NOTE : If you wanna make a tuple with only 1 element in it make sure to put a comma ","
oneTuple = (1, );