# while and for
# a = 0
# while a < 6:
#     print(a)
#     a = a+1

# while True:
#     email_test = str(input("Enter your email here: "))
#     if "@" in email_test and (email_test.split("@")[1] == "gmail.com" or email_test.split("@")[1] == "hotmail.com"):
#         print("This is a personal email account")
#         break
#     elif "@" in email_test:
#         print("This is a company email account")
#         break

a = ["cars", "buses", "airplane", "Helicopter"]
b = {"name": "Raghad Alkurdi", "age": 50, "country": "Syria"}
email = [
    "raghadalkurdi94@gmail.com",
    "liuyuenfu@gmail.com",
    "Chiko Liu",
    "NSah AgneS",
]
# for key in b.keys():
#     print(key)

# for value in b.values():
#     print(value)

# for mail in email:
#     if "@" in mail:
#         print(mail)

# for mail in email:
#     if "s" in mail.lower():
#         print(mail.title())
for mail in email:
    if "u" in mail.lower():
        if "@" in mail:
            print(mail.lower())
        else:
            print(mail.title())


# list comprehension, function, class, inheritance

# while and for loops

# while condition:
#     execute if condition is yet to be fulfilled

#     Break

# ridwan = 0

# while ridwan < 10:
#     print(ridwan)
#     ridwan = ridwan +1

# Delimiter = seperator
# birhane="Hello Birhane welcome to python programming"
# print(birhane[5:])
# print(birhane.split(" "))
# print(birhane.split(" ")[-1])

# email = "liuyuenfu.gmail.com"
# username,domain,_ = email.split(".")

# print(f'user: {username}')
# print(f"domain: {domain}")
# print(f"domain type: {_}")
# 
# email = "liuyuenfu@gmail.com"

# email = input("Enter your email address here: ")

# while True:
#         email = input("Enter your email address here: ")
#         if "@" in email and (email.split("@")[1] == "gmail.com" or email.split("@")[1] == "hotmail.com"):
#             print(f"{email} is a personal email account")
#             break
#         elif "@" in email: 
#             print(f"{email} is a company email account")
#             break
#         print("you must enter an email address")

# kessie = [1,2.2,"3",False,5,6,7,8,[0]]
# for loop in kessie:
#     print(f'data type for {loop}: {type(loop)}')

numbers = [1,2,3,4,5,6,7,8,9,10]
odd_number=[]
even_number=[]
# odd number are number/2 give a remainder
# even number are number/2 doesn't give a remainder
# for number in numbers:
#     if number % 2 ==0:
#         even_number.append(number)
#     elif number %2 !=0:
#         odd_number.append(number)
# enter_range = int(input("Enter a number range: "))
# for number in range(1,enter_range+1,1):
#     if number % 2 ==0:
#         even_number.append(number)
#     elif number %2 !=0:
#         odd_number.append(number)

# print(f"Odd number are {odd_number}")
# print(f"Even number are {even_number}")

email = [
    "raghadalkurdi94@gmail.com",
    "liuyuenfu@gmail.com",
    "Chiko Liu",
    "Stephanie Simon",
]

for check in email:
    # if "@" in check:
    if "s" in check.lower():
        print(check.title())

# function class inheritance
