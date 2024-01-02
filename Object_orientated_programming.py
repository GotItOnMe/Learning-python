#Object orientated programing.
class NameOfClass():
    def __init__(self,param1,param2):
        self.param1=param1
        self.param=param2
    def some_method(self):
        print(self.param1)

class Dog():
   #Class Object attribute remains the same for class:
   __species='mammal' #strongly private accessed externally with different names
   def __init__(self,mybreed,name,height,gender='male'): #calls on this
       self._hiddeng=gender #shows that it is weakly private
       self.breed=mybreed
       self.name=name
       self.height=int(height)
   #operations --->methods
   def bark(self,number):
       print('WOOOF! my name is {} and the number is {}'.format(self.name,number))
       print(self._hiddeng) #can still be accessed by external code
my_dog=Dog(mybreed='Lab',name='Max', height=132.2)
print(my_dog.height)
new_dog=Dog('lab','Bane',1320)
print(new_dog.name) #characteristics so no brackets
new_dog.bark(12)#is a function so yes brackets
print(my_dog._Dog__species)

class Animal():
   def __init__(self):
       print('animal created')
   def who_am_i(self):
       print('I am a BEAST')
   def eat(self):
       print('NOM NOM NOM')

class Dog(Animal):   #derived class
   def __init__(self):
       Animal.__init__(self)
       print('dog created')
   def who_am_i(self):
       print('I am a dog!') #overwrites it
   def bark(self):
       print("WOOF") #adds in more functions
doge=Dog()
doge.eat() #inheritence
#polymorphism
class Dog():
   def __init__(self,name):
       self.name=name
   def speak(self):
       return self.name+" Says Woof"
class Cat():
   def __init__(self,name):
       self.name=name
   def speak(self):
       return self.name+" Says MEOW"
niko=Cat("niko")
felix=Dog("felix")
print(felix.speak())
for pet in [niko,felix]:
   print(type(pet))
   print(pet.speak())
def pet_speak(animal):
   print(animal.speak()) #carries the function over
pet_speak(niko)
class Animal():
   def __init__(self,name):
       self.name=name
   def speak(self): #abstact functions can be replicated
       return "Subclass must implement this abstract method" #supposed to be raise and show error

class Book():
   def __init__(self,title,author,pages):
       self.title=title
       self.author=author
       self.pages=pages
   def __str__(self):
       return f"{self.title} by {self.author} with {self.pages} pages" #string representation
   def __len__(self):
       return self.pages #can't use as string because then if tries to find length of 200 also its a 200 in string but in int
   def __del__(self):
       print("book instance has been deleted")
b=Book("Python rocks",'Jose',200)
print(b)
print(len(b))
del b #deleted class b
class Simple():
   def __init__(self,value):
       self.value=value
   def add_to_value(self,amount):
       self.value=self.value+amount
s=Simple(300)
s.add_to_value(100)
print(s.value)

#magic methods: y.__radd__(x) for when add hasnt been implemented in x
#__sub__ =                           lt,le,eq,ne,gt,ge = <,<=,==,!=,>,>=
#__mul__ = *                          TO ACT LIKE CONTAINERS:
#__truediv__ = /                      __repr__ for representing in str
#__floordiv__ = //                   __len__ for len()
#__mod__= %                         __getiitem__ for indexing
#__pow__= **                        __setitem__ for assigning to indexed values
#__and__= &                         __delitem__ for deleting indexed values
#__or__= ^                          __iter__ for iteration over objects
#__xor__ = |                       __contains__ for in
class Circle():
   pi=3.14
   def __init__(self,radius=1):
       self.radius=radius
       self.area=radius**2*Circle.pi #Circle and self are interchangeable
   def getcircumference(self):
       return self.pi*self.radius*2
   def __and__(self,other):
       return self.area+other.area
Circle1=Circle()
Circle2=Circle(2)
print(Circle1.getcircumference())#need to initiate a class
print(Circle1.area)
print("magic", Circle1&Circle2)
# cls methods/static method/properties
class Rectangle():
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self._two=2
    def calculatearea(self,width,height):
        return self.width*self.height
    @classmethod
    def new_square(cls,side_length):
        return cls(side_length,side_length)
    @staticmethod #removes need for self
    def HeightIsFive(height,width):
        if height==5 and width==5:
            return 5
        else:
            return False
    @property
    def two(self):
        return self._two
    @two.setter #without it, property two() cannot be changed
    def two(self,value):
        self._two=value

Square=Rectangle.new_square(5)
print(Square.HeightIsFive(Square.height,Square.width))
try:
    Square.two=3
except:
    print("property cannot be changed")
print(Square.two)
#errors
def ask_for_int():
    while True:
        try:
            result=int(input("please provide number:")) #if there is error, the rest doesnt execute
            if result>100:
                raise ValueError('number less than 100')
        except OSError:
            print("bruh how")
        except:
            print("type error, probably")
        else:
            print("if there are no errors")
            break
        finally:
            print("this always runs")
    print(result)
ask_for_int()

