age = 22
# age = 12

name = 'Matt'

todayIsCold = True

print(f'Hello my name is {name} and I am {age} years old.');

if age > 18 :
    print('You are older than 18.')
    print('this is another line')
else:
    print('You are younger than 18.')

def hello():
    print('Hello World!')
    print('Hello Dog!')
    print('Hello Cat!')

hello()

def sentence(name='', age=0):
    return "Hello {} you are {} years old".format(name, age)

s = sentence('test', 10)
print(s)
