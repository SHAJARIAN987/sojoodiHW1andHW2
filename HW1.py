myString = "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics"

print(myString)
print(len(myString))
print(myString[0])
print(myString[0:3])
print(myString[len(myString)-3:len(myString)])
myStringBACK = ""
for i in range(1, len(myString)+1):
    myStringBACK = myStringBACK + myString[-i]
print(myStringBACK)
print(myString[1:-1])
print(myString.upper())
print(myString.replace("a", "e"))
print(myString.split(",")[1])