
# a=int(input("Enter number : "))
# b=int(input("Enter number : "))
# choice=input("""Enter operation you want to run :
#                 1.add
#                 2.sub
#                 3.multi
#                 4.div
#                 5.floordiv
#                 6.mod
#                 7.exit
#                 : """)
# while choice!=7:
#     match choice:
#         case "add":
#             print(a+b)
#         case "sub":
#             print(a-b)
#         case "multi":
#             print(a*b)
#         case "div":
#             if b!=0:
#                 print(a/b)
#             else:
#                 print("not possible")
#         case "floor":
#             if b!=0:
#                     print(a//b)
#             else:
#                 print("not possible")
#         case "mod":
#             print(a%b)
#         case _:
#             print("invalid output")
#     choice=input("""Enter operation you want to run :
#                 1.add
#                 2.sub
#                 3.multi
#                 4.div
#                 5.floordiv
#                 6.mod
#                 7.exit
#                 : """)
#     print("Exited") 
            

# num=int(input("enter a number : "))
# choice=input("""Enter choice : 
#                 1.even
#                 2.odd
#                 3.prime
#                  :""")
# count=0 
# match choice:
#     case "even":
#         if num%2==0:
#             print("even")
#         else:
#             print("not even")
#     case "odd":
#         if num%2==1:
#             print("odd")
#         else:
#             print("not odd")
#     case "prime":
#         for i in range(1,num+1): 
#             if num%i==0:
#                 count+=1
#             if count==2:
#                 print("is prime")
#             else:
#                 print("not a prime number")   

# day=5
# match day:
#     case 1|2|3|4|5:
#         print("Weekday")
#     case 6|7:
#         print("Weekend")
#     case _:
#         print("Enter valid day")

# day=int(input("Enter day"))
# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday")
#     case 6|7:
#         print("Weekend")
#     case _:
#         print("Enter valid day")

# marks=int(input("Enter marks : "))
# match marks:
#     case x if x>=90:
#         print("A")
#     case x if x>=75:
#             print("B")
#     case x if x>=60:
#             print("C")
#     case x if x>=40:
#             print("D")
#     case _:
#             print("fail")


# company = int(input("""Enter Gas Company: 
#                     1. HP Gas
#                     2. Bharat Gas
#                     3. Indane
#                     : """))
# match company:
#     case 1:
#         print("HP Gas selected")

#         choice = int(input("""1. Book Cylinder
# 2. Check Booking
# 3. Cancel Booking
# : """))

#         match choice:
#             case 1:
#                 print("HP Gas cylinder booked")
#             case 2:
#                 print("HP Gas booking checked")
#             case 3:
#                 print("HP Gas booking cancelled")
#             case _:
#                 print("Invalid choice")

#     case 2:
#         print("Bharat Gas selected")

#         choice = int(input("""1. Book Cylinder
# 2. Check Booking
# 3. Cancel Booking
# : """))

#         match choice:
#             case 1:
#                 print("Bharat Gas cylinder booked")
#             case 2:
#                 print("Bharat Gas booking checked")
#             case 3:
#                 print("Bharat Gas booking cancelled")
#             case _:
#                 print("Invalid choice")

#     case 3:
#         print("Indane selected")

#         choice = int(input("""1. Book Cylinder
# 2. Check Booking
# 3. Cancel Booking 
# : """))

#         match choice:
#             case 1:
#                 print("Indane cylinder booked")
#             case 2:
#                 print("Indane booking checked")
#             case 3:
#                 print("Indane booking cancelled")
#             case _:
#                 print("Invalid choice")

#     case _:
#         print("Invalid gas company")


# # Q1. Food Ordering System

# choice = int(input("Enter Any Serial Number: "))

# match choice:
#     case 1:
#         print("You selected Pizza")
#     case 2:
#         print("You selected Burger")
#     case 3:
#         print("You selected Pasta")
#     case 4:
#         print("You selected Sandwich")
#     case _:
#         print("Invalid Menu Choice")


# # Q2. Mobile Settings

# choice = int(input("Enter Any Serial Number: "))

