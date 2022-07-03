y=100.0
print(type(y))

s=int(y)
print(type(s))

s1="I am vasanth"
print(s1)

print(s1[1])

print(s1*2)

print(len(s1))

print(s1[-4:-2])

print(s1[::-1])

s=" i am vasanth "
print(s.strip())

print(s.find("am",0,12))

lst=[1,3,5,6,-10,-5]
print(max(lst))
lst.sort()
print(lst)

dict1={1:"John",2:"Wow",5:"bell"}
print(dict1)
print(dict1.items())
print(dict1.keys())

k=dict1.values()
print(type(k))
for i in k:print(i)

a=20
b=22
#Memory Location will be the same for below
print(id(a))
print(id(b))
print(a is b)
