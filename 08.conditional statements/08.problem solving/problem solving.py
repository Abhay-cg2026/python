#task 1
a=int(input("Enter a number"))
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")
#task 2
a=int(input("Enter a number : "))
if a>0 and a%2==0:
    print("Positive even")
elif a>0 and a%2==1:
    print("positive odd")
elif a<0 and a%2==0:
    print("negative even")
elif a<0 and a%2==1:
    print("negative odd")
else:
    print("0")
#task 3
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
if a>b:
    print("a is larger")
elif a<b:
    print("b is larger")
elif a==b:
    print("both are equal")
else:
    print("take input correctly")

#task 4
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
c=int(input("Enter a number : "))
if a<b and a<c:
    print("a is smallest")
elif b<a and b<c:
    print("b is smallest")
elif c<a and c<b:
    print("c is smallest")
else:
    ("nothing")

#task 5
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
c=int(input("Enter a number : "))
if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
elif c>a and c>b:
    print("c is largest")
else:
    ("nothing")

#task 6
a=int(input("Enter a number : "))
if a%5==0 and a%11==0:
    print("Divisible by both 5 and 11")
elif a%5==0:
    print("Divisible by 5 only ")
elif a%11==0:
    print("Divisible by 11 only ")
else:
    print("not divisble by 5 or 11 both")

#task 7
a=int(input("Enter a number : "))
if a%3==0 and a%7==0:
    print("Divisible by 3 or 7")
elif a%3==0:
    print("Divisible by 3 only ")
elif a%7==0:
    print("Divisible by 7 only ")
else:
    print("divisible by neither")

#task 8
a=int(input("Enter a marks : "))
if a>100 or a<0:
    print("invalid marks")
elif a>40:
    print("pass")
else:
    print("fail")

#task 9
marks=int(input("Enter marks"))
if marks>90 and marks<100:
    print("A")
elif marks>80 and marks<89:
    print("B")
elif marks>80 and marks<89:
    print("C")
elif marks>80 and marks<89:
    print("D")
elif marks>80 and marks<89:
    print("E")
else:
    print("fail")


#task 10
age=int(input("Enter age : "))
if a<0:
    print("invalid age")
elif a<18:
    print("cannot vote")
elif a>=18 and a<120:
    print("can vote")
else:
    print("cannot vote")

#task 11
year=int(input("Enter year"))
if year%400==0 or year % 4 == 0 and year % 100 != 0:
    print("it is leap year")
else:
    print("not leap year")


#task 12
char=input("Enter a character : ")
if char.isupper():
    print("upper case")
elif char.islower():
    print("lower case")
elif char.isdigit():
    print("digit")
else:
    print("special character")

#task 13
alpha=input("Enter alphabet : ")
if alpha=="a" or alpha=="e" or alpha=="i" or alpha=="o" or alpha=="u":
    print("vowel")
elif alpha.isdigit():
    print("not deifned")
else:
    print("consonents")

#task 14
cost_price=float(input("Enter cost price : "))
selling_price=float(input("Enter selling price : "))
if selling_price>cost_price:
    print("profit")
elif selling_price<cost_price:
    print("loss")
else:
    print("no profit and no loss")

#task 15
cost_price=float(input("Enter cost price : "))
selling_price=float(input("Enter selling price : "))
profit=(selling_price - cost_price)
loss=(cost_price-selling_price)
print("profit",profit)
print("loss",loss)
if profit:
    print(profit / cost_price * 100)
elif loss:
    print(loss / cost_price * 100)
else:
    print("no profit or loss")


#task 16
unit=int(input("Enter electricity reading : "))
if unit>0 and unit<=100:
    bill=(unit*5)
    print(f"Electricity bill is {unit}")
elif unit>100 and unit<=200:
    bill=(100*5+((unit-100)*7))
    print(f"Electricity bill is {unit}")
elif unit>200:
    bill=(100*5+(100*7)+((unit-200)*10))
    print(f"Electricity bill is {unit}")


#task 17
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
c=input("operation you want to do : ")
if c=="addition":
    print(f"addition of {a} and {b} is {a+b}")
elif c=="subtraction":
    print(f"subtraction of {a} and {b} is {a-b}")
elif c=="multiplaction":
    print(f"multiplication of {a} and {b} is {a*b}")
elif c=="division":
        if b==0:
             print("Error: Division by zero is not allowed.")
        else:
            print(f"division of {a} and {b} is {a/b}")
else:
     print("Error: Unsupported operator.")


#task 18

temp=int(input("Enter temp in celsius : "))
if temp<0:
    print("Freezing")
elif temp>0 and temp<15:
    print("Very cold")
elif temp>16 and temp<25:
    print("cold")
elif temp>26 and temp<35:
    print("normal")
else:
    print("hot")

#task 19 

n1=int(input("Enter a number : "))
if n1<0:
    print("negative")
elif n1>0 and n1<10:
    print("number is between 0 and 10")
elif n1>11 and n1<50:
    print("number is between 10 and 50")
elif n1>51 and n1<100:
    print("number is between 51 and 100")
else:
    print("above 100")

#task 20
a=int(input("Enter side A : "))
b=int(input("Enter side B : "))
c=int(input("Enter side C : "))
if a+b>c and a+c>b and b+c>a:
    print("valid triangle")
