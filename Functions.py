# NOTE : Python code run in a sequenctial manner, so always invoke the function after declaration

# Using "def" keyword we declare a function
def manipulate(myData):
    i = 0;
    while i < len(myData):
        print(myData[i]);
        i += 1;

manipulate("I love math");