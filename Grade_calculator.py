name = "kashyap"
maths_marks = 70
science_marks = 63
social_marks = 39
total_marks = maths_marks + science_marks + social_marks
average_marks = total_marks / 3
percentage = (total_marks/300)*100
print(total_marks)
print(average_marks)
print(percentage)
print(name)
#now checking if the student is pass or fail
if maths_marks >= 40 and science_marks >= 40 and social_marks >= 40 :
    print("status: Pass")
else:
    print("status: Fail")
print("Added the line to check the pull request")