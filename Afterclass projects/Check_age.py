Age= int(input("Enter your age (e.g: 10 or 20)"))
if Age >=50:
   print("You are a senior citizen")
elif Age >=18:
    print("You are an adult")
elif Age<18:
    print("You are not an adult" )
    if Age <=3:
     print("You are an infant ")
    elif Age<=12:
       print("You are a kid/Child")
    else:
       print("You are a teen")
else:
   print("invalid input")
       