class Dog:

    dogInfo = 'Hey dogs are cool.'

    def bark(self):
        print('BARK!')

    def bark2(self, str):
        print('BARK! '+str)


myDog = Dog()

myDog.bark()
myDog.bark2('TEST')

myDog.name = 'Fido'
myDog.age = 16

print(myDog.name)
print(myDog.age)

print(Dog.dogInfo)

Dog.dogInfo = 'Hey there.'
print(Dog.dogInfo)

class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

myCat = Cat('fadle', 13, 'white')       
print(myCat.name)