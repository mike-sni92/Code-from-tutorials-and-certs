#Variables are dynamically typed.
n = 0
print('n =', n)

n = "abc"
print('n =', n)

  #type is determined at run time
  #n when printed out goes from 0 and changes to "abc


##multiple assignments
##none is null
###if statements don't need parentheses or curly braces
  ##indentation is used
##Parentheses needed  for multi-line condition.

#NETWORKCHUCK

#Google Cyber Sec Python notes, tuple data types are unchangeable, run test code at later time, tried print(tuple variable + string) == invalid response by python.

OS = "OS_4"
if OS == "OS_2":
 print("system update needed")
elif OS == "OS_1":
 print("system update badly needed")
else:
 print("system updated")


computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    print(asset)
  
computer_assets = ["laptop1", "desktop20", "smartphone03"]
print(computer_assets)
  
#output computer_assests = ["laptop1", "desktop20", "smartphone03"] 
# output asset = 
#laptop1
#desktop20
#smartphone03

string = "security"
for character in string:
    print(character)
#works on strings too, output each letter per line.

#RANGE for loops
for i in range(0, 5, 1):
    print(i)
    #output = 0 as starting point, 5 as end point, 1 as increment /// ""but if the start point is the default value of 0 and the increment is the default value of 1""


#As long as the condition is True, the loop continues, but when it evaluates to False, the while loop exits. The following while loop continues as long as the condition that i < 5 is True:
i = 1
while i < 5:
    print(i)
    i = i + 1

#integers in loop condition
login_attempts = 0
while login_attempts < 5:
    print("Login attempts:", login_attempts)
    login_attempts = login_attempts + 1

#Booleans in loop condition
count = 0
login_status = True
while login_status == True:
    print("Try again.")
    count = count + 1
    if count == 4:
        login_status = False

#BREAKS
computer_assets = ["laptop1", "desktop22", "smartphone03", "desktop0", "desktop20"]
for asset in computer_assets:
    if asset == "desktop20":
        break
    print(computer_assets)
    #output = entire computer_assets string displayed until it reaches "desktop20"

#continue
computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        continue
    print(asset)
    #output, asset will not include desktop20

#EXERCISE----You want to welcome 3 users from a list by their name (for example, “Welcome, Emerick Larson”).

name = ["El Lar", "Ken Lma", "Cam ros"]
for i in name:
  print("Welcome,", i)
  #output Welcome, El Lar and so on.

name = ["El Lar", "Ken Lma", "Cam ros"]
for i in name:
  print("Welcome,", name)
  #output = ["El Lar", "Ken Lma", "Cam ros"] 3X

name = ["El Lar", "Ken Lma", "Cam ros"]
for i in range(3):
  print("Welcome,", i)
  #output = Welcome, 0 Welcome, 1 Welcome, 2

