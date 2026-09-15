stephanie = [1,2.3,False,"Asakhe"]

print(type(stephanie))

print(stephanie[0])
print(type(stephanie[0]))
print(type(stephanie[2]))
stephanie[2] = True
print(stephanie)

stephanie.append("WTM rocks")
print(stephanie)
# adding a list to an existing list
declare = [3,5,3.0,7,6]
steph = stephanie + declare
print(steph)
steph.pop(8)
# steph.pop(-2)
print(steph)
print(sorted(declare,reverse=False))
print(sorted(declare,reverse=True))
# characteristics/ Behaviour
# it is indexed
# it is changeable - items in a list can be replaced
# list accepts accepts duplicate
print(len(declare))


