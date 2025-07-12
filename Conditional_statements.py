# if statement
number = 100
if number == 100:
    print("the number is 100")
divider = "-" * 40
print(divider)

a = 50
if 30<a>=20:
    print("a is number")
else:
    print("a is not value")
print(divider)

number = 110
if number >= 100:
    print("number is greater than 100")
print(divider)

#if_else statement
text = "I love cricket"
if "love" in text:
    print("The text has a word love")
else:
    print("the test is not valid ")
print(divider)

#eligible to vote
age = 18
if age >= 18:
    print("ELIGIBLE FOR VOTE")
else:
    print("Not eligible for voting")
print(divider)

#temparature 

temparature = 40
if temparature >=30:
    print("Temparature is hot")
else:
    print("Temaparature is cold")
print(divider)

#if_elif_else statement
age = 16
if age < 12:
    print("child ticket is : $12")
elif age <18:
    print("Teen ticket: $15")
elif age < 65:
    print("Adult ticket: $25")
else:
    print("senior ticket:$22")
print(divider)

# checking the score
score = 65
if score < 40:
    print("need to work in nets")
elif score <100:
    print("You scored Half century")
else:
    print("Very well played")
print(divider)

#checking the number is positive or negative

number = float(input("Enter a number"))

if number > 0:
    print("The number is positive")
elif number <0:
    print("The number is negative")
else :
    print("the number is Zero")
print(divider)

# nested if statements
#checking scholorship eligibilty
marks = 74
games = True

if marks >= 85:
    if games :
        print("Eligible for scholorships")
    else:
        print("Not eligible for scholorships")
else:
    print("not elgible for scholorships because of low marks")
print(divider)

# checking discount

age = 32
is_member = False
if age >= 30:
    if is_member:
        print("Eligible for discount")
    else:
        print("Not eligible for dicount")
else:
    print("No discount")
print("divider")

#Comparision operators 

a = 20
b = 15
if a==b:
    print("a is equal to b")
else:
    print("a is not equal to b")
print(divider)

x = 15
y = 40
if x!=y:
    print("x not equal to y")
else:
    print("x is equal to y")
print(divider)

eggs = 2
milk = 1
if eggs > milk:
    print("Eggs are costlier than milk")
else:
    print("Milk is cheaper than eggs")
print(divider)

temparature = 12
is_snowy = True
if temparature <= 12 and is_snowy:
    print("Carry umbrella and wear thermals")
else:
    print("It's ideal to go outside")
print(divider) 

 # using is and in keywords

a = [1,2,3]
b = a

if a is b :
    print("a and b refers to the same object.")
else:
    print("a and b is not same object.")
print(divider)

name1 = "RISHI"
name2 = "RISHI"
if name1 is name2:
    print("name1 and name2 have same object memeory")
else:
    print("They have different memory")
print(divider)

#using in
team = ["jaiswal","gill","pant","rohit"]
if "rohit" in team:
    print("rohit is the captain")
else:
    print("gill is the captian")
print(divider)

fruits = ['apple', 'banana', 'orange']

if 'banana' in fruits:
    print("Yes, banana is in the list!")
else:
    print("No, banana is not in the list.")
print(divider)

#using is not and notin

a = [1, 2, 3]
b = [1, 2, 3]

if a is not b:
    print("a and b are not the same object.")
print(divider)


person = {'name': 'Robo', 'age': 30}

if 'address' not in person:
    print("Address key is not in the dictionary.")
else:
    print("Address key is present in the dictionary.")
print(divider)

attendance_list = ['Rahul', 'Robin', 'Varnu']

if 'David' not in attendance_list:
    print("David is absent today.")
print(divider)


















