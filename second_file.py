print("Commiting the second file to the remote")
print("created our new branch")
print("Writing to understand concept better on branching")
name = input("enter your name")
weight = input("enter weight")
height = input("enter your height")
BMI = float (weight) /(float(height) ** 2)
print(BMI)
if BMI < 18.5:
    print("Underweight")
elif 18.5 >= BMI <= 24.9:
    print("Healthy_weight")
else:
    print("Overweight")