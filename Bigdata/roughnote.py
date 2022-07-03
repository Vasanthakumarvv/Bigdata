#34a.Positional & Keyword
def greatestof3(a,b,c):
    if (a > b and a > c):
        print("a is greater")
    elif (b > a and b > c):
        print("b is greater")
    else:
        print("c is greater")

greatestof3(22,44,66)
greatestof3(c=22,a=44,b=66)