# match choice:
#     case 1:
#         print("Wi-Fi Selected")
#     case 2:
#         print("Bluetooth Selected")
#     case 3:
#         print("Mobile Data Selected")
#     case 4:
#         print("Airplane Mode Selected")
#     case 5:
#         print("Exit Selected")
#     case _:
#         print("Invalid Setting")


# # Q3. ATM Main Menu

# choice = int(input("Enter Any Serial Number: "))

# match choice:
#     case 1:
#         print("Check Balance Selected")
#     case 2:
#         print("Withdraw Money Selected")
#     case 3:
#         print("Deposit Money Selected")
#     case 4:
#         print("Change PIN Selected")
#     case 5:
#         print("Exit Selected")
#     case _:
#         print("Invalid Choice")


# # Q4. Traffic Signal

# choice = int(input("Enter Signal Number (1-Red, 2-Yellow, 3-Green): "))

# match choice:
#     case 1:
#         print("Stop")
#     case 2:
#         print("Wait")
#     case 3:
#         print("Go")
#     case _:
#         print("Invalid Signal")


# # Q5. Student Portal

# choice = int(input("Enter Any Serial Number: "))

# match choice:
#     case 1:
#         print("Opening Profile")
#     case 2:
#         print("Opening Courses")
#     case 3:
#         print("Opening Marks")
#     case 4:
#         print("Opening Attendance")
#     case 5:
#         print("Logging Out")
#     case _:
#         print("Invalid Choice")


# # Q6. Online Shopping Menu

# choice = int(input("Enter Any Serial Number: "))

# match choice:
#     case 1:
#         print("Opening Electronics")
#     case 2:
#         print("Opening Clothing")
#     case 3:
#         print("Opening Books")
#     case 4:
#         print("Opening Grocery")
#     case 5:
#         print("Exit Selected")
#     case _:
#         print("Invalid Category")


# # Q7. Banking Service Selection

# choice = int(input("Enter Any Serial Number: "))

# match choice:
#     case 1:
#         print("Opening Account Balance")
#     case 2:
#         print("Opening Mini Statement")
#     case 3:
#         print("Opening Fund Transfer")
#     case 4:
#         print("Opening Bill Payment")
#     case 5:
#         print("Opening Customer Support")
#     case _:
#         print("Invalid Service")


# # Q8. Movie Ticket Booking

# choice = int(input("Enter Any Serial Number: "))

# match choice:
#     case 1:
#         print("Morning Show Selected")
#     case 2:
#         print("Afternoon Show Selected")
#     case 3:
#         print("Evening Show Selected")
#     case 4:
#         print("Night Show Selected")
#     case _:
#         print("Invalid Show")


# # Q9. Weather Advice

# choice = int(input("Enter Weather Number (1-Sunny, 2-Rainy, 3-Cloudy, 4-Snowy): "))

# match choice:
#     case 1:
#         print("Wear sunglasses")
#     case 2:
#         print("Carry an umbrella")
#     case 3:
#         print("Weather may change")
#     case 4:
#         print("Wear warm clothes")
#     case _:
#         print("Unknown Weather")


# # Q10. Payment Method

# choice = int(input("Enter Payment Number (1-UPI, 2-Card, 3-Cash, 4-Wallet): "))

# match choice:
#     case 1:
#         print("UPI Payment Selected")
#     case 2:
#         print("Card Payment Selected")
#     case 3:
#         print("Cash Payment Selected")
#     case 4:
#         print("Wallet Payment Selected")
#     case _:
#         print("Invalid Payment Method")


# # Q11. File Type Detector

# choice = int(input("Enter File Number (1-PDF, 2-JPG, 3-PNG, 4-MP3, 5-MP4): "))

# match choice:
#     case 1:
#         print("Document File")
#     case 2:
#         print("Image File")
#     case 3:
#         print("Image File")
#     case 4:
#         print("Audio File")
#     case 5:
#         print("Video File")
#     case _:
#         print("Unknown File Type")


# # Q12. User Role

# choice = int(input("Enter Role Number (1-Admin, 2-Teacher, 3-Student, 4-Guest): "))

