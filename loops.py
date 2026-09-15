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

