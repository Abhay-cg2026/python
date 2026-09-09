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
age=int(input("Enter age : "))
if a<0:
    print("invalid age")
elif a<18:
    print("cannot vote")
elif a>=18 and a<120:
    print("can vote")
else:
    print("cannot vote")