# match choice:
#     case 1:
#         print("Full Access")
#     case 2:
#         print("Teacher Dashboard")
#     case 3:
#         print("Student Dashboard")
#     case 4:
#         print("Limited Access")
#     case _:
#         print("Invalid Role")


# # Q13. Weekday or Weekend

# day = int(input("Enter Day Number: "))

# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday")
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Invalid Day")


# # Q14. Customer Support Priority

# priority = int(input("Enter Priority Number: "))

# match priority:
#     case 1 | 2:
#         print("Normal Priority")
#     case 3 | 4:
#         print("Urgent Priority")
#     case _:
#         print("Invalid Priority")


# # Q15. Store Discount Category

# level = int(input("Enter Membership Number: "))

# match level:
#     case 1 | 2:
#         print("Basic Membership")
#     case 3 | 4:
#         print("Premium Membership")
#     case _:
#         print("Invalid Membership Level")


# # Q16. University Portal

# user_type = int(input("Enter User Type (1-Student, 2-Teacher): "))

# match user_type:
#     case 1:
#         option = int(input("Enter Option: "))

#         match option:
#             case 1:
#                 print("Opening Student Courses")
#             case 2:
#                 print("Opening Student Marks")
#             case 3:
#                 print("Opening Student Attendance")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         option = int(input("Enter Option: "))

#         match option:
#             case 1:
#                 print("Opening Teacher Students")
#             case 2:
#                 print("Entering Marks")
#             case 3:
#                 print("Opening Teacher Attendance")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid User Type")


# # Q17. ATM with Account Type

# account = int(input("Enter Account Type (1-Savings, 2-Current): "))

# match account:
#     case 1:
#         print("Savings Account")
#         operation = int(input("Enter Operation: "))

#         match operation:
#             case 1:
#                 print("Check Balance Selected")
#             case 2:
#                 print("Deposit Selected")
#             case 3:
#                 print("Withdraw Selected")
#             case _:
#                 print("Invalid Operation")

#     case 2:
#         print("Current Account")
#         operation = int(input("Enter Operation: "))

#         match operation:
#             case 1:
#                 print("Check Balance Selected")
#             case 2:
#                 print("Deposit Selected")
#             case 3:
#                 print("Withdraw Selected")
#             case _:
#                 print("Invalid Operation")

#     case _:
#         print("Invalid Account Type")


# # Q18. E-Commerce Application

# category = int(input("Enter Category (1-Electronics, 2-Clothing): "))

# match category:
#     case 1:
#         product = int(input("Enter Product Number: "))

#         match product:
#             case 1:
#                 print("Mobile Selected")
#             case 2:
#                 print("Laptop Selected")
#             case 3:
#                 print("Headphones Selected")
#             case _:
#                 print("Invalid Product")

#     case 2:
#         product = int(input("Enter Product Number: "))

#         match product:
#             case 1:
#                 print("Shirt Selected")
#             case 2:
#                 print("Jeans Selected")
#             case 3:
#                 print("Shoes Selected")
#             case _:
#                 print("Invalid Product")

#     case _:
#         print("Invalid Category")


# # Q19. Food Delivery Application

# category = int(input("Enter Category (1-Vegetarian, 2-Non-Vegetarian): "))

# match category:
#     case 1:
#         food = int(input("Enter Food Number: "))

#         match food:
#             case 1:
#                 print("Paneer Selected")
#             case 2:
#                 print("Dal Selected")
#             case 3:
#                 print("Veg Biryani Selected")
#             case _:
#                 print("Invalid Food")

#     case 2:
#         food = int(input("Enter Food Number: "))

#         match food:
#             case 1:
#                 print("Chicken Biryani Selected")
#             case 2:
#                 print("Chicken Curry Selected")
#             case 3:
#                 print("Fish Fry Selected")
#             case _:
#                 print("Invalid Food")

#     case _:
#         print("Invalid Category")


# # Q20. Simple Calculator

# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# choice = int(input("Enter Operator Number (1-Add, 2-Subtract, 3-Multiply, 4-Divide): "))

