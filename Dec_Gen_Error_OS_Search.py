#decorators with @
def hello():
    return "hello"
print(hello())
greet=hello
print(greet())

def hello(name="Jose"):
    def greet():
        return "This is the greet() func inside hello"
    def welcome():
        return "This is welcome() inside hello"
    print("return function")
    if name=="Jose":
        return greet
    else:
        return welcome#can't add () after for after transcribing only
print(hello("Jose")) #idk why, it is the function name it returns
meet=hello("Sanzhez")
print(meet())
#welcome() is not defined outside
def other(some_def_func):
    print("other code runs here!")
    print(some_def_func)
print("\n")
print(hello("Sanchez"))
other(print(hello("Sanzhez")))
def new_decorator(og_func):
    def wrap_func():
        print("Some random code")
        og_func()
        print("THE END")
    return wrap_func()
def func_needs_decorator():
    print("Decoration needed")
new_decorator(func_needs_decorator)
@new_decorator #decorator with func name wraps the function
def quickmaths():
    print(2+2)
def create_cubes(n):
    for x in range(n):
        yield(x**3)
for x in create_cubes(12):
    print(x)
print(list(create_cubes(12)))
def gen_fibon(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b #a becomes b
for x in gen_fibon(10):
    print(x)
def simple_gen():
    for x in range(3):
        yield x
g=simple_gen()
print(next(g))
print(next(g))
print(next(g)) #returns the next one

s='hello'
for letter in s:
    print(letter)
try: next(s) #doesnt support it
except: pass
s_iter=iter(s)
print(next(s_iter))
from collections import Counter
mylist=[1,1,1,1,1,1,2,2,2,2,3,3,3,3,3]
print(Counter(mylist))
letter='aaaabbbbccccddd'
c=Counter(letter)
print(c.most_common(2)) #two most common
from collections import defaultdict
d=defaultdict(lambda: 0) #sets default value
print(d["wrong key"])
mytuple=(10,20,30)
from collections import namedtuple
Dog=namedtuple('Dog',['age','breed','name'])
sammy=Dog(age=5,breed="Husky",name="Sam")
print(sammy[0])
f = open("practice.txt","w+")
f.write("This is a test string")
f.close()
import os
print(os.getcwd())
print(os.listdir("C:\\Users"))
import shutil
try:shutil.move("practice.txt","C:\\Users\\justi") #moves this
except: pass
list=os.listdir("C:\\Users\\justi")
print(list.index("practice.txt"))
#shutil.rmtree(path) #removes all files and folders in path
#import send2trash
#send2trash.send2trash("practice.txt"), pip install still doesn't work
x=0
for folder,sub_folder,files in os.walk(os.curdir):
    print(f"Currently looking at {folder}")
    print("\n")
    print("The subfolders are:")
    for sub_fold in sub_folder:
        print(f"sub folders:{sub_fold}")
    print("\n")
    for f in files:
        print(f"File:{f}")
        x=x+1
    print("\n")
    if x>10:
        break
import datetime
mytime=datetime.time(2,20)
print(mytime)
today=datetime.date.today()
print(today)
print(today.ctime())
print(datetime.datetime.today())
print(today.replace(year=2020))
#Date addition and subtraction
date1=datetime.date(2021,11,3)
date2=datetime.date(2020,11,3)
print(date1-date2)
datetime1=datetime.datetime(2021,11,3,22,0)
datetime2=datetime.datetime(2020,11,3,12,0)
mydiff=datetime1-datetime2 #returns in days and seconds
print(mydiff.seconds)
print(mydiff.total_seconds)
import math
print(round(4.5))
print(round(5.5)) #balances the values out in large calculations
print(math.log(math.e,100))
import time
t=1000*time.time()
print(t)
import random
random.seed(101)
print(random.randint(0,100)) #74
print(random.randint(0,100)) #24
print(random.randint(0,100)) #69
mylist=range(20)
print(mylist)
print(random.choice(mylist))
#sample with replacement, gets chosen multiple times
print(random.choices(population=mylist,k=10))
#sample with replacement
print(random.sample(population=mylist,k=10))
mylist=[1,1,1,9,12,2,2,2,2]
print(random.shuffle(mylist))
print(random.uniform(a=0,b=100))
print(random.gauss(mu=0, sigma=1)) #gaussian distribution
import pdb
x="hello"
y=1
q=2
#pdb.set_trace() #pauses the script and tells you what variables are, use what isnt there to quit
import re
text="The agen's phone number is 408-123-9192. The second phone is..."
pattern="phone"
match=re.search(pattern,text)
print(match)
print(match.span())
print(match.start())
print(match.end())
matches=re.findall("phone",text)
print(len(matches))
for match in re.finditer("phone",text):
    print(match.group())
pattern="not in text"
print(re.search(pattern,text)) #not in
#\d a digit
#\w alphanumeric, includes_
#\s white space
#\D a non digit
#\W a non alphanumeric =D
#\S Non-whitespace
phone=re.search(r"408-123-9192",text)
print(phone)
#+ one or more
#{3} exactly three times
#{2,4} occurs 2 to 4 times
#{2:} occurs more than two times
#* occurs zero or more times
#? once or none times
phone=re.search(r"\d+-\d*-\d{4}",text)
print(phone)
phone_pattern =re.compile(r"(\d{3})-(\d{3})-(\d{4})")
results=re.search(phone_pattern,text)
print(results.group())
print(results.group(1))
re.search(r"car|dog","I want a dog") #searches for either
print(re.findall(r"...at","The cat in the hat went splat")) #the things in front
print(re.search(r"^\d","1o ne is a number")) #searches if entire text starts with a one
print(re.search(r"\d$","This ends with a number 2"))
phrase="there are 3 numbers. 34? inside 5 this sentence"
pattern=r"[^\d.?]+" #everything that isnt a number
clean=''.join(re.findall(pattern,phrase))
print(clean)
text="Only find the hyphen-words in this sentence. But you dont know how long-ish they are"
pattern=r"[\w]+-[\w\d]+" #no ^, the [] is usually just there cause easier to read
print(re.findall(pattern,text))
text="are u catfish?"
texttwo="Hello? Catnap"
textthree="Hello, have you seen this caterpillar?"
print(re.search(r"\wat(fish|nap|erpillar)",texttwo)) #cause its upper case
hello()

def func_one(n):
    return[str(num) for num in range(n)]
def func_two(n):
    return map(str,range(n))
import time
start_time=time.time()
result=func_one(1000000)
end_time=time.time()
elapsed_time=end_time-start_time
# needs to spend a lot of time running
import timeit
stmt='func_two(100)'
setup="def func_two(n):" \
      "return map(str,range(n))"
print(timeit.timeit(stmt,setup,number=10000)) #time it takes to run this 10000 times

f=open("fileone.txt","w+")
f.write("ONE FILE")
f.close()
f=open("filetwo.txt","w+")
f.write("TWO FILE")
f.close()
import zipfile
comp_file=zipfile.ZipFile("comp_file.zip","w")
comp_file.write("fileone.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.write("filetwo.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()
zip_obj=zipfile.ZipFile("comp_file.zip","r")
zip_obj.extractall("extracted_content")
dir_to_zip="C:\\Users\\justi\\PycharmProjects\pythonProject6\\extracted_content"
output_filename="example"
shutil.make_archive(output_filename,"zip",dir_to_zip)
shutil.unpack_archive("example.zip","final_unzip","zip")