else:
    print("not valid triangle")

#task 21

a=int(input("Enter side A : "))
b=int(input("Enter side B : "))
c=int(input("Enter side C : "))
if a+b>c and a+c>b and b+c>a:
    print("valid triangle")
    if a==b==c :
        print("Equilateral triangle ")
    elif a==b!=c or a==c!=b or b==c!=a:
        print("isosceles")
    else:
        print("scalen")
else:
    print("invalid triangle")

#task 22
account_balance=int(input("Enter account balance : "))
withdrawal_ammount=int(input("Enter withdrawal balance : "))
if withdrawal_ammount <= 0:
    print("Withdrawal amount must be greater than 0")
elif withdrawal_ammount % 100 != 0:
    print("Withdrawal amount must be divisible by 100")
elif withdrawal_ammount > account_balance:
    print("Insufficient balance")
elif account_balance - withdrawal_ammount < 500:
    print("Cannot withdraw: at least 500 must remain in the account")
else:
    print("Withdrawal successful")
    print("Remaining balance:", account_balance - withdrawal_ammount)

#task 23
crct_username="admin"
crct_pass="python123"
username=input("Enter your username : ")
if username==crct_username:
    password=input("Enter your pass : ")
    if password==crct_pass:
        print("login successful")
    else:
        print("Wrong password")
else:
    print("user not found")
        

#task 24

amount = float(input("Enter purchase amount: "))
 
if amount < 500:
    discount_percent = 0
elif amount < 1000:
    discount_percent = 5
elif amount < 2000:
    discount_percent = 10
elif amount < 5000:
    discount_percent = 15
else:
    discount_percent = 20
 
discount_amount = amount * discount_percent / 100
final_amount = amount - discount_amount
 
print("Original amount:", amount)
print("Discount percentage:", discount_percent)
print("Discount amount:", discount_amount)
print("Final amount:", final_amount)

#task 25
marks1=int(input("Enter marks of sub1 : "))
marks2=int(input("Enter marks of sub2 : "))
marks3=int(input("Enter marks of sub3 : "))
if marks1<0 or marks1>100 or marks2<0 or marks2>100 or marks3<0 or marks3>100 :
    print("no valid marks")
elif marks1<35 and marks2<35 and marks3<35:
    print("fail")
else:
    average=(marks1+marks2+marks3)/3   
    if average>=75:
        print("distinction")
    elif average>=60 and average<75:
        print("First class")
    elif average>=50 and average<60:
        print("Second class")
    else:
        print("pass")

#task 26
day=int(input("Enter day : "))
month=int(input("Enter month : "))
year=int(input("Enter year : "))
is_leap = False
if year % 400 == 0:
    is_leap = True
elif year % 4 == 0 and year % 100 != 0:
    is_leap = True

if month<0 and month>12:
    print("invalid")
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    if day>0 and day<=31:
        print("valid")
    else:
        print("invalid")
elif month==4 or month==6 or month==9 or month==11:
    if day>0 and day<=30:
        print("valid")
    else:
        print("invalid")
else:
    if is_leap:
        if day>0 and day<=29:
            print("valid")
        else:
            print("invalid")
    else:
        if day>0 and day<=28:
            print("valid")
        else:
            print("not valid")


#task 27
hours=int(input("Enter hour : "))
mins=int(input("Enter minutes : "))
secs=int(input("Enter seconds : "))
if hours>0 and hours<=23:
    if mins>0 and mins<60:
        if secs>0 and secs<60:
            print("valid time ")  
else:
    print("invalid time ")      

#task 28
name1=input("Enter name : ")
person1=int(input("Enter age : "))
name2=input("Enter name : ")
person2=int(input("Enter age : "))
name3=input("Enter name : ")
person3=int(input("Enter age : "))
if person1<person2 and person1<person3:
    print(f" {name1} ,{person1} is youngest")
elif person2<person1 and person2<person3:
    print(f"{name2},{person2} is youngest")
elif person3<person1 and person3<person2:
    print(f"{name3},{person3} is youngest")
elif person3==person2==person1 :
    print("All three are of same age")
elif person1==person2 or person1==person3 or person2==person3:
    print("there are two persons of same age")
else:
    print("invalid syntax")

#task 29
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
c=int(input("Enter a number : "))
if(b > a and a > c) or (c > a and a > b):
    second_largest = a
elif (a > b and b > c) or (c > b and b > a):
    Second_largest = b
else:
    second_largest = c
print(f"The second-largest number is:{Second_largest}")

#task 30 
age=int(input("Enter your age : "))
marks=int(input("Enter your marks : "))
Attendance=int(input("Enter your Attend. : "))
family_income=int(input("Enter your family income : "))
age = age>=18 and age<=25
marks=marks>=85
Attendance= Attendance>=75
income=family_income<=300000
if age and marks and Attendance and income:
    print("Scholarship approved")
else:
    print("Scholarship rejected")
    if not age:
        print("Reason: Age not between 18 and 25")
    if not marks:
        print("Reason: Marks below 85")
    if not Attendance:
        print("Reason: Attendance below 75%")
    if not income:
        print("Reason: Family income above 300000")