# match choice:
#     case 1:
#         print("Result =", num1 + num2)
#     case 2:
#         print("Result =", num1 - num2)
#     case 3:
#         print("Result =", num1 * num2)
#     case 4:
#         if num2 != 0:
#             print("Result =", num1 / num2)
#         else:
#             print("Cannot Divide By Zero")
#     case _:
#         print("Invalid Operator")


# # Q21. Temperature Converter

# choice = int(input("Enter Choice (1-Celsius to Fahrenheit, 2-Fahrenheit to Celsius): "))
# temperature = int(input("Enter Temperature: "))

# match choice:
#     case 1:
#         result = (temperature * 9 / 5) + 32
#         print("Temperature =", result, "F")
#     case 2:
#         result = (temperature - 32) * 5 / 9
#         print("Temperature =", result, "C")
#     case _:
#         print("Invalid Choice")


# # Q22. Unit Converter

# choice = int(input("Enter Choice (1-KM to M, 2-M to KM, 3-KG to G, 4-G to KG): "))
# value = int(input("Enter Value: "))

# match choice:
#     case 1:
#         print(value * 1000, "meters")
#     case 2:
#         print(value / 1000, "kilometers")
#     case 3:
#         print(value * 1000, "grams")
#     case 4:
#         print(value / 1000, "kilograms")
#     case _:
#         print("Invalid Choice")


# # Q23. ATM Withdrawal

# account = int(input("Enter Account Type (1-Savings, 2-Current): "))

# match account:
#     case 1:
#         print("Savings Account")
#         amount = int(input("Enter Withdrawal Amount: "))

#         if amount > 0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid Amount")

#     case 2:
#         print("Current Account")
#         amount = int(input("Enter Withdrawal Amount: "))

#         if amount > 0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid Amount")

#     case _:
#         print("Invalid Account Type")

# # task 24
# exam = int(input("Enter your choice (1-start exam, 2-View result,3-exit): "))
# match exam:
#     case 1:
#         print("Start exam")
#         age=int(input("Enter your age : "))
#         if age >= 18:
#             print("you can start the exam")
#         else:
#             print("not eligible to give exam")
#     case 2:
#         print("View result")
#     case _:
#         print("Exit")

# # task 25
# ticket = int(input("Enter your choice (1-Regular, 2-Premium ,3-VIP  ): "))
# match ticket:
#     case 1:
#         age=int(input("Enter your age : "))
#         if age<5:
#             print("Free entry")
#         else:
#             print("Regular")
#     case 2:
#             age=int(input("Enter your age : "))
#             if age<5:
#                 print("Free entry")
#             else:
#                 print("Premium")
#     case 3:
#             age=int(input("Enter your age : "))
#             if age<5:
#                 print("Free entry")
#             else:
#                 print("VIP")
#     case _:
#           print("Enter valid iteration")

# # task 26
# control = int(input("Enter your choice (1-Light, 2-Fan , 3-AC , 4-TV  ): "))
# match control:
#     case 1:
#         print("Light Controller Opened")
#     case 2:
#         print("Fan Controller Opened")
#     case 3:
#         print("AC Controller Opened")
#     case 4:
#         print("TV Controller Opened")
#     case _:
#         print("Enter valid input")

# task 27


# Depart= int(input("Enter your choice (1-General medicie, 2-Cardiology , 3-Orthopedics , 4-Pediatrics , 5-Emergency  ): "))
# match Depart:
#     case 1:
#         print("General medicie")
#     case 2:
#         print("Cardiology")
#     case 3:
#         print("Orthopedics")
#     case 4:
#         print("Pediatrics")
#     case 5:
#         print("Emergency ")
#     case _:
#         print("Invalid Department")

# # task 28
# Ticket= int(input("Enter your choice (1-Book Ticket, 2-Cancel Ticket , 3-Check PNR , 4-Train Schedule , 5-Exit  ): "))
# match Ticket:
#     case 1:
#         print("Book Ticket")
#     case 2:
#         print("Cancel Ticket")
#     case 3:
#         print("Check PNR")
#     case 4:
#         print("Train Schedule")
#     case 5:
#         print("Exit ")
#     case _:
#         print("Invalid input")

