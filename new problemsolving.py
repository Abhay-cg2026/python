# level 1(basic)
# task 1(Even or odd)
# a=int(input("Enter a number : "))
# if a%2==0:
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")


# # task 2(maximum of two numbers)
# a=int(input("Enter a number : "))
# b=int(input("Enter a number : "))
# if a>b:
#     print(f"{a} is greater")
# elif b>a:
#     print(f"{b} is greater")
# else:
#     print("Both are equal")


# # task 3(maximum of three numbers))
# a=int(input("Enter a number : "))
# b=int(input("Enter a number : "))
# c=int(input("Enter a number : "))
# if a>b and a>c:
#     print(f"{a} is greater")
# elif b>a and b>c:
#     print(f"{b} is greater")
# elif c>a and c>b:
#     print(f"{c} is greater")
# elif a==b==c:
#     print("All are equal")
# else:
#     print("Any two numbers are equal")

# # task 4(+,- and 0)
# a=int(input("Enter a number : "))
# if a >0:
#     print("positve")
# elif a<0:
#     print("negative")
# else:
#     print("zero")


# # task 5(age group)
# age=int(input("Enter a number : "))
# if 12>=age>0:
#     print(age,"Child")
# elif 19>=age>12:
#     print(age,"Teenager")
# elif age>=20:
#     print(age,"Adult")
# else:
#     print("invalid age")

# # task 6
# marks=int(input("Enter marks : "))
# Grade=""
# if 100>marks>=90:
#     Grade="A"
# elif 90>marks>=80:
#     Grade="B"
# elif 80>marks>=70:
#     Grade="C"
# elif 70>marks>=60:
#     Grade="D"
# elif 60>marks>=0:
#     Grade="F"
# else:
#     print("Enter valid marks")

# print(Grade)

# # task 7(div by 5)
# num=int(input("Enter a number : "))
# if num%5==0:
#     print("Divisible by 5")
# else:
#     print("not divisible by 5")

# # task 8(div by 3 and 5)
# num=int(input("Enter a number : "))
# if num%5==0 and num%3==0:
#     print("Divisible by 5 and 3")
# else:
#     print("not divisible by both")

# # task 9(leap year simple rule)
# year=int(input("Enter year : "))
# if year%4==0:
#     print("leap year")
# else:
#     print("not leap year")

# # task 10
# num=int(input("Enter a number : "))
# if num>=10 and num<=50:
#     print("in range")
# else:
#     print("not in range")



# # level 2
# # task 11
# for i in range(1,10+1):
#     print(i,end=" ")

# # task 12
# n=int(input("Enter number : "))
# for i in range(1,n+1):
#     print(i,end=" ")

# # task 13
# n=int(input("Enter number : "))
# for i in range(1,n+1):
#     if i%2==0:
#         print(i,end=" ")

# # task 14
# n=int(input("Enter number : "))
# for i in range(1,n+1):
#     if i%2==0+1:
#         print(i,end=" ")

# # task 15
# n=int(input("Enter number : "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# # task 16
# n=int(input("Enter number : "))
# multi=1
# for i in range(1,n+1):
#     multi*=i
# print(multi)

# # task 17
# n=int(input("Enter number : "))
# i=1
# while i<=10:
#     print(n*i,end=" ")
#     i+=1

# # task 18
# n=int(input("Enter number : "))
# count=0
# for i in range(1,n):
#     if i%3==0:
#         count+=1
# print(count)

# # task 19
# n=int(input("Enter number : "))
# multi=1
# i=1
# while i<=n:
#     multi*=i
#     i+=1
# print(multi)

# # task 20
# n=int(input("Enter number : "))
# i=1
# while i<=n:
#     print(7*i,end=" ")
#     i+=1
    

# level 3
# # task 21
# a=int(input("Enter a number : "))
# count=0
# for i in str(a):
#     if i.isdigit():
#         count+=1
# print(count)


# # task 22
# n=int(input("Enter number : "))
# total=0
# while n>0:
#     digit=n%10
#     total=total+digit
#     n=n//10
# print("sum",total)


# # task 23
# n=int(input("Enter number : "))
# multi=1
# while n>0:
#     digit=n%10
#     multi=multi*digit
#     n=n//10
# print("Product",multi)

# # task 24
# n=int(input("Enter number : "))
# reverse=0
# while n>0:
#     digit=n%10
#     reverse=reverse*10+digit
#     n=n//10
# print(reverse)


# # task 25
# str=input("Enter a string : ")
# i=0
# j=len(str)-1
# flag=True
# while i<j:
#     if str[i]!=str[j]:
#         flag=False
#         break
#     i+=1
#     j-=1
# if flag==True:
#     print("is Palindrome")
# else:
#     print("not palindrome")


# # task 26
# a=int(input("Enter a number : "))
# count=0
# for i in range(1,a+1):
#     if a%i==0:
#         count+=1
# if count==2:
#     print("is prime")
# else:
#     print("not a prime number")



