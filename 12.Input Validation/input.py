# Part A

# # task 1
# while True:
#     marks=int(input("Enter marks between 0 to 100 : "))
#     if 0<marks<100:
#         print(marks)
#         break
#     else:
#         print("Enter again")

# # task 2
# while True:
#     a=int(input("Enter numbers : "))
#     if a>0:
#         print("positve",a)
#         break

# # task 3
# while True:
#     age=int(input("Enter age : "))
#     if 18<=age<=120:
#         print("Valid Age")
#         break
#     else:
#         print("Enter valid age")


# # task 4
# while True:
#     menu=int(input("1.View profile\n2.Edit profile\n3.Settings\n4.Exit : "))
#     if menu==1:
#         print("View profile")
#     elif menu==2:
#         print("Edit profile")
#     elif menu==3:
#         print("Settings")
#     elif menu==4:
#         print("Exit")
#         break
#     else:
#         print("Enter value again")  

# # task 5
# while True:
#     password=input("Enter password : ").strip().lower()
#     if len(password)<8:
#         print("Enter again")
#     else:
#         print("Correct password")
#         break

# # task 6
# while True:
#     temp=float(input("Enter temperature  : "))
#     if temp>=40 or temp<=-25:
#         print("Enter again")
#     else:
#         print("temp=",temp)
#         break


# # task 7
# bank_balance=5000
# while True:
#     withdrawal_amnt=int(input("Enter widthdrawal amount : "))
#     Updated_amnt=bank_balance-withdrawal_amnt
#     if withdrawal_amnt>bank_balance or withdrawal_amnt<=0 :
#         print("Withdrawal Rejected")
#     else:
#         print("Remaining Amnt=",Updated_amnt) 
#         break

# # task 8
# while True:
#     u_name=input("Enter Username : ").strip().lower()
#     count=0
#     if len(u_name)<5 or  u_name== " " or " " in u_name:
#         print("Enter again")
#     else:
#         print("User name = ",u_name)
#         break
        

# # task 9
# while True:
#     num=int(input("Enter a number : "))
#     if num%3!=0 or num%5!=0:
#         print("Enter again")
#     else:
#         print(num,"Accepted")
#         break

# # task 10
# pin=2468

# for i in range(3):
#     crrctpin=int(input("Enter your pin : "))
#     if pin!=crrctpin:
#         print("Incorrect pin")
#     else:
#         print("Correct pin")
#         break

# # task 11
# while True:
#     number=int(input("Enter integer : "))
#     if number<10 or number>50:
#         print("Enter again")
#     else:
#         if number%2==0:
#             print("Even")
#         else: 
#             print("odd")
#         break

# # task 12
# balance=2000
# while True:
#     deposit=int(input("Enter amount you want to deposite : "))
#     new_balance=balance+deposit
#     if deposit<=0:
#         print("Enter again")
#     else:
#         print("new balance= ",new_balance)
#         break

# # task 13
# while True:
#     a=int(input("Enter integer : "))
#     if a>0 and a<100:
#         print(a)
#     elif a==0:
#         print("Loop ended")
#         break
#     else:
#         print("Enter again")

# # task 14
# while True:
#     marks=int(input("Enter your marks : "))
#     if marks>=75 and marks<=100:
#         print("Distinction")
#     elif marks>=60 and marks<75:
#         print("First class")
#     elif marks>=35 and marks<60:
#         print("pass")
#     elif marks<35 and marks>=0 :
#         print("Fail")
#     else: 
#         print("Invalid marks")

# # task 15
# while True:
#     user_name=input("Enter your username : ").strip()
#     password=input("Enter your password : ").strip()
#     if len(user_name)<5 or " " in user_name and len(password)<8 or " " in password:
#             print("Both username and password are wrong") 
#     elif len(user_name)<5 or " " in user_name:
#         print("Wrong username")
#     elif len(password)<8 or " " in password:
#         print("Wrong password")
#     elif len(user_name)<5 or " " in user_name or len(password)<8 or " " in password:
#         print(" both username and password are wrong") 
#     else:
#         print("login succesful")
#         break


# # task 16
# a=int(input("Enter a number : "))
# b=int(input("Enter a number : "))
# while True:
#     operation=int(input("1.+\n2.-\n3.*\n4./\nEnter operation you want to run : "))
#     if operation!=1 and operation!=2 and operation!=3 and operation!=4 :
#             print("Enter operation again")
#     elif operation==1:
#         print(a+b)
#         break
#     elif operation==2:
#         print(a-b)
#         break
#     elif operation==3:
#         print(a*b)
#         break
#     elif operation==4:
#         if b!=0:
#             print(a/b)
#         else:
#             print("enter again")
#             b=int(input("Enter number again : "))
#             print(a/b)
#         break 
                                                                                                                                                   
