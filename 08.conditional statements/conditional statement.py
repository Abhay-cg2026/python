#task 1
a=int(input("Enter a number: "))
if a>10:
    print("greater then 10")
#task 2
a=int(input("Enter age: "))
if a>18:
    print("Adult")
#task 3
a=int(input("Enter a number : "))
if a>0:
    print("positive")
#task 4
marks=int(input("enter a number :"))
if marks>=40:
    print("pass")
else:
    print("fail")
#task 5
a=int(input("Enter a number : "))
if a==0:
    print(0)
#task 6
a=int(input("Enter a number : "))
if a>0:
    print("Positive")
else:
    print("not positive")
#task 7
age=int(input("Enter a number : "))
if age>=18:
    print("Adult")
else:
    print("minor")
#task 8
numbers=int(input("Enter a number"))
if numbers%2==0:
    print("Even")
else:
    print("Odd")
#task 9
marks=int(input("Enter marks : "))
if marks>=40:
    print("pass")
else:
    print("fail")
#task 10   
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
if a>b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")
#task 11
marks=int(input("Enter a number : "))
if marks>=90:
    print("Grade A")
elif marks>75 and marks<89:
    print("Grade B")
elif marks>60 and marks<74:
    print("Grade C")
elif marks>40 and marks<59:
    print("Grade D")
else:
    print("fail")

#task 12
number=int(input("Enter a  number : "))
if number>0:
    print("Positive")
elif number<0:
    print("Negative")
else:
    print("Zero")

#task 13
day=int(input("Enter a day number : "))
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
else:
    print("Friday")

#task 14
marks=int(input("Enter a number : "))
if marks>=90 and marks<100:
    print("Excellent")
elif marks>75 and marks<89:
    print("Good")
elif marks>40 and marks<74:
    print("Pass")
else:
    print("fail")

#task 15
a=int(input("Enter a digit : "))
if a==1:
    print(1)
elif a==2:
    print(2)
elif a==3:
    print(3)
else:
    print("other")
#task 16 
age=int(input("Enter age : "))
if age>=18:
    if age<=60:
        print("age is between 18 and 60")
else:
    print("age is not between 18 and 60")

#task 17
marks=int(input("Enter a number : "))
if marks>=75:
    print("good")
elif marks>=40:
    print("passed")
else:
    print("failed")

#task 18
a=int(input("Enter a number : "))
if a>0:
    if a>100:
        print("greater than 100")
    else:
        print("not greater than 100")
else:
    input("number is negative")

#task 19
age=int(input("Enter age"))
if age>=18:
    print("atleast 18 yrs old")
    if age>=60:
        print("greater than 60")
    else:
        print("not greater than 60")
else:
    print("not greater than 18")

#task 20
n1=int(input("Enter a number : "))
if n1!=0:
    print("it is non zero")
    if n1>0:
        print("positive")
    else:
        print("negative") 
else:
    print("it is zero")

#task 21
age=int(input("Enter age : "))
marks=int(input("Enter marks : "))
if age>=18 and marks>=40:
    print("Eligible")
else:
    print("not eligible")

#task 22
number=int(input("Enter number : "))
if number<10 or number>100:
    print("special")
else:
    print("not special")

#task 23
age=int(input("Enter age : "))
has_id=True
if age>=18 and has_id:
    print("allowed")
else:
    print("not allowed")

#task 24
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
if a>10 and b>10:
        print("both are greater than 10")
else:
    print("not greater than 10")

#task 25
a=int(input("Enter a number"))
if a<0 or a>100:
    print("number is either less than 0 or greater than 100")
else:
    print("number is not less than 0 or greater than 100")


#task 26 


#task 27
a=int(input("Enter a number : "))
if a>10 and a<50:
    print("number is between 10 and 50")
else:
    print("not between 10 and 50")

#task 28 
a=int(input("Enter a number : "))
if a<10 or a>50:
    print("outside range")
else:
    print("inside range")

#task 29
is_student=input("are you student : (yes/no) : ").strip().lower()
if is_student=="yes":
    is_student=True
else:
    print("not allowed")
has_id=input("are you student : (yes/no) : ").strip().lower()
if has_id=="yes":
    has_id=True
else:
    print("not allowed")
has_ticket=input("are you student : (yes/no) : ").strip().lower()
if has_ticket=="yes":
    has_ticket=True
else:
    print("not allowed")










