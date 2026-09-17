# def function_name(): # take in a parameter(s)
#     return f"Hello from a function"

# myfunc = function_name()

# print(function_name())
# function_name()

# def function_name(): # take in a parameter(s)
#     print(f"Hello from a function")

# function_name()

# Myfunction myfunction myFunction

# usd = 1
# zwd = 29
# usd=20
# conversion_usd_zwd = zwd *usd

# print(conversion_usd_zwd,"zwd for usd")

# def conversion_from_zwd_usd(amount):

#     convert = amount/29
#     print(f"{amount} zwd to usd is : {convert:.1f} usd")
#     # return amount,"zwd to usd is : ",convert,"usd"

# conversion_from_zwd_usd(1000)
# conversion_from_zwd_usd(3000)
# conversion_from_zwd_usd(3230)

# def calculate():
#     pass

# if 100>50:
#     pass

# def display_welcome(fname,lname):
#     print(f"Hello {fname} {lname}, How is python programming today?")

# display_welcome("Raghad","Alkurdi")
# display_welcome("Yeukai","Marashe")
# display_welcome("Milasha","Subasinghe")
# display_welcome("Franco","Alioma")
# display_welcome("Chiko")

# def display_welcome(fname,lname="Why didn't you put a last name???"):
#     print(f"Hello {fname} {lname}, How is python programming today?")

# display_welcome("Raghad","Alkurdi") # positional argument
# display_welcome(lname="Yeukai",fname="Marashe") # keyword argument
# display_welcome("Milasha","Subasinghe")
# display_welcome("Franco","Alioma")
# display_welcome("Chiko")


# def zoo(animal, name, age):
#     print(
#         "In the Zoo, there is an animal with a name called",
#         name,
#         " it is a",
#         animal,
#         " and it is ",
#         age,
#         "years old",
#     )

# zoo("Lion","Buddy",89)
# zoo("Giraffe",age=9,name="Guyanese")


# arbitrary argument
# def number_argument(*args,country="Nigeria"):
#     print(
#         f"\n fullname:{args[0]} \n age:{args[1]} \n course:{args[2]} \n country:{country}"
#     )
#     print(type(args))

# number_argument("Chiko Liu",50,"Backend Development",country="South Africa")
# number_argument("Yeukai Marashe",500,"Frontend Development",country="Hongkong")
# number_argument("Franco Alioma",400,"Data Science")

#arbitrary keyword argument
# def keyword(fname="Chiko",lname="Franco",country="USA"):
#     print(f"fullname: {fname} {lname}\ncountry:{country}")


# keyword()
# keyword("Franco","Yeukai","Zimbabwe")
# keyword("Franco",country="Yeukai",lname="Zimbabwe")
# print(type(keyword()))

# def keyword(**franco):
#     print(type(franco))
#     print(f"fullname: {franco['name']}\nage:{franco['age']}\ncountry:{franco["country"]}")

# keyword(name="Chiko Franco",age=70,country="England")
# keyword(country="Scotland",name="Yeukai Marashe",age=40)

def declare(a, *args, **the):
    pass