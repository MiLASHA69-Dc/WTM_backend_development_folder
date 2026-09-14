# Data structure / Data type

liu = [1,2,3.0,False,"Chiko Liu Abdulsamad"]
print(type(liu))
print(liu)
print(liu[3]) # start indexing from left to right
print(liu[-2]) # start indexing from right to left
print(type(liu[3]))
# slicing
# print(liu[0:3])
# print(liu[:3])
# print(liu[2:5])
# print(liu[2:])
# print(liu[-3:])
# print(liu[-1:-3])
liu[4]= "Yechale Mulu"
print(liu)
liu.pop(3)
print(liu)
liu.append("Raghad Alkurdi")
print(liu)
maria = ["Guttabingi Maria","Milasha N. Subasinghe","Yechala Mulu","Chiko Liu Abdulsamad"]

z = liu+maria
y = [10,50,1,45,30,100,95]
# print(liu+maria)
# print(liu.__add__(maria))
# print(dir(liu))
# print(z)
print(y)
print(sorted(y))
print(sorted(y,reverse=True))


#characteristics of list
# accept duplication
# indexing
# mutable - items can be replaced
# 



