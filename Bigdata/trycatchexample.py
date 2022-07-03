
#1.Simple try except block -> if there is no exception else will be printed
try:
    lst=["eng","tam","tel"]
    print("Enter 0 for English / 1 for tamil / 2 for telugu")
    userinput=int(input())
    print("user selected {}".format(lst[userinput]))
    print("IVR continues with 10 more lines of the code")
except Exception as msg:
    print("Caught in exception block with error {}".format(msg))
else:
    print("No exception occured")


#2.try and multiple except block -> Based on the error we can catch in except (Either defined(IndexError) or default(Exception))
#re run from beginning for 2nd exception
try:
    lst=["eng","tam","tel"]
    print("Enter 0 for English / 1 for tamil / 2 for telugu")
    userinput=int(input())
    print("user selected {}".format(lst[userinput]))
    print("Enter some Number")
    userinput2=int(input())
    print(userinput/userinput2)
    print("IVR continues with 10 more lines of the code")
except IndexError as msg:
    print("Caught in exception block with error {}".format(msg))
except Exception as msg:
    print("Caught in exception block with error {}".format(msg))
else:
    print("No exception occured")

finally:
    print("Finally will be executed at any cost")
    print("Close all the DB Connection")
    print("Have a nice day")

#3.Continuation of the progrm should be executed: for that we should keep incentive in seperate block
try:
    sal=''
    bonus_sal=sal+1000
    print("The bonus salary is {}".format(bonus_sal))
    incentive=bonus_sal+2000
except Exception as msg:
    print("Some exception occured {}".format(msg))

#4.Predefined exception using raise -> it should always come inside if
try:
    amount = 1999
    if amount < 2999:
        # raise the ValueError
        raise ValueError("please add money in your account")
    else:
        print("You are eligible to purchase DSA Self Paced course")

# if false then raise the value error
except ValueError as e:
    print(e)

#5.How to avoid getting except block in python -> we can handle everything in if and else block
try:
    vowels=['a','e','i','o','u']
    index=int(input())
    if len(vowels)>index:
        print(vowels[index])
    else:
        print(vowels[len(vowels)-1])

except IndexError as msg:
    print("Index error happened{}".format(msg))