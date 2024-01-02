#Advanced_python_basics
print(hex(200))
print(bin(200))
print(pow(2,4,3)) #x**y%z
print(abs(-2))
print(round(3.513,2))
s="hello world"
print(s.count("o"))
print(s.find("o"))
print(s.center(20,'z'))#letter has to be one letter long
print(s.isalpha())
print(s.islower())
print(s.endswith("d"))
print(s.split('l'))
print(s.partition(" ")) #returns front, seperator and back
s={1,2,3}
s.add(1)
sc=s.copy()
s.remove(2)
print(f"set s difference:{s.difference(sc)}") #what is in set s but not in set sc
print(sc)
print(sc.difference_update(s))#changes the sc by removing the difference
print(sc)
s.discard(2) #discards even if it is present
print(s)
s1={1,2,3}
s2={1,4,5}
s2.intersection_update(s1)#updates s1 to intersection
print(s2)
s1={1,2,}
s2={1,2,4}
s3={5}
print(s1.isdisjoint(s2)) #checks if there is nothing in common
print(s1.issubset(s2)) #checks if its a subset, use superset() for superset
print(s1.symmetric_difference(s2)) #returns difference in both sets
print(s2.union(s3))#in either sets
#dictionaries
print("\n")
d={k:v**2 for k,v in zip(['a','b','c','d'],range(10))} #zip conjoins the lists, one after another
print(d)
for k in d.items():
    print(k)
print(d.values())
#advanced lists
l=[1,2,3,4,5]
l1=[6,7,8,9]
l.extend(l1)
l.pop(2)# pops last items and returns it
l.remove(1) #removes value
l.reverse()
print(l)
