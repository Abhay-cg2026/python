# # task 1
# IPO:
#Input: price, y
#Process: total = price + y
#Output: total

# ALGORITHM:
#Start
#Read price and y
#Calculate total = price + y
#Print total
#Stop

# a=float(input("Enter a number : "))
# b=float(input("Enter a number : "))
# print(f"sum of {a} and {b} is {a+b}")

# #task 2
# IPO:
#Input: n
#Process: Check n % 2 == 0
#Output: "Even" or "Odd"
#
# ALGORITHM:
#   1. Start
#   2. Read n
#   3. If n % 2 == 0, print "Even"
#   4. Else, print "Odd"
#   5. Stop


# how=int(input("Enter how many times you want to run : "))
# for i in range(how):
#     n=int(int(input("Enter a number : ")))
#     if n%2==0:
#         print("Even")
#     else:
#         print("odd")


# # task 3
# IPO:
#   Input: price, y, z
#   Process: Compare price, y, z to find the largest
#   Output: Largest number
#
# ALGORITHM:
#   1. Start
#   2. Read a, b, c
#   3. If a > b and a > c, print a
#   4. Elif b > a and b > c, print c
#   5. Elif c>a and c>b print c
#   6. Elif a == b == c ,  print all equal
#   7. Else two numbers are equal
#   8. Stop

# how=int(input("Enter how many times you want to run : "))
# for i in range(how):
#     a=int(input("Enter number : "))
#     b=int(input("Enter number : "))
#     c=int(input("Enter number : "))
#     if a>b and a>c:
#         print(f"{a}")
#     elif b>a and b>c:
#         print(f"{b}")
#     elif c>a and c>b:
#         print(f"{c}")
#     elif a==b==c:
#         print("All are equal")
#     else:
#         print("Two numbers are equall")

# # task 4
# IPO :
#   Input: age (age)
#   Process: Check age >= 18
#   Output: "Eligible" or "Not Eligible"
#
# ALGORITHM:
#   1. Start
#   2. Read price
#   3. If age >= 18, print "Eligible"
#   4. Else, print "Not Eligible"
#   5. Stop

# for i in range(5):
#     age=int(input("Enter age : "))
#     if age>=18:
#         print("Eligible to vote ")
#     else:
#         print("not eligible to vote ")

# # task 5
# IPO :
#   Input: price (price)
#   Process: If price >= 2000, final_price = price - (price * 0.20), else final_price = price
#   Output: final_price
#
# ALGORITHM:
#   1. Start
#   2. Read price
#   3. total_price=addtion of all prices
#   3. discount=total_price*20/100
#   3. If price >= 2000, final_price = totalprice - discount
#   4. Else, final_price = price
#   5. Print final_price
#   6. Stop

# total_price=0
# final_price=0
# discount=0
# for i in range(5):
#     price=int(input("Enter price : "))
#     total_price+=price
#     if total_price>=2000:
#         discount=total_price*20/100
#         final_price=total_price-discount
# else:
#     print("no discount")

# print(total_price)
# print(discount)
# print(final_price)

# # task 6
# IPO :
#   Input: x, y, z (marks)
#   Process: avg = (x + y + z) / 3, check avg >= 40
#   Output: "Pass" or "Fail"
#
# ALGORITHM:
#   1. Start
#   2. Read x, y, z
#   3. avg = (x + y + z) / 3
#   4. If avg >= 40, print "Pass"
#   5. Else, print "Fail"
#   6. Stop

# total_marks=0
# for i in range(3):
#     sub=int(input("Enter marks : "))
#     total_marks+=sub
#     average=total_marks/3
# if average>=40:
#     print("pass")
# else:
#     print("fail")
# print(total_marks)
# print(average)





    

