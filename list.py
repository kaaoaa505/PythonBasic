dogNames = ['Fido', 'Sean', 'Sally', 'Mark', 1234, False, True, 10.99]

del(dogNames[2])

dogNames[1] = 'Jane'

print(dogNames[2])
print(len(dogNames))
print(dogNames)

for dog in dogNames:
    print(dog)

for i in range(1, 10):
    print(i)

age = 10
while age > 0:
    age -= 1
    print(age)