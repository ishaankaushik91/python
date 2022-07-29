# Dictionary is just like a book, we have a key which has got some information as value
# therefore it's a key - value pair
a = {
    "a" : [1, 2, 3, 10, 89],
    "computers" : "Gift to humanity",
    "b" : (21, 11, "sheeesh"),
    "c" : {
        "apple" : "fruit",
        "algorithms" : "Life"
    }
};

# To access dictionary elements
print(a["a"]);
print(a["a"][0]);
print(a["b"][0]);
print(a["c"]["apple"]);

# These are mutable, unordered
a["a"][0] = "Elon";
print(a["a"][0]);

# Dictionary methods
everything = a.items(); # This will return a tuple
print(everything, type(everything));

keys = a.keys(); # Returns a list, class of type "dict_items" with all key in it (WE CAN TYPE CAST)
print(keys, type(keys));
keys = list(keys);
print(type(keys));

keys = a.values(); # Returns a list, class of type "dict_items" with all values in it (WE CAN TYPE CAST)
print(keys, type(keys));
keys = list(keys);
print(type(keys));

# More dictionary methods --> https://www.w3schools.com/python/python_ref_dictionary.asp