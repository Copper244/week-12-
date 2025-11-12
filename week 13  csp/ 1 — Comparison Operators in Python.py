# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a) #3
print(b) #4
print (a == b) #output false

print(a == b)   #checks for equality # False
print(a != b)   #checks if is not equal # True
print(a > b)    #checks for greater than # False
print(a < b)    # checks for less than # True
print(a >= b)   # checks for greater than or equal to #False
print(a <= b)   # checks for less than or equal to #True


#predict the output of the following comparisons:
10 > 5 #output True
7 == 2 * 3 + 1 #output True
8 != 8 #output False
4 <= 2 + 2 #output True

# Write 3 examples that result in True and 3 that result in False.
3 > 1      # True  
5 == 5     # True  
2 != 3     # True  

4 < 2      # False  
6 == 7     # False  
9 <= 5     # False  

# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"

score = int(input("what is your score?"))
#make this program for all grading spectrums
# if the score is between 90-100 -- you got an A
# if the score is between 80-89 -- you got an B
# if the score is between 70-79 -- you got an C

if score >= 90:
    print("You got an A")
elif score >= 80:
    print("You got a B")
elif score >= 70:
    print("You got a C")
elif score >= 60:
    print("You got a D")
else:
    print("You got an F")

if score >= 60:
    print("you passed the test")
else:
    print("you didnt pass")



#ask for a password
#password = input("what is your passwords")

password = input("what is your password")
if len(password) >= 8 and any(char.isdigit() for char in password):
  print("Password is valid.")
else:
  print("Password is invalid. " \
  "It must
