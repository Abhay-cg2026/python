# # task-1
# def welcome():
#     print("Wlcome To Python")
# welcome()

# # task-2
# def greet(name):
#     print("Hello!",name)
# greet("Adarsh")

# # task-3
# def show_number(number):
#     print("Selected Number:",number)
# show_number(24)

# # task-4
# def add(a,b):
#     return f"The Sum of these Two numbers :{a+b}"
# sum=add(12,87)
# print(sum)

# # task-5
# def square(number):
#     return f"The Square of {number} is {number**2}"
# Sq=square(13)
# print(Sq)

# # task-6
# def is_even(number):
#     if number%2==0:
#        return True
#     else:
#         return False
# status=is_even(27)
# print(status)
   
# # task-7
# def get_full_name(first_name,last_name):
#     return f"My name is {first_name+last_name}"
# full_name=get_full_name("Adarsh"," Anand")
# print(full_name)

# # task-8
# def introduction(name,city="Pune"):
#     return f"My Name is {name}.I live in {city}"
# intro=introduction("Rahul Nagar","Mumbai")  #in that case parameter's is replaced by argument
# Intro=introduction("Ashish Anand")  
# print(f"{intro}\n{Intro}")

# # task-9
# def subtract(a,b):
#     print(f"The Subtraction of {b} from {a} is {a-b}")
# subtract(16,7)

# # task-10
# def get_min_max(a,b):
#     if a>b:
#         return f"The Smaller And Larger Values Are {b} and {a} respectively."
#     else:
#         return f"The Smaller And Larger Values are {a} and {b} respectively."
# numbers=get_min_max(165,98)
# print(numbers)

# # task-21
# def analyze_number(number):
#     if number < 0:
#         absolute_value = -number
#     else:
#         absolute_value = number

#     even = number % 2 == 0
#     digits = len(str(absolute_value))

#     return absolute_value, even, digits

# print(analyze_number(-246))


# # task-22
# def calculate_stats(a, b, c):
#     return min(a, b, c), max(a, b, c), a + b + c

# print(calculate_stats(10, 25, 15))


# # task-23
# def make_sentence(subject, verb, object):
#     return f"{subject} {verb} {object}."

# print(make_sentence(object="Python", subject="I", verb="love"))


# # task-24
# def apply_discount(price, discount=0):
#     return price - (price * discount / 100)

# print(apply_discount(1000))
# print(apply_discount(1000, 20))
# print(apply_discount(price=2000, discount=15))


# # task-25
# def calculate_pay(hours, rate=200, bonus=0):
#     return hours * rate + bonus

# print(calculate_pay(8))
# print(calculate_pay(8, 250))
# print(calculate_pay(hours=8, bonus=500))
# print(calculate_pay(hours=10, rate=300, bonus=1000))


# # task-26
# def get_coordinates(x=0, y=0):
#     return x, y

# print(get_coordinates())
# print(get_coordinates(x=10))
# print(get_coordinates(y=20))


# # task-27
# def compare(a, b):
#     if a > b:
#         message = "A is greater"
#         difference = a - b
#     elif b > a:
#         message = "B is greater"
#         difference = b - a
#     else:
#         message = "Equal"
#         difference = 0

#     return message, difference

# print(compare(20, 10))
# print(compare(10, 20))
# print(compare(15, 15))


# # task-28
# def convert_temperature(value, scale="C"):
#     if scale == "C":
#         return (value * 9 / 5) + 32
#     else:
#         return (value - 32) * 5 / 9

# print(convert_temperature(25))
# print(convert_temperature(77, "F"))


# # task-29
# def calculate_result(marks, passing_marks=35):
#     if marks >= passing_marks:
#         return "Pass"
#     else:
#         return "Fail"

# print(calculate_result(80))
# print(calculate_result(30))
# print(calculate_result(60, 70))


# # task-30
# def order_summary(item, quantity=1, price=100, delivery_fee=40):
#     return quantity * price + delivery_fee

# print(order_summary("Book", 2, 150))
# print(order_summary("Book", 2, 150, delivery_fee=20))


# /- in the end of arg for positional arg.
# *- in the start of arg for keyword arg.

# def divide(a,b,*args,c,**kwargs):
#     total=0
#     for number in args:
#         total+=number
#     print(args,total)
#     sum=0
#     for number in 

# divide(1,2,3,4,5,6,7,7,c=8,l=22,m=23)

# x=0
# while x>=-10:
#     name="Abhay"
#     print(name)
#     x-=1
# print(name)

# message="Global"
# def outer():
#     global message
#     message=message+"Enclosing"
#     def inner():
#         nonlocal message
#         message=message+"local"
#         print(message)
#     inner()
# outer()
# print(message)

# def outer():
#     age=20
#     print(age)
#     return age
# data=outer()
# print(data)

def make_counter():
    count=0 
    def increment():
        nonlocal count
        count+=1
        return count
    return increment
counter = make_counter()
print(counter())
print(counter())
print(counter())
