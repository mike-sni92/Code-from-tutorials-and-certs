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


def welcome_msg(first_name, last_name):
  print("Welcome,", first_name, last_name)

welcome_msg("test", "name")

#test name = arguements // welcome_msg = function // first_name, last_name = parameters
# A return statement is a Python statement that executes inside a function and sends information back to the function call.

#RETURNs
def calculate_fails(total_attempts, failed_attempts):
  fail_percentage = failed_attempts / total_attempts
  return fail_percentage

calculate_fails(4, 2)
#output = .5
    #When we run this, the function returns the percentage of failed attempts. It’s .5, or 50 percent, but in some Python environments, this might not be printed to the screen.We cannot use the specific variable named fail_percentage outside of the function. So, in order to use this information in another part of the program, we would need to return the value from the function and assign it to a new variable.
# You would want the output to display something else.
def calculate_fails(total_attempts, failed_attempts):
  fail_percentage = failed_attempts / total_attempts
  return fail_percentage

percentage = calculate_fails(4, 2)

if percentage <= 0.5:
  print("Act Lok")
  #output = "Act Lok"


def remaining_login_attempts(maximum_attempts, total_attempts):
    return maximum_attempts - total_attempts
remaining_attempts = remaining_login_attempts(3, 2)
if remaining_attempts <= 0:
    print("Your account is locked")
else:
 print("system updated")
#output = systemp updated





name = ["El Lar", "Ken Lma", "Cam ros"]
for i in name:
  print("Welcome,", i)

username = "elarson"
print("1:" + username)
def greet():
    username = "bmoreno"
    print("2:" + username)
greet()
print("3:" + username)


#both outputs arguments per line. Quite annoying, would love to learn how to increment the numbers to the left automatically per new entry, not there yet.

#BUILT IN FUNCTIONS
a = 1
b = 2
c = 99
print(max(a,b,c))

time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))
print(time_list)
#What if you wanted to change the variable to the sorted numbers.


#WEEK 3 Gsec cert, to test on env to refresh

new_string = str(123)
old_string = str(456)
print(type(new_string))
print(len(new_string))
print(new_string + old_string)

old = "new"
new = "old"
print (new + old)
old[0:2] #indices
#search in string
print("HELLOOOOO".index("O"))
my_string = "HELNO"
my_string[1] = "A" # strings are immutable





#WEEK 7 PYTHON


with open("login_attempts", "r") as file:
  file_text = file.read()
print(file_text)

#output = login_attempts content as string

print(file_text.split())

#output = login_attempts content as list with each space as own string

approved_users = "elarson,bmoreno,tshah,sgilmore,eraab"
print("before .split():", approved_users)
approved_users = approved_users.split(",") #now displayed as --- after .split(): ['elarson', 'bmoreno', 'tshah', 'sgilmore', 'eraab']
print("after .split():", approved_users)

#list to string is done by .join
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
print("before .join():", approved_users)
approved_users = ",".join(approved_users)
print("after .join():", approved_users)

#The keyword with handles errors and manages external resources. 
#When using with, Python knows to automatically release resources that would 
#otherwise keep our system busy until the program finishes running. 
#It's often used in file handling to automatically close a file after reading it.
#To open files and then read them, we write a statement that begins with the keyword with.
#Then, we use the open() function.

# .read() converts files into strings

"access_log.txt"
line = "jrafael, 192.168.1.1, 4:51:27, True"
with open("access_log.txt", "a") as file:
  file.write(line)

# "a" append to file // "w" write to file


#algo to count how many usernames is entered

with open("login_attempts.txt", "r") as file:
  file_text = file.read()
usernames = file_text.split()
print(usernames)

def login_chk(login_list, current_user):
  counter = 0
  for i in login_list:
    if i == current_user:
      counter = counter + 1
  if counter >= 3:
    return "login attemps exceeded."
  else:
    return "You can login now."

login_check(username, "#ENTER NAME TO CHECK HERE#")


#DEBUGGING notes

new_users = ["sgilmore", "bmoreno", "anotherentry"]
approved_users = ["bmoreno", "tshah", "elarson"]
def add_users():
    for user in new_users:
        print("line 5 - inside for loop")
        if user in approved_users:
            print("line 7 - inside if statement")
            print(user,"already in list")
        print("line 9 - before .append method")
        approved_users.append(user)
add_users()
print(approved_users)

#The print statement "line 5 - inside for loop" outputs twice, indicating that Python has entered the for loop for each username in new_users. This is as expected. 
#Additionally, the print statement "line 7 - inside if statement" only outputs once, and this is also as expected because only one of these usernames was already in approved_users.

#However, the print statement "line 9 - before .append method" outputs twice. This means the code calls the .append() method for both usernames even though one is already in approved_users. 
#This helps isolate the logic error to this area. This can help you realize that the line of code approved_users.append(user) should be the body of an else statement so that it only executes when
#user is not in approved_users.

#algo to count how many usernames is entered

with open("login_attempts.txt", "r") as file:
  file_text = file.read()
usernames = file_text.split()
print(usernames)

def login_chk(login_list, current_user):
  counter = 0
  for i in login_list:
    if i == current_user:
      counter = counter + 1
  if counter >= 3:
    return "login attemps exceeded."
  else:
    return "You can login now."

login_check(username, "#ENTER NAME TO CHECK HERE#")


