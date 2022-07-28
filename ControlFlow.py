x = 10;
sum = 0;

# Conditinals
if x < 10 :
    print("x is less than 10");
elif x == 10 :
    print("x is", 10);
else :
    print("x is shit");


# Iteration (LOOPS)
while x < 100 :
    print(x);
    x += 1;

while sum < 1000 :
    sum += x;

print(sum);

# for loop here is to traverse of some iterable thing :
y = [1, 1, 2, 3, 5, 8, 13];
summation = 0;

for w in y :
    summation += w; # w here is = index of y OR
                    # w = y[0], then y[1], till the end
print(summation);

m = "Hopea";
newOne = [];
index = len(m) - 1;

while index >= 0:
    newOne.append( m[index]);
    index -= 1;

print(newOne);