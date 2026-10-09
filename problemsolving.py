# # task 1
# text = input("Enter a string: ")
# ucase = 0
# lcase = 0
# digits = 0
# spaces = 0
# special = 0
# for i in text:
#     if i.isupper():
#         ucase += 1
#     elif i.islower():
#         lcase += 1
#     elif i.isdigit():
#         digits += 1
#     elif i.isspace():
#         spaces += 1
#     else:
#         special += 1

# print(ucase)
# print(lcase)
# print(digits)
# print(spaces)
# print(special)


# str=input("Enter a str : ")
# ucase=0
# lcase=0
# digit=0
# space=0
# spc=0
# for i in str:
#     if i.isupper():
#         ucase+=1
#     elif i.islower():
#         lcase+=1
#     elif i.isdigit():
#         digit+=1
#     elif i.isspace():
#         digit+=1
#     else:
#         spc+=1
# print(ucase)
# print(lcase)
# print(digit)
# print(space)
# print(spc)


# # task 2
# grade=""
# for i in range(1,11):
#     marks=int(input("enter your marks"))
#     if marks>=75:
#         grade="Excellent"
#     elif marks>=50:
#         grade="Good"
#     elif marks>=35:
#         grade="Pass"
#     else:
#         grade="Fail"
#     print(grade)
#     print (marks)


# grade=""
# for i in range(10):
#     marks=int(input("Enter your marks : "))
#     if marks>100 or marks<0:
#         print("Enter valid marks")
#     else:   
#         if 100>=marks>=75:
#             grade="Excellent"
#         elif 75>marks>=50:
#             grade="Good"
#         elif 50>marks>=35:
#             grade="pass"
#         else:
#             grade="fail"
#         print(grade)



# # task 3
# str=input("Enter a str : ").split()
# highest_score=0
# highest_word=0
# for i in str:
#     score=0
#     for j in i:
#         if j in "aeiouAEIOU":
#             score+=2
#         elif j.isalpha():
#             score+=1
#         elif j.isdigit():
#             score+=3
#         else:
#             score+=4
#     if score > highest_score:
#         highest_score=score
#         highest_word=i
# print("Highest word = ",highest_word)
# print("Highest score  = ",highest_score)

# # task 4
# for i in range(5):
#     password=input("Enter password : ")
#     conditions=0
#     lower=False                                        
#     upper=False
#     digit=False
#     special=False
#     if len(password)>=8:
#         conditions+=1
#     for ch in password:
#         if ch.isupper():
#             upper=True
#             conditions+=1
#         elif ch.islower():
#             lower=True
#             conditions+=1
#         elif ch.isdigit():
#             digit=True
#             conditions+=1
#         else:
#             special=True
#             conditions+=1
#     if conditions <= 2:
#         strength = "Weak"
#     elif conditions <= 4:
#         strength = "Medium"
#     else:
#         strength = "Strong"
# print(strength)


# str=input("Enter a string : ")
# sen=str.split()
# short_count=0
# medium_count=0
# long_count=0
# for i in sen:
#     print(i,len(i))
#     if len(i)<=3:
#         short_count+=1
#         print("short")
#     elif len(i)>=6 and len(i)<=6:
#         medium_count+=1
#         print("medium")
#     else:
#         long_count+=1
#         print("long")
# print(short_count)
# print(medium_count)
# print(long_count)

# # task 6
# for i in range(5):
#     num = int(input("Enter a number: "))
#     num1 = str(num)
#     even = 0
#     odd = 0
#     for ch in num1:
#         if int(ch) % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     print("Even =", even)
#     print("Odd =", odd)
#     if even > odd:
#         print("Even occurs more")
#     elif odd > even:
#         print("Odd occurs more")
#     else:
#         print("Equal")

# # task 7
# text = input("Enter a string: ")

# for ch in text:
#     count = 0

#     for x in text:
#         if ch == x:
#             count += 1

# if count > 1:
#     if count == 2:
#         print(ch, "Duplicate")
#     elif count <= 4:
#         print(ch, "Repeated")
#     else:
#         print(ch, "Highly Repeated")

# # task 8
# total = 0

# budget = 0
# regular = 0
# premium = 0
# luxury = 0

# for i in range(8):

#     price = int(input("Enter price: "))

#     total += price

#     if price < 500:
#         print("Budget")
#         budget += 1

#     elif price <= 1999:
#         print("Regular")
#         regular += 1

#     elif price <= 4999:
#         print("Premium")
#         premium += 1

#     else:
#         print("Luxury")
#         luxury += 1

# average = total / 8

