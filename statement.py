"""set condition if the condition execute an action, 
if not condition execute a different action"""

# if statement, match statement
"""if condition:
    execute an action if True

else:
    execute an action if False

if condition:
    execute an action if True
elif condition:
    execute an action if True
else:
    execute an action if False

if condition:
    if another condition:
        execute action if another condition is True
    else:
        execute action if another condition is false
else:
    execute action if condition is False"""

# me = 200
# me = int(input("Enter only number here: "))
# if me > 300:
#     if me > 900:
#         print(f'{me} is way greater than 300')
#     else:
#         print(f'{me} is greater than 300')
# elif me == 300:
#     print(f'{me} is equal to 300')
# else:
#     print(f'{me} is less than 300')

# Inline statement/condition
# a = f"{me} greater than 300" if me>300 else (f"{me} equal to 300" if me==300 else f"{me} less than 300")
# print(a)

'''variable, a,raghad = True,30, "Hi"

print(f"The Value of variable is :{variable}")
print(f"The Value of a is : {a}")
print(f"The Value of raghad is :{raghad}")'''

# Delimiter =seperator

"""liu = 'Hello How are you doing today'
print(liu[8])
print(liu.split(" "))
"""
# email = "raghadalkurdi94@gmail.com"
# _email = "raghadalkurdi94@gmail.com"
# email1 = "chikoliu@phase3telecom.com"
# email2 = "yuecae@innovision-bd.com"

# print(email1.split("@"))
'''test,domain = email.split("@")

print(f"this is name: {test}")
print(f"this is domain: {domain}")'''

'''if email1.split("@")[1] == "gmail.com":
    print("This is a personal email")
else:
    print("This is an organizational email")
'''
# variable_that = "name,organization,contact"
# print(variable_that.split(","))

email_test = str(input("Enter your email here: "))
# | / or anyone can be true
# & / and both must be true

if (email_test.split("@")[1] == "gmail.com") | (email_test.split("@")[1] == "hotmail.com"):
    print("This is a personal email account")
else:
    print("This is a company email account")