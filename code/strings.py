#rendering literal characters
print("this is a \"quote\" ")

#printing a variable
variable = "text"
print(variable)

#concatenation
statement = "string"
print("this is a " + statement)

#lowercase function
lowercase_text = "THIS IS LOWERCASE"
print(lowercase_text.lower())

#uppercase function
uppercase_text = "this is uppercase"
print(uppercase_text.upper())

#check string is uppercase or lowercase
check = "is this uppercase"
print(check.isupper())

print(check.islower())

#nesting functions, the code below is equivalent
item = "this is a item"
item_upper = item.upper()
print(item_upper.isupper())

print(item.upper().isupper())

#string length
length = "what is this string length"
print(len(length))

#indexing the first character
string_index = "index this string"
print(string_index[0])

#return the first index of a character
index_string = "index this string"
print(index_string.index("d"))

#replace characters within a string
replace_string = "replace this"
print(replace_string.replace("this", "that"))

#strings to decimal value
print(float("5"))

#strings to integer value
print(int("5"))