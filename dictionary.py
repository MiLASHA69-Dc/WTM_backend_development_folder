chiko = {
    "name":"chiko liu Abdulsamad","mentorship_course":"Backend development","is_mentor":True
}

print(chiko)
# print(type(chiko))
print(f"Course: {chiko["mentorship_course"]}")
print("Name: {}".format(chiko["name"]))
print("Is a mentor:",chiko["is_mentor"])

chiko["country"]="Nigeria"


print(chiko)
chiko["name"]=["Raghad Alkurdi","Milasha Subasinghe","chiko Liu AbdULSamad"]
# print(chiko)
# chiko["name"][2] = "Chiko Liu Abdulsamad"
chiko["name"][2]=chiko["name"][2].lower()
# print(chiko)
# print(chiko["name"][2])

# print(dir(chiko))
print(chiko.keys())
print(chiko.values())

# Statements (if, else, elif), Loops(while for), list comprehension, function def, classes class, inheritance