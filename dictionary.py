# a ={key:value}
a =  {"name": "Chiko Liu Abdulsamad","age":7000, "is_mentor":True}

print(a)
print(type(a))
# print(dir(a))
print(a.keys())
print(a.values())
print(a.items())
print("name: ",a["name"])
print("age: {}".format(a["age"]))
print(f"is_mentor: {a["is_mentor"]}")

a["name"] = ["Abanda Glory","Chiko Liu Abdulsamad"]
a["age"] = [4500,7000]
a["is_mentor"] = [False,bool(1)]
print("name: ",a["name"])
print(a)

a["Country"]="Cameroon"
print(a)
print(a["name"][1])
# print("name: ",a["name"])
# print("age: {}".format(a["age"]))
# print(f"is_mentor: {a["is_mentor"]}")
# print(f"Country: {a["Country"]}")

# b = [9]
# b.append(a)
# print(b)
# print(b[1]["Country"])

#statements, loops, list comprehension, def ,class, inheritance