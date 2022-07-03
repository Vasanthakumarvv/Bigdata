#16.Create a list with a range of 10 values starting from 2 to 11 and prove mutability by
# updating the 3rd element with 100 and prove resizable properties by adding 100 in the 5th position.
x=[]
for i in range(2,12):
    x.append(i)
print(x)
x.append(110)
x[3]=100
x[5]=100
print(x)

#17. Create a tuple of 2 fields eg. ("Inceptez","Technologies","Pvt","Ltd"), prove immutability
# and non resizable nature, access the 2nd and 4th fields and store in another tuple.
x=("Inceptez","Technologies","Pvt","Ltd")
x[0]="aa" #-> will get type error TypeError: 'tuple' object does not support item assignment
y=(x[1],x[3])
print(y)

#18. Convert the list of tuples [("Inceptez","Technologies"),("Apple","Incorporation")] to
# list of dictionary type, using for loop as given below
# [{"Inceptez":"Technologies"},{"Apple":"Incorporation"}] ,
# once the list of dictionary is arrived print only "Incorporation" by passing "Apple"
# as a key using dict["Apple"] and dict.get("Apple") and try with dict["Apple1"]
# and dict.get("Apple1") then find the difference between get and using[] notation.

x=[("Inceptez","Technologies"),("Apple","Incorporation")]
a={}
for (key,value) in x:
    a.setdefault(key,[]).append(value)

print(a['Apple'])


#19. Create a list of tuple as given below and delete all duplicate tuples of the list
# lst=[("Inceptez","Technologies"),("Apple","Incorporation"),("Inceptez","Technologies"),
# ("Inceptez","Technologies")]
lst=[("Inceptez","Technologies"),("Apple","Incorporation"),("Inceptez","Technologies"),("Inceptez","Technologies")]
setv=set(lst)
lst=list(setv)
print(lst)

#20. Append ("Intel","Corp") in the above de duplicated list
lst.append(("Intel","Corp"))
print(lst)

#21. Convert the lst_dict= [{"Inceptez":"Technologies"},{"Apple":"Incorporation"}]
# to lst1=["Inceptez","Apple"] , think about using for loop, list() function, keys function and
# list append functions to achieve this.
lst_dict= [{"Inceptez":"Technologies"},{"Apple":"Incorporation"}]
lst1=[]
for i in lst_dict:
    for key in i.keys():
        lst1.append(key)

print("List1 values are {}".format( lst1))
print()

#22. Create a list of values lst=[10,20,40,30,20], find the first, last values of the list, sort the list
# in ascending order, sort in descending order, print the minumum and maximum values of the descending
# sorted list, find the sum of all elements in the list, remove the number 30 and 20 from the list.
lst=[10,20,40,30,20]
firstvalue=lst[0]
lastvalue=lst[len(lst)-1]
print("First value is {} and Last value is {} : ".format(firstvalue,lastvalue))
lst.sort(reverse=True)
print("Descending Order : ",lst)
maxvalue=lst[0]
minvalue=lst[len(lst)-1]
print("maxvalue is {} and minvalue is {} : ".format(maxvalue,minvalue))
sum=0
for i in lst:
    sum=sum+i

print("Sum is : ",sum)
lst.remove(30)
lst.remove(20)
print("After removing the values from list is : ",lst)

#23. Do the above same (step 25) operation in the tuple of elements tup=(10,20,40,30,20)
tup=(10,20,40,30,20)
firstvalue=tup[0]
lastvalue=tup[len(tup)-1]
print("First value is {} and Last value is {} : ".format(firstvalue,lastvalue))
lst=list(tup)
lst.sort(reverse=True)
tup=tuple(lst)
print("Descending Order : ",tup)
maxvalue=tup[0]
minvalue=tup[len(tup)-1]
print("maxvalue is {} and minvalue is {} : ".format(maxvalue,minvalue))
sum=0
for i in tup:
    sum=sum+i
print("Sum is : ",sum)
lst=list(tup)
lst.remove(30)
lst.remove(20)
tup=tuple(lst)
print("After removing the values from list is : ",tup)

#24. Convert the string to list from 24. Convert the string to list from
# str1="Inceptez Technologies Pvt Ltd" to lst_str1=['Inceptez', 'Technologies', 'Pvt', 'Ltd']
str1="Inceptez Technologies Pvt Ltd"
lst_str1=str1.split(" ")
print("liststr : ", lst_str1)

#25. With the below given data in the format of list(list(elements))
#emplstlst= [["1", ("Arun","Kumar"), "10000"],["2", ("Bala","Mohan"), "12000"]]
# Display the below output for all of the 5 given simple scenarios


# a. Convert the first element of the above list into tuple
# ("1", ("Arun","Kumar"), "10000")
emplstlst= [["1", ("Arun","Kumar"), "10000"],["2", ("Bala","Mohan"), "12000"]]
tup1=tuple(emplstlst[0])
print("List to tuple of first element : ",tup1)

# b. Print the second element's second element and reverse the first and last name as given below
# ("Mohan","Bala")
secondele = emplstlst[1][1]
print("Print the second element's second element : {}".format(secondele))
lst2=list(secondele)
lst2.reverse()
tup2=tuple(lst2)
print("Reversed of Print the second element's second element : {}".format(tup2))


# c. Convert the emplstlst into tuples(tuples)
# emplstlst= (("1", ("Arun","Kumar"), "10000"),("2", ("Bala","Mohan"), "12000"))
emplstlst1=[]
for i in emplstlst:
    emplstlst1.append(tuple(i))
print("Convert the emplstlst into tuples",emplstlst1)

# d. Add all salary of the above list
# 22000
Totalsal=0
for i in emplstlst:
    Totalsal=Totalsal+int(i[2])
print("Total Salary : ",Totalsal)