# # task 29
# lib= int(input("Enter your choice (1-Search book, 2-Issue Book , 3-Return Book , 4-View Issued Book , 5-Exit  ): "))
# match lib:
#     case 1:
#         print("Search book")
#     case 2:
#         print("Issue Book ")
#     case 3:
#         print("Return Book ")
#     case 4:
#         print("View Issued Book")
#     case 5:
#         print("Exit ")
#     case _:
#         print("Invalid Department")


# task 30

# order=int(input("1.Placed\n2.Confirmed\n3.Preparing\n4.Out Of Delivery\nDelivered\nCancelled\nEnter  the Order Status:- "))

# match order:
#     case 1:
#         print("Your Order is Placed")
#     case 2:
#         print("Your Order is Confirmed")
#     case 3:
#         print("Your Ortder is Preparing")
#     case 4:
#         print("Your Order is Delivered")
#     case 5:
#         print("your order is cancelled")
#     case  _:
#         print("invalid input")

# # task 31
# bank=int(input("1.Personal Banking\n2.Business Banking : "))
# match bank:
#     case 1:
#         option=int(input("1.Balance\n2.Transfer\n3.Loan : "))
#         match option:
#             case 1:
#                 print("Balance selected")
#             case 2:
#                 print("Transfer Selected")
#             case 3:
#                 print("Loan Selected")
#             case _:
#                 print("Invalid input")
#     case 2:
#         option=int(input("1.Balance\n2.Payroll\n3.Buisness Laon : "))
#         match option:
#             case 1:
#                 print("Balance selected")
#             case 2:
#                 print("Payroll Selected")
#             case 3:
#                 print(" Buisness Loan Selected")
#             case _:
#                 print("Invalid input")
#     case _:
#         print("Invalid input")

# # task 32
# school=int(input("1.Student\n2.Teacher\n3.Parents : "))
# match school:
#     case 1:
#         print("Student")
#         option=int(input("1.Marks\n2.Attendance\n3.Homework : "))
#         match option:
#             case 1:
#                 print("Marks")
#             case 2:
#                 print("Attendance")
#             case 3:
#                 print("Homework")
#             case _:
#                 print("Invalid input")
#     case 2:
#             print("Teacher")
#             option=int(input("1.Enter Marks\n2.Attendance\n3. Assign Homework : "))
#             match option:
#                 case 1:
#                     print("Enter Marks")
#                 case 2:
#                     print("Attendance")
#                 case 3:
#                     print("Assigned Homework")
#                 case _:
#                     print("Invalid input")
#     case 3:
#             print("Parents")
#             option=int(input("1.Child Marks\n2.Child Attendance\n3.Contact Teacher : "))
#             match option:
#                 case 1:
#                     print("Child Marks")
#                 case 2:
#                     print("Child Attendance")
#                 case 3:
#                     print("Contact teacher")
#                 case _:
#                     print("Invalid input")
#     case _:
#         print("Invalid input")


# # task 33
# Travel=int(input("1.Flight\n2.Bus\n3.Train : "))
# match Travel:
#     case 1:
#         print("Flight")
#         option=int(input("1.Economy\n2.Business : "))
#         match option:
#             case 1:
#                 print("Economy class Selected")
#             case 2:
#                 print("Business class Selected")
#             case _:
#                 print("Invalid input")
#     case 2:
#             print("Train")
#             option=int(input("1.Sleeper\n2.AC : "))
#             match option:
#                 case 1:
#                     print("Sleeper class Selected")
#                 case 2:
#                     print("AC class Selected")
#                 case _:
#                     print("Invalid input")
#     case 3:
#             print("Bus")
#             option=int(input("1.Ordinary\n2.Volvo : "))
#             match option:
#                 case 1:
#                     print(" Ordinary class Selected")
#                 case 2:
#                     print("Volvo class Selected")
#                 case _:
#                     print("Invalid input")
#     case _:
#         print("Invalid input")

