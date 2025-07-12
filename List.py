# lsit indexing 
numbers = [10,20,30,40]
divider = "-"*30
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(divider)

#accessign elements
cities = ["hyderabad", "bangalore", "chennai", "delhi"]
print(cities[2])
print(divider)

#mixed data types
list = [1.5, "hyderabad",2,"false"]
print(list[3])
print(list[-3])
print(divider)

list = [0.1, 1,"telugu","hindi","marathi","tamil","true"]
print(list[3])
print(list[-2])
print(list[len(list) -2]) #question arrised about positive index
print(divider) #page 12

#nested lists
#simple nexted lists

nested_lists = [
    ["jaiswal","rahul","gill"],
    ["pant","nair","nitesh"],
    ["jadeja","siraj","bumrah"]
]
print(nested_lists)
print(divider)

#mixed_lists

nested_lists = [
    ["jaiswal",39,"rahul",47,"gill",68],
    ["pant", 99,"nair", 22,"nitesh",87 ],
    ["jadeja", 4,"siraj", 5,"bumrah",7]
]
print(nested_lists)
print(divider)
print(nested_lists[1][2])
print(divider)

#nested_lists_with strings
mixed_lists = ["apple","banana",["x","y","z"],["cat","dog"]]
print(mixed_lists)
print(mixed_lists[0])
print(mixed_lists[1])
print(mixed_lists[2][0])
print(mixed_lists[2][1])
print(mixed_lists[2][2])
print(mixed_lists[3])
print(divider)

# Nested list with mixed data types
mixed_data = [
    "hello",             
    42,                  
    ["red", "blue"],     
    [100, 200, 300],     
    ["sun", [1, 2, 3]]   
]

print(mixed_data)
print(mixed_data[0])           
print(mixed_data[1])           
print(mixed_data[2][1])        
print(mixed_data[3][0])        
print(mixed_data[4][0])        
print(mixed_data[4][1])        
print(mixed_data[4][1][2]) 
print(divider)
mixed_data[2][1]="green"
print(mixed_data)
print(divider)

#concatenating lists
marks = [22,24,18]
names = ["bharat","sai","rahul"]
report = marks + names
report_updated = marks *3 + names
print(report)
print(report_updated)
print(divider)

#Methods

fruits = ["apple", "banana", "cherry", "mango"]
fruits.append("Grapes")
fruits.append("Berry")
print(fruits)
print(divider)

fruits = ["apple", "banana", "cherry", "mango"]
fruits.insert(1,"grapes")
print(fruits)
print(divider)

animals = ["pig","cat"]
animals.insert(0,"Hen")
animals.extend(["cow","Buffalo"])
animals.remove("Hen")
remove_animals = animals.pop(2)
index = animals.index("cat")
print(index)
print(animals)
print(divider)

fruits = ["apple","Cherry", "banana", "Cherry", "mango"]
fruits.insert(1,"grapes")
fruits_count=fruits.count("Cherry")
print(fruits_count)
print(fruits)
print(divider)























