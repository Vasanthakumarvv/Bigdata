#26. Write a program using for loop to print even numbers and odd numbers in the below range of data
# (generate using range function) [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] output should be
# with even as 6,8,10,12,14,16,18,20 and odd as 5,7,9,11,13,15,17,19.

oddnos=[]
evennos=[]
for i in range(5,21):
    if i%2==0:
        oddnos.append(i)
for i in range(5,20):
    if i%2!=0:
        evennos.append(i)
print(oddnos)
print(evennos)

#27. Write a while loop to loop from 0 till 21 with the increment of 3, the result should be
# exactly 3,6,9,12,15,18 and store this result in a list

#way1
lst=[]
for i in range(0,21,3):
    lst.append(i)
print(lst)

#way2
lst1=[]
i=1
while(i<21):
    if(i%3==0):
        lst1.append(i)
    i+=1
print(lst1)


#28. Write a for or while loop to print the cube of 4, result should be 4*4*4=64
# (initiate some variable outside the loop with 4 and loop through 3 times to achieve the result)
a=4
cube=1
for i in range(3):
    cube=cube*4
print("Cube value is : ",cube)

# 29. Create a list as sal_lst=[10000,20000,30000,10000,15000], loop through the list and add 1000
# bonus to the salary and store in another list sal_bonus_lst=[11000,21000,31000,11000,16000]
# then store the bonus applied salary in another list where sal>11000
sal_lst=[10000,20000,30000,10000,15000]
bonus=1000
sal_bonus_lst=[]
salmaxval=[]
for i in sal_lst:
    sal_bonus_lst.append(i+1000)
    if(i+1000>11000):
        salmaxval.append(i+1000)
print("sal_bonus_lst values : ",sal_bonus_lst)
print("salmaxval values : ",salmaxval)

#30. Write a do while loop to print “Inceptez technologies” n number of times as per the input you
# get from the user. Minimum it has to be printed at least one time regardless of the user input.
i=3
n=3
while(True):
    print("Inceptez technologies")
    if(i>n+1):
        break
    i+=1

# 31. From the given list of list of elements produce the following output using nested for loop
# lst1=[[10,20],[30,40,50],[60,70,80]], calculate the sum of all number, calculate the min value and
# the max value of all the elements in the lst1.
lst1=[[10,20],[30,40,50],[60,70,80]]
sum=0
lst2=[]
for i in lst1:
    for j in i:
        sum=sum+j
        lst2.append(j)
print(sum)
lst2.sort(reverse=True)
print("Max value is {} and min value is {}".format(lst2[0],lst2[len(lst2)-1]))

# 32. Create a looping construct to create 3 tables upto 10 values. Output should be like this…
# 1 x 3 = 3
# 2 x 3 = 6
# 3 x 3 = 9
# .
# .
# 10 x 3 = 30
n=3
for i in range(1,11):
    print(i," * ",n," = ",i*n)