# # task 33
# Menu=int(input("1.Start Game\n2.Load Game\n3.Settings\n4.Exit : "))
# match Menu:
#     case 1:
#         print("Game Started")
#     case 2:
#             print("Game Loaded")
#     case 3:
#             print("Settings")
#             option=int(input("1.Sounds\n2.Graphics\n3.Controls : "))
#             match option:
#                 case 1:
#                     print(" Sounds Selected")
#                 case 2:
#                     print("Graphics Selected")
#                 case 3:
#                       print("Controls Selected")
                      
#                 case _:
#                     print("Invalid input")
#     case _:
#         print("Invalid input")


# task 35
# order=int(input("1.Starters\n2.Main course\n3.Desert\n4.Drinks : "))
# match order:
#     case 1:
#         print("Starters")
#         option=int(input("1.Soup\n2.Spring roll\n3.Garlic Bread : "))
#         match option:
#             case 1:
#                 print("Soup Ordered")
#             case 2:
#                 print("Spring roll Ordered")
#             case 3:
#                 print("Garlic Bread Ordered")
#             case _:
#                 print("Invalid input")
#     case 2:
#             print("Main Course")
#             option=int(input("1.Pizza\n2.Pasta\n3.Biryani : "))
#             match option:
#                 case 1:
#                     print("Pizza Ordered")
#                 case 2:
#                     print("Pasta Ordered")
#                 case 3:
#                     print("Biryani Ordered")
#                 case _:
#                     print("Invalid input")
#     case 3:
#             print("Dessert")
#             option=int(input("1.Ice Cream\n2.Cake\n3.Gulab Jamun : "))
#             match option:
#                 case 1:
#                     print("Ice Cream Ordered")
#                 case 2:
#                     print("Cake Ordered")
#                 case 3:
#                     print("Gulab Jamun Ordered")
#                 case _:
#                     print("Invalid input")
#     case 4:
#             print("Drinks")
#             option=int(input("1.Coffee\n2.Tea\n3.Juice : "))
#             match option:
#                 case 1:
#                     print("Coffee Ordered")
#                 case 2:
#                     print("Tea Ordered")
#                 case 3:
#                     print("Juice Ordered")
#                 case _:
#                     print("Invalid input")
    
#     case _:
#         print("Invalid input")

# # task 36
# payment=int(input("1.UPI\n2.Card\n3.Wallet : "))
# match payment:
#     case 1:
#         print("UPI mode selected")
#         option=int(input("1.Scan QR\n2.Enter UPI ID : "))
#         match option:
#             case 1:
#                 print("Scan QR Selected")
#             case 2:
#                 print("Enter UPI ID Selected")
#             case _:
#                 print("Invalid input")
#     case 2:
#             print("Card mode selected")
#             option=int(input("1.Credit Card\n2.Debit Card : "))
#             match option:
#                 case 1:
#                     print("Credit Card Selected")
#                 case 2:
#                     print("Debit Card Selected")
#                 case _:
#                     print("Invalid input")
#     case 3:
#                 print("Wallet mode selected")
#                 option=int(input("1.Add Money\n2.Pay using wallet : "))
#                 match option:
#                     case 1:
#                         print("Add Money Selected")
#                     case 2:
#                         print("Pay using wallet Selected")
#                     case _:
#                         print("Invalid input")
#     case _:
#             print("Invalid input")

# # task 37
# subject=int(input("1.Programming\n2.Mathematics\n3.Communication : "))
# match subject:
#     case 1:
#         print("Programming Selected")
#         option=int(input("1.Python\n2.Java\n3.C++ : "))
#         match option:
#             case 1:
#                 print("Python Selected")
#             case 2:
#                 print("Java Selected")
#             case 3:
#                 print("C++ Selected")
#             case _:
#                 print("Invalid input")
#     case 2:
#             print("Mathematics")
#             option=int(input("1.Algebra\n2.Calculas\n3.Statistics : "))
#             match option:
#                 case 1:
#                     print("Algebra Selected")
#                 case 2:
#                     print("Calculas Selected")
#                 case 3:
#                     print("Statistics Selected")
#                 case _:
#                     print("Invalid input")
#     case 3:
#                 print("Communication")
#                 option=int(input("1.English\n2.Presentation\n3.Interview sKills : "))
#                 match option:
#                     case 1:
#                         print("Algebra Selected")
#                     case 2:
#                         print("Calculas Selected")
#                     case 3:
#                         print("Statistics Selected")
#                     case _:
#                         print("Invalid input")
    
