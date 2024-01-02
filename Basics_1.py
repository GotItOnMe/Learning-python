print("i liked to eat \nfood")
print("i dont like to eat \tfood")
print(len("foooooood"))
print("1234567890"[-1]+"1234567890"[6:-1])
print("my bruddah"[2:])
print("his buddah"[::-2])
z="hello world"
print(z.split())
print("This is {2} a string {1} {0} {0}".format("not","inserted",":D"))
print("The {q} {b} {f} {h}".format(f=12, b="brown", q="quick", h=z))
pi=130.1415
print("pi is equal to {:.2f}".format(pi))
name="Walter"
print(f"Hello his name is {name}")
new_list=[1,2,3,4,5,6,7,8,9,0]
popped_item=[]
x=new_list.pop(2)
popped_item.append(x)
print (popped_item)
my_dicks={"Jeff":("12"+" inches"), "Me":("69"+"lightyears"),"My gf":("0"+"micrometers")} #can't concatenate numbers with letters
my_dicks["You"]="is stupid"
print(my_dicks["Jeff"])
print(my_dicks.values())
print(my_dicks.keys())
print(my_dicks.items())
print("\n")
t=(12,13,14,12,11) #tuple
print(t)
print(t.count(12))
print(t.index(12))
print("\n")
myset=set()
myset.add(2)
myset.add(2) #sets cannot have repeating units
myset.remove(2)
print('myset',myset) #sets are autosorted
print(set(t)) #converts into only one tings from var t
print(set("yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeet")) #splits it, such that there are only one of each
print(1==1 and 3<2<1 and ('h'!='h'))
print(not 1==2 or 2==2)
booleanvalue_true=True
if booleanvalue_true:
   print("my name is jeff")
three_dimensional_list=[(12,14,16),(13,15,17),[18],[19],[20]]
for x in three_dimensional_list:
   for y in x:
       if y%2==0:
           print(y)
name=[]
for letter in "My name is jeff":
   name.append(letter)
new_list_two=[(1,2),(3,4),(5,6),(7,8)]
for a,b in new_list_two:
   print(a)
   print(b)
d={'k1':1,'k2':2,'k3':3}
for key,value in d.items(): #called tuple unpacking
   print(key)
x=[1,2,3]
for item in x:
   pass
mystring="LIGMA"
for letter in mystring:
   if letter =="a":
       continue #goes back to the loop
   print(letter)
x=0
while x<5:
   print(x)
   if x==2:
       break
   x+=1
numberslist=list(range(12,0,-2))
index_count=0

for letter in 'abcde':
   print("At index {} the letter is {}".format(index_count,letter))
   index_count+=1
word="abracadabra"
for index,letter in enumerate(word):
   print(index)
mylist1=[1,2,3]
mylist2=['a','b','c']
for item in zip(mylist1,mylist2):
   print(item)

print('x' in [1,2,3])

maxandmin=[10,123,4,124,1]
max(maxandmin)
min(maxandmin)
import random as rand
rand.shuffle(maxandmin) #operates in place, cannot be assigned.
rand.randint(0,1000)

mystring=("bob likes eating doritoes")
mylist=[x**2 for x in range(0,11) if x%2==0]
print(mylist)
mylist=list(mystring)
print(mylist)
celcius=[0,10,20,34.5]
farenheit=[((9/5)*temp + 32) for temp in celcius]
result=[x if x%2==0 else f'ODD: {x}' for x in range(0,11)]
print(result)
mylist=[x*y for x in [2,4,6] for y in [1,10,1000]]
def say_hello(name='anonymous', surname=' '):
   print("Hello {0} {1}".format(name,surname))
   return name+surname
say_hello("James","Bond")
say_hello()
listnum=[1,3,5,7,5]

def even_check(listnum):
   for item in listnum:
       if item%2!=0:
           pass #continue is used if something else is used after it and goes back, pass is just a placeholder
       else:
           return True #breaks out of the function
           #you could also make a list by doing even_list.append(item)
   #then return it afterwards
print(even_check(listnum))

stock_prices=[('APPL',200),('ALPH',400),('TSLA',100)]
for ticker,price in stock_prices:
   print(ticker)
print("\n")
def stocks(stock_prices):
   current_max=0
   share=''
   for stock,worth in stock_prices:
       if worth>current_max:
           current_max=worth
           share=stock
       else:
           pass
   return (share,current_max)
best_stock,price=stocks(stock_prices)
print(best_stock)

import random
def shuffle():
   chosen=random.randint(1,3)
   return chosen
def ask_user():
   user_choice=str(input("Choose left, middle or right cup"))
   if user_choice=="right":
       user_choice=3
   if user_choice=="middle":
       user_choice=2
   if user_choice=="left":
       user_choice=1
   return user_choice
x=1 #set x to 0 to play
while x==0:
   if ask_user()==shuffle():
       print("correct")
   else:
       print("wrong")
   continue_game=input("try again? y/n")
   if continue_game=='n':
       x=1

def shuffle_list(mylist):
   random.shuffle(mylist)
   return mylist
def player_guess():
   guess=''
   guess=int(input("pick cup 1,2 or 3"))
   return guess-1
def play_game(mylist,guess):
   if mylist[guess]=='o':
       print("correct!")
   else:
       print(mylist)
mylist=['','o','']

mixed=shuffle_list(mylist)
guess=player_guess()
play_game(mixed,guess)

#args and kwargs
def myfunc(a,b,c=0,d=0,e=0):
   #returns 5% of the sum of a and b
   return sum(a,b)*0.05
#can add more arguments until e
def myfunc(*args): #args is arbitary, just need the star *
   return sum(args)*0.05 #infinte amount, accesssed as tuple args
print(round(myfunc(40,606,123,40,12,40.0,5))) #floating point error

def myfunc(**kwargs): #creates a dictionary
   if 'fruit' in kwargs: #same with kwargs as args, handles name arguements (dictionaries)
       print('My fruit of choice is {}'.format(kwargs['fruit']))
   else:
       print('i didnt find anything')
myfunc(fruit='apple')

def myfunc(*args,**kwargs):
   print("I would like {} {}".format(args[0],kwargs['food']))
myfunc(10,20,30, fruit='orange',food='eggs',animal='dog')

def splicer(mystring):
   if len(mystring)%2==0:
       return 'EVEN'
   else:
       return mystring[0]
names=['ANDY','EVE','ADAMS']
for item in map(splicer,names): #applies a function to every value in list
   print(item) #^also no brackets

def check_even(num):
   return num%2==0
mynums=[1,2,3,4,5,6]
even=[]
for x in filter(check_even,mynums):
   even.append(x)

print((lambda x:x**2)(2)) #can write simple function in other functions, can be used with list as well
map(lambda x:x[::-1],names) #map carries out the function in the set list
filter(lambda x:x%2==0,mynums) #filters out so that it's only ones that fit function
#generators
def numbers(x):
    for i in range(x):
        if i%2==0:
            yield i
print(list(numbers(11)))
#recursion
def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return(fibx-1)+fib(x-2)
print(fib(4))
#Local--> direct function                   Goes down in importance
#Enclosing--> the function surrounding function      For values, (x=y)
#Global--> The one outside functions
#Built-in--> built in things like print
x=50
def func():
   global x  # grabs from the global instead of reading it, you can edit it
   print(f'x is {x}')
   x='New Value'
   print(x)
