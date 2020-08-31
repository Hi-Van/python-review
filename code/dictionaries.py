#declaring a dictionary
dict = {
    "key": "value",
    "key2": "value2",
}

#referencing keys in a dictionary
ref = {
    "key": "value",
    "three": 3,
    "true": True, 
}

print(ref["key"])
print(ref.get("key"))

#specify a default value for invalid key references
spec = {
    "key": "value",
    "three": 3,
    "true": True, 
}

print(spec.get("key here", "default message here"))