#     case _:
#         print("Invalid input")

# # task 38
# vehicle=int(input("1.Engine\n2.Lights\n3.Music\n4.Navigation : "))
# match vehicle:
#     case 1:
#         option=int(input("1.Start\n2.Stop : "))
#         match option:
#             case 1:
#                 print("Vehicle Started")
#             case 2:
#                 print("Vehicle Stopped")
#             case _:
#                 print("Invalid Input")
#     case 2:
#             print("Lights")
#             option=int(input("1.Headlights\n2.Indicators\3.Hazard Lights : "))
#             match option:
#                 case 1:
#                     print("Headlights")
#                 case 2:
#                     print("Indicatiors")
#                 case 3:
#                     print("Hazard Lights")
#                 case _:
#                       print("Invalid Input")
#     case 3:
#             print("Music")
#             option=int(input("1.Play\n2.Pause\3.Next\n4. Previous : "))
#             match option:
#                 case 1:
#                     print("Music Played")
#                 case 2:
#                     print("Music Puased")
#                 case 3:
#                     print("Next Music")
#                 case 4:
#                     print("Previous Music")
#                 case _:
#                     print("Invalid Input")
#     case 4:
#           print("Navigation")
#           option=int(input("1.Start Navigation\n2.Stop Navigation : "))
#           match option:
#                 case 1:
#                     print("Navigation Started")
#                 case 2:
#                     print("Navigation Stopped")
#                 case _:
#                     print("Invalid Input")
#     case _:
#         print("Invalid Input")

# # task 39
# employee=int(input("1.Employee\n2.Manager : "))
# match employee:
#     case 1:
#         print("Employee")
#         option=int(input("1.Veiw Profile\n 2.Apply Leave \n3.View Salary : "))
#         match option:
#             case 1:
#                 print("View Profile selected")
#             case 2:
#                 leave=int(input("Enter how many days of leave you want : "))
#                 if leave>0:
#                     print("Leave Request Submitted")
#                 else:
#                     print("Invalid Leave Days")
#             case 3:
#                 print("View Salary")
#             case _:
#                 print("Invalid Input")
#     case 2:
#         print("Manager")
#         option=int(input("1.Veiw Team\n 2.Approve Leave \n3.View Reports : "))
#         match option:
#             case 1:
#                 print("Team Viewed")
#             case 2:
#                 print("Approve Leave")
#             case 3:
#                 print("View Reports")
#             case _:
#                 print("Invalid Input")
#     case _:
#         print("Invalid Input")

# # task 40
# role=int(input("1.Student\n2.Teacher\n3.Adminstration : "))
# match role:
#     case 1:
#         print("Student Portal")
#         option=int(input("1.Profile\n2.Marks\n3.Attendance\n4.Courses : "))
#         match option:
#             case 1:
#                 print("Opening Student Profile")
#             case 2:
#                 print("Opening Student Marks")
#             case 3:
#                 print("Opening Student Attendance Portal")
#             case 4:
#                 print("Student Courses")
#             case _:
#                 print("Invalid Input")
#     case 2:
#         print("Teacher Portal")
#         option=int(input("1.Students\n2.Enter Marks\n3.Attendance\n4.Courses : "))
#         match option:
#             case 1:
#                 print("Opening Student's List")
#             case 2:
#                 print("Enter Student Marks")
#             case 3:
#                 print("Opening Student Attendance Portal")
#             case 4:
#                 print("Student Courses")
#             case _:
#                 print("Invalid Input")
#     case 3:
#             print("Admistration Portal")
#             option=int(input("1.Fees\n2.Admissions\n3.Notices\n4.Departments : "))
#             match option:
#                 case 1:
#                     print("Opening Fees Structure")
#                 case 2:
#                     print("Admisson Portal")
#                 case 3:
#                     print("Notice board")
#                 case 4:
#                     print("All Departments")
#                 case _:
#                     print("Invalid Input")
#     case _:
#         print("Invalid Input")



          
     


    