# # task 17
# balance=10000
# while True:
#     operation=int(input("1.Check balance\n2.Deposit money\n3.Withdraw money\n4.Exit\nWhat operation do you want to perform : "))
#     if operation!=1 and operation!=2 and operation!=3 and operation!=4:
#         print("Invalid operation")
#     elif operation==1:
#         print(balance)
#     elif operation==2:
#         deposit=int(input("Enter money you want to deposit : "))
#         if deposit<=0:
#             print("Money cant be deposited")
#         else:
#             balance=balance+deposit
#             print(balance)
#     elif operation==3:
#         withdraw=int(input("Enter money you want to withdraw : "))
#         if withdraw>balance or withdraw<=0:
#             print("Money cant be withdrawed")
#         else:
#             balance=balance-withdraw
#             print(balance)
#     if operation==4:
#         print("Exiting")
#         break

# # task 18
# leap=366
# while True:
#     month=int(input("Enter month : "))
#     if month<1 and month>12:
#         print("Enter again")
#     else:
#         if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#             day=int(input("Enter day : "))
#             if day<1 or day>31:
#                 print("invalid day")
#             else:
#                 print(f"{day}/{month}")
#                 break
#         elif month==2:
#             if month is leap:
#                 day=int(input("Enter day : "))
#                 if day<1 or day>30:
#                     print("invalid day")
#                 else:
#                     print(f"{day}/{month}")
#                     break
#             else:
#                 day=int(input("Enter day : "))
#                 if day<1 or day>29:
#                     print("invalid day")
#                 else:
#                     print(f"{day}/{month}")
#                     break
#         else:
#             day=int(input("Enter day : "))
#             if day<1 or day>30:
#                 print("invalid day")
#             else:
#                 print(f"{day}/{month}")
#                 break


# # task 19
# while True:
#     quant=int(input("Enter the quantity of the product : "))
#     if quant<=0:
#         print("Invalid Quantity")
#     else:
#         price=float(input("Enter the price of the product : "))
#         if price<=0:
#             print("Invalid Price")
#         else:
#             print(f"total price is : {quant*price}")
#             break


# task 20
# a=int(input("Enter any number between 1 to 20 : "))
# while a<1 or a>20:
#     print("invalid input")
#     a=int(input("Enter number 1 to 20 : "))
# sum=0
# i=1
# while i<=a:
#     number=int(input("Enter number : "))
#     sum+=number
#     i+=1
# avg=sum/a
# print(avg)

# # task 21
# while True:
#     a=input("Enter password : ").strip()
#     if len(a)<8:
#         print("invalid input")
#     else:
#         for c in a:
#             if c.isupper():
#                 for c in a:
#                     if c.isdigit():
#                         print("correct pass")
#                         break
#                     else:
#                         print("invalid input")
#             else:
#                 print("invalid input")
#                 break


# # task 22
# password = input("Enter your password: ")
# while len(password) < 8 or password.islower() or password.isupper() or password.isalpha() or " " in password:
#     print("Password does not meet the following rules:")
#     if len(password) < 8:
#         print("Password must contain at least 8 characters.")
#     upper=lower=digit=space=False
#     for ch in password:
#         if ch >= "A" and ch <= "Z":
#             upper = True
#         if ch >= "a" and ch <= "z":
#             lower = True
#         if ch >= "0" and ch <= "9":
#             digit = True
#         if ch == " ":
#             space = True
#     if upper == False:
#         print("Password must contain at least one uppercase letter.")
#     if lower == False:
#         print("Password must contain at least one lowercase letter.")
#     if digit == False:
#         print("Password must contain at least one digit.")
#     if space == True:
#         print("Password must not contain whitespace.")
#     password = input("Enter your password again: ")
# print("Password accepted!")

# # task 23
# number=int(input("Enter any integer from 1 to 10:"))
# while number>10 or number<0:
#     print("Oops!The Selected Integer is Out Of Range\nPlease Try Again")
#     number=int(input("Re-enter any integer from 1 to 10:"))
# print("Integer is in Range")
                    
# # task 24
# score1=int(input("Enter the First Score:"))
# score2=int(input("Enter the Second Score:"))
# score3=int(input("Enter the Third Score:"))
# while score1<0 or score1>100 or score2<0 or score2>100 or score3<0 or score3>100:
#     print("Either Score1,score2 or score3 is Out of Range")
#     score1=int(input("Enter the First Score:"))
#     score2=int(input("Enter the Second Score:"))
#     score3=int(input("Enter the Third Score:"))
        

        