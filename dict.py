product = {"laptop":"Mackbook","mobile":"Iphone","watch":"apple"}
divider = "-" * 30
print(product["laptop"])
print(product["mobile"])
print(product["watch"])
print(divider)

price_details = {"laptop":"2700","mobile":"1200","watch":"700"}
print(price_details["laptop"])
print(price_details["mobile"])
print(price_details["watch"])
print(divider)

price_details = {"laptop":"2700","mobile":"1200","watch":"700"}
key_price_details = price_details.keys()
key_values = price_details.values()
print(key_values)
print(key_price_details)
print(divider)

empty_dict = {}
empty_values = empty_dict.values()
print(empty_values)
print(divider)

price_details = {
    "laptop":"2700",
    "mobile":"1200",
    "watch":"700"
    }
product_items = price_details.items()
print(product_items)
print(divider)

#modifying dicts
price_details = {
    "laptop":"2700",
    "mobile":"1200",
    "watch":"700"
    }
price_details.update({"earpods":"799","headphones":"400"})
del price_details["mobile"]
print(price_details)
print(divider)

# Nested Dictionaries  #error displayed
student_info = {
    "name" : "rishi",
    "details" : {
        "age" : 28,
        "module" : "python"
        },
    "adress": "india"
}
print(student_info)
print(divider)

classroom = {
    "class_name" : "Drawing",
    "students" : {
        "class1":{"rahul","venky"},
        "class2":{"rohit","rishi"}
    }
}
print(classroom)

#Methods
#getting information of particular key
school = {
    "name": "Greenwood High",
    "location": "New York",
    "classes": {
        "class1": {
            "teacher": "Mr. Smith",
            "students": ["Anna", "Ben", "Clara"]
        },
        "class2": {
            "teacher": "Ms. Lee",
            "students": ["David", "Eva", "Frank"]
        }
    }
}
School_class1 = school.get("classes").get("class1").get("students")
print(School_class1)
print(divider)

#getting all the keys in the dict
student_info = {
    "name" : "rishi",
    "details" : {
        "age" : 28,
        "module" : "python"
        },
    "adress": "india"
}
student_update = student_info.get("details").get("module")
print(student_update)
print(divider)
student_keys = student_info.keys()
print(student_keys)
print(divider)

locations = {"Germany":"Berlin","India":"Delhi","Singapore":"Malaysia"}
keys_of_loactions = locations.keys()
values_of_location = locations.values()
print(keys_of_loactions)
print(values_of_location)
print(divider)

# getting all the items in the dict
list_of_items = {"choclates":"cadbury","biscuits":"britania"}
fruits = {"apple":10,"banana":6,"grapes":10}
total_items =list_of_items.items()
list_of_items.update(fruits)
print(total_items) 
print(list_of_items)
print(divider)

#removing 
list_of_items = {"choclates":"cadbury","biscuits":"britania"}
updated_list = list_of_items.pop("biscuits")
print(updated_list)
print(divider)

#clearing all items
list_of_items = {"choclates":"cadbury","biscuits":"britania"}
list_of_items.clear()
print(list_of_items)
print(divider)















