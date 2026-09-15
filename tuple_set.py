stephanie = [1,1,2,2,2,2.3,2.3,False,"Asakhe"]
steph = tuple(stephanie)
a = set(stephanie)
print(steph)
print(type(steph))
print(a)
print(type(a))

# characteristics of tuple
# it is indexed
# it is subscriptable
# it is not changeable
# it is accept duplicate
print(steph[1])
# steph[1]= True
print(steph)

#characteristics of a set

# it is not subscriptable
# it is not changeable
# it is not indexed
# it is doesn't accept duplicate
# a.pop()
print(dir(a))

b = list(a)
print(b)
print(type(b))