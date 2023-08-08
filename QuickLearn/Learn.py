print("hello world")
the_world_is_flat=True
if the_world_is_flat:
    print("nope")

#-----------------------------------------------------
#strings
#-----------------------------------------------------
print(3*'alma'+'fasz')
#you can multyply stings and add them up or tougether
print('aaaaaaaaa''lahuacbara')
word='python'
print(word[2])
print(word[-1])
#normal index is like normally
#negative is counting backwords 
print(word[1:4]," this is with a given range")
#you can make this with a range, the firs one is included and the last one is not
#the start point is included and the end point is exluded
print(word[:2],' from the beginig of the string to the end of the range')
print(word[2:]," from the range to the end of the string")
#and you can do this with the negative shit
#adding just the ranges works as well 
print(word[2]+word[1:4])

print(len(word)," aka the length of the string")


#-----------------------------------------------------
#Lists
#-----------------------------------------------------
squers=[1,4,9,16,25,36,57,58]
#writing them out is the same as the strings, but here you can change the values of the individuals ex: squers[3]=555
#this works with letters and everything else as well, and you can change an etire range as well
print(squers)
squers[2:5]=['a','s','d']
print(squers)
#clearing a list is like this
squers[:]=[]
print(squers,"this is the deleted list")

#list in the list
a=['a','b','c']
b=[1,2,3]
c=[a,b]
print(c)
print(c[0])
print(c[0][1])

#-----------------------------------------------------
#while and stuff like that
#-----------------------------------------------------
a,b=0,1
while a<10:
    print(a)
    a,b=b,a+b

a,b=0,1
while a<10:
    print(a, end='|')
    a,b=b,a+b
#you can write all of your shits in one line with the word end and after that  with whta you want to make the separation

#-----------------------------------------------------
#even more satatements
#-----------------------------------------------------

#x=int(input("I need an intiger please"))

#if x<0:
 #   print('negative')
#elif x==0:
 #   print('nullaaa')
#else:
 #   print('positive')

#-------------------------------------------------------
#while
#-------------------------------------------------------

words=['cat','dog','hamster']
for w in words:
    print(w, len(w))

users={'anakin':'dead','steven hawkings':'dead in a wheel chare','kim Jong un':'maybe dead but not sure'}

for name, ishedead in users.items():
    print('this is ', name, 'and he or she is' ,ishedead)

for i in range(10):
    print(i)

# and again over here the intervals also plays just as  before and for a range you can set a len aka a length of a list or [] you need to use for i in range (len (a))

for n in range(2,10):
    for x in range(2,n):
        if n %x==0:
            print(n, 'equals',x,'*',n//x)
            break
    else:
        print(n,'is a prime number')

#here me out, the else belongs to the for statement, and it works like the try statement MEANING that the loops statements else part run when there is no break before, so if there is a break then it wont reach to the else part

for num in range(2,10):
    if num %2==0:
        print('found an even nymber' ,num)
        continue
    print('found an odd number',num)

#and here is the continue thingi thingi, it does what sounds like, it goes to the next number in the cicle


#----------------------------------------------------------------------------
#pass Statement
#----------------------------------------------------------------------------

#this is if you cant leave something empty and you can just simply say pass and you can work 


#----------------------------------------------------------------------------
#match  Statement
#----------------------------------------------------------------------------

def http_errors(status):
    match status:
        case 400|401|402: #you can set multiple cases for one case
            return 'bad request'
        case 404:
            'not found'
        case 418:
            'im a teapot'
        case _:
            'this is when nothing matches, then this is used to have a default answer'

#and this is the switch statement

class Points:
    x: int
    y: int

def where_is(point):
    match point:
        case Points(x=0,y=0) if x==y: #you can add if statement, if this is false then it goes to the next case
            print('origin')
        case Points(x=0,y=y):
            print(f"Y={y}")
        case Points(x=x,y=0):
            print(f"Y={x}")
        case Points():
            print('somewhere else')
        case _:
            print('not a point')

#you can have multiple parametters added to a case or it can be a class or a list, anything



#----------------------------------------------------------------------------
#functions
#----------------------------------------------------------------------------

def fib(n):
    """Print a Fibonacci series up to n"""
    #this is a dockstring do it to tell what the function does, make a habit of it
    a,b=0,1
    while a<n:
        print(a, end=" ")
        a,b=b,b+a

fib(2000)


def ask_ok(prompt,retries=4,reminder='Please try again!'):
    """this is an example"""
    while True:
        ok=input(prompt)
        if ok in('y','ye','yes'):
            return True
        if ok in ('n','no','nop'):
            return False
        retries=retries-1
        if retries<0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('do you really wanna quit?')


#----------------------------------------------------------------------------
#Keyword Arguments
#----------------------------------------------------------------------------

def parrot(voltage,state='a stiff', action='voom', type='blue'):
    """multyple argumets and theire order"""
    print('-- this parrot wouldnt', action, end=' ')
    print('if you put ', voltage,'volt through it.')
    print('--lovely plumage, the', type)
    print('-- its', state)

parrot(1000)
parrot(voltage=1000, action='PADUM TSSSSS')
parrot('a million', 'bereft of life', 'jump') 

#you can create functions wehere you set arguments where you have required arquments (voltage) and you have optional arguments(state, actions, type). Required is Required and the others has a default value but you can change those 

def cheeseshop(kind, *arguments, **keywords):
    print('do you have any', kind,'?')
    print('Im sorry but we all out of that',kind)
    for arg in arguments:
        print(arg)
    print('-'*40)
    for kw in keywords:
        print(kw,":",keywords[kw])

cheeseshop('Limburger','pice of shit','another pice of shit','and a third shit', shopkeeper='elon musk',client='alma')   

#When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of the form *name (described in the next subsection) which receives a tuple containing the positional arguments beyond the formal parameter list. (*name must occur before **name.) 



#----------------------------------------------------------------------------
#Data Structures
#----------------------------------------------------------------------------

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count('apple')
# How mant times the thing appears in the list

fruits.index('banana')
#the index of the first appearanta of the thing

fruits.index('banana',4)
#the first apparance after the 4th index

fruits.reverse()
#you can guess you idiot

fruits.append('grape')
# this isnt rocket sience either

fruits.sort()
# its in the name mate

fruits.pop()
# just like in JS its remove the last from the list


#----------------------------------------------------------------------------
#Using Lists as Queues
#----------------------------------------------------------------------------

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.popleft() # takes of the first one from the list

#----------------------------------------------------------------------------
#List Comprehensions
#----------------------------------------------------------------------------

squersagain=[]
for x in range(10):
    squersagain.append(x**2)

# OR

squersagain2=[]
squersagain2=list(map(lambda x:x**2, range(10)))

# OOOR

squersagain3=[]
squersagain3=[x**2 for x in range(10)]

#----------------------------------------------------------------------------
#List Comprehensions nested edition aka Matrix
#----------------------------------------------------------------------------

matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

transposed=[] # aka the rows gonna be colums and vice versa
transposed=[[row[i] for row in matrix]for i in range(4)]
print(transposed)

# to be honest I have no clue how the fuck this shit works, but I guess I can look after is I need it later


#----------------------------------------------------------------------------
#del statement
#----------------------------------------------------------------------------

# its a pop method but it works with the indexes
delTry=[-5,0,2,5,10,15]
del delTry[0] # removes the -5
del delTry[2:4] # 2 and 5 are gone
del delTry[:] # delete all

#----------------------------------------------------------------------------
#set
#----------------------------------------------------------------------------

# side not, you can use the 'in' keyeord to see if something is in an array, and it will throw back a true of a false

# the set gonna make an arrat without dublication 

a= set('abrakadabra') # {'a', 'r', 'b', 'c', 'd'}
b = set('alacazam') # {'a','l','c','z','m'}

# and you can use shit like a-b OR a|b OR a&b


#----------------------------------------------------------------------------
#Dictionaries
#----------------------------------------------------------------------------


alma='geci allat'
print(f'faszom az egeszbe {alma}')

class Employee:
    numOfEmployee=0
    raiseAmount=1.04
    
    def __init__(self,first,last,pay) -> None:
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        
        Employee.numOfEmployee+=1
        #if you use self.something that will be just a specific element, but if you use Employee.something that gonna be for the whole class

    def fullName(self):
        """this will write out the full name"""
        return '{} {}'.format(self.first, self.last)
    
    def applyRase(self):
        self.pay=int(self.pay* self.raiseAmount)

emp_1=Employee('aladar','tibike',50000)
emp_2=Employee('masztur','balint',60000)

# emp_1.first='sanyi'
# emp_1.last='tibi'
# emp_1.pay=50000

# emp_2.first='barmi'
# emp_2.last='aron'
# emp_2.pay=60000


print(emp_1.fullName())

print(Employee.fullName(emp_1)) # this is the same as above, but its  a bit more obvous
print(emp_1.pay)
emp_1.applyRase()
print(emp_1.pay)

#fun fact: you can change the value of the raiseAmount for everyone: Employee.raiseAmount=1.5 oooooorrrrrr just for a specific one: emp_1.raiseAmount=1.5
