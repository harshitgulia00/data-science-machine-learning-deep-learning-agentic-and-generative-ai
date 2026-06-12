# dictionary
# key-value pair
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict)
print(my_dict["name"])
# add new key-value pair
my_dict["email"] = "alice@example.com"
print(my_dict)
# update existing key-value pair
my_dict["age"] = 31
print(my_dict)
# delete key-value pair
del my_dict["city"]
print(my_dict)
# iterate through dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
# check if key exists
if "name" in my_dict:
    print("Name exists in the dictionary")
# get value with default
print(my_dict.get("city", "City not found"))
# dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)