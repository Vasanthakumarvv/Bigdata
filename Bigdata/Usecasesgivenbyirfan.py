#1.Create 2 variables with x as 100 & y as 10 respectively and find the Multiplication and division
# of both and store in some val as z and z1.
x,y=100,10
z,z1=x*y,x/y
print(z,z1)

#2. Create a as 2000 and find the division of a by y (created in step 1) and reassign a with
# the divided result (200).
a=2000
a=a/y
print(a)

#3. Prove Python is Dynamically Typed Language: Create x:int=100, then assign the x to y,
# but the datatype of y has to be of type string. (think about using some function like str()).
# Print the type of y and x
x=100
y=str(x)
print("Type of x is {} and Type of y is {}".format(type(x),type(y)))

#4.Prove Python has dynamic inference feature(We can reassign the value) DIReassign
p=4
print(p)
p=5
print(p)

#5. Prove Python is Strongly Typed Language (we cannot mix concat 2 diff data types)
a=100
b="vasanth"
print(type(a),type(b))
#print(a+b) -> unsupported operand type(s) for +: 'int' and 'str' it will throw

#6.Create variables a,b,c,d assigned with 10,20,30,40 respectively
a,b,c,d=10,20,30,40

#7. Prove Python variables are case sensitive
a,A=5,10
print(a,A)

#8. Prove variable name can’t start with numbers or cannot contains special character other than _
#1a=5 -> this will throw syntax error
#s$%=4 -> this will throw syntax error
__s=5

#9. Show some examples of when do we use single, double and triple (single/double) quotes
#Both single and double quote represents string
single='We "welcome" you.'
double="We 'welcome' you."
triple='''We 'welcome' you
with all the vaalue
of here'''
print(single,double,triple)

#10. Show an examples to use arithmetic, comparison, relational and logical operators.
#*Assignment
a,b=10,20

#Arithmetic
c,d = a+b,a-b
print(c,d)

#Relational
a=10
if a==10:
    print("pass")
a="Vasanth"
if a=="Vasanth":
    print("pass")

if a!="Vasanthak":
    print("fail")

#Logical:
a=10
if not a==5:
    print("pass")
a,b,c=10,20,30
if a<b and a<c:
    print("a is smaller")


#11. Write a program to find the greatest of 3 numbers
def greatestof3(a,b,c):
    if (a > b and a > c):
        print("a is greater")
    elif (b > a and b > c):
        print("b is greater")
    else:
        print("c is greater")


#12. Write a single program to find the given number is even or whether it is negative
# and print the output as (the given number is even but not negative or the given number
# is not even but negative or the given number is neither negative nor even)
def methodv(a):
    if (a%2==0 and a>0):
        print("the given number is even but not negative")
    elif (a%2!=0 and a<0):
        print("the given number is not even but negative")
    elif (a>0 and a%2!=0):
        print("the given number is neither negative nor even")

methodv(4)

#13. Write a nested if then else to print the course fees - check if student choosing bigdata,
# then fees is 25000, if student choosing spark then fees is 15000, if the student choosing
# datascience then check if machinelearning then 25000 or if deep learning then 45000
# otherwise if both then 25000+25000.
def choosecourse(course):
    if(course=="bigdata"):
        print("The bigdata fee is 25000")
    elif(course=="spark"):
        print("The spark fee is 15000")
    elif(course=="datascience"):
        subcourse=input("Enter a subcourse : ")
        if(subcourse=="machinelearning"):
            print("The machinelearning fee is 25000")
        elif(subcourse=="deeplearning"):
            print("The deeplearning fee is 45000")
        else:
            print("The machinelearning & deeplearning fee is 70000")


choosecourse("Bigdata")


#14.Check whether the given string is palindrome or not (try to use some function like reverse).
# For eg: x="madam" and y=”madam”, if x matches with y then print as "palindrome" else "not a  palindrome".
x="madam"
y="madam"
if(x[::-1]==y):
    print("Palindrome")
else:
    print("Not a palindrome")

#15.Check whether the val x=100 is an integer or string.
# (try to use some functions like str or upper function etc to execute this use case)
# or use isinstanceof(variablename,datatype) function.
x="100"
print(str(x).capitalize())
print(isinstance(x,str))
