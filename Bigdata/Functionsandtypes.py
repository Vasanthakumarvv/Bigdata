def ivroptions(arg1,arg2,arg3):
    print("Entered inside the method")
    additionalval =arg1+arg2+arg3
    print("Method is over")
    return additionalval

x=ivroptions(20,24,22)
print("additional value is {}".format(x))