# print("Total amount:", total)
# print("Budget products:", budget)
# print("Regular products:", regular)
# print("Premium products:", premium)
# print("Luxury products:", luxury)
# print("Average price:", average)

# # task 9
# name="1Abhay1" #input("enter a string")
# vowel="aeiouAEIOU"
# count=0
# v=0
# c=0
# d=0
# sc=0
# for ch in name:
#     print(ch)
#     print(name.index(ch))
#     if name.index(ch)%2==0:
#         print("even position")
#     else:
#         print("odd position")
#     if ch in vowel:
#         print("chracter is a vowel")
#         v+=1
#     elif ch.isdigit():
#         print("ch is digit")
#         d+=1
#     elif ch.isalpha:
#         print("ch is a consonent")
#         c+=1
#     else:
#         print("ch is special")
#         sc+=1

# print("vowel",v)
# print("consonents",c)
# print("digit",d)
# print("special",sc)

# # task 10
# n=int(input("enter a number"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j%3==0 and j%5==0:
#             print("z",end=" ")
#         elif j%3==0:
#             print("x",end=" ")
#         elif j%5==0:
#             print("Y",end=" ")
#         else:
#             print(j,end=" ")
#     print()

# # task 11
# invalid=False
# for i in range(5):
#     username=input("enter your username...")
#     print("length=",len(username))
#     print("First character=",username[0])
#     countd=0
#     countu=0
#     for ch in username:
#         if ch.isdigit():
#             countd+=1
#         elif ch=="_":
#             countu+=1
#         else:
#             invalid=True
#     print("digit",countd)             
#     print("underscore",countu)

#     if invalid:
#         print("invalid")
#     elif not ch.isdigit() and not ch.isalpha:
#         print("need improvement")
#     else:
#         print("valid")

# # task 12
# for i in range(5):
#     username = input("Enter username: ")
#     digits = 0
#     underscores = 0
#     invalid = False
#     length = len(username)
#     first = username[0]
#     for ch in username:
#         if ch.isdigit():
#             digits += 1
#         elif ch == "_":
#             underscores += 1
#         elif ch.isalpha():
#             pass
#         else:
#             invalid = True
#     if invalid:
#         print("Invalid")
#     elif not first.isalpha():
#         print("Invalid")
#     elif length < 5:
#         print("Needs Improvement")
#     elif length >= 5:
#         print("Valid")
#     print("Length:", length)
#     print("First character:", first)
#     print("Digits:", digits)
#     print("Underscores:", underscores)

# # task 12
# sen=input("type a sentence")
# words=sen.split()
# vowels="aeiouAEIOU"
# vowel=0
# con=0
# for word in words:
#     for ch in word:
#         if ch in vowels:
#             vowel+=1
#         else:
#             con+=1
# print("Vowels=",vowel)
# print("Consonents=",con)
# if vowel>con:
#     print("vowel wins")
# elif vowel==con:
#     print("Tei")
# else:
#     print("Con wins")

# # task 13
# for i in range(6):
#     units=int(input("Enter the no. of units"))
#     bill=0
#     if units<=100:
#         bill=5*units
#     elif units<=200:
#         bill=(5*100)+7*(units-100)
#     elif units<=400:
#         bill=(5*100)+(7*100)+10*(units-100)
#     elif units>400:
#         bill=(5*100)+(7*100)+(10*units)+15*(units-100)
#     print(bill)
#     if bill<1000:
#         print("low")
#     elif bill<=3000 and bill>=1000:
#         print("medium")
#     else:
#         print("high")

# # task 14
# sen=input("enter a sentence")
# words=sen.split()
# vowels="aeiouAEIOU"
# vowel=0
# con=0
# for word in words:
#     for  ch in word:
#         if ch in vowels:
#             vowel+=1
#         elif ch.isalpha():
#             con+=1
# print(vowel)
# print(con)
# if vowel>con:
#     print("vowel heavy")
# elif con>vowel:
#     print("con heavy")
# else:
#     print("balanced")

# # task 15
# matrix = []
# even=0
# odd=0
# positive=0
# negative=0
# zero=0
# largest=0
# for i in range(3):
#     row = []
#     for j in range(3):
#         num = int(input("Enter number: "))
#         row.append(num)
#     matrix.append(row)
# print(matrix)

# n=int(input("Enter number : "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if  j==1  or j==n or i==n :
#             print("*",end=" ")
#         elif n%2==0 and j==(n)/2 and i==(n)/2:
#             print(" *",end="")
#         elif n%2!=0 and j==(n+1)/2 and i==(n+1)/2:
#             print("* ",end="")
#         else:
#             print(" ",end=" ")
#     print()
