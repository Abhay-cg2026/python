
# # Ques - 1
# def show_city():
#     city = "Indore"
#     print(city)
# show_city()

# # Ques - 2
# School = "Govt. School of Excellence Indore"
# def show_school():
#     global School
#     print (School)
# show_school()

# # Ques - 3
# if True:
#     y=15
# print(y)

# # Ques - 4
# for number in range(1,4):
#     print(number)

# # # Ques - 5
# # => Scope - Where a name can be accesed.
# # => Lifetime - How long a name binding or object continues to exist. 


# # Ques - 6
# value = 100
# def test():
#     value = 200
#     print(value)
# test()
# print(value)

# # Output : 
# # 200
# # 100

# # Ques - 7
# clicks = 0
# def click():
#     global clicks
#     clicks += 1
#     print(clicks)
# click()

# # Ques - 8
# #because the variable is designed in the function but the variable is not visible cause fuction loads the variables but does not assign values to it.

# Ques - 9
message="Global"
def outer():
    message="Enclosing"
    def inner():
        print(message)
    inner()
outer()

# Question-8
# name = "Asha"
# def show():
#     print(name)
#     name = "Ravi"
# show()

# Reason to raise an error:-Here in the show named function ,print function is written above the name variable which is already printed before assigning also it doesn't access the global varible because, after checking the variable in the function, it actually finds it but can't get the value of the variable as its assigning is after the print statement.
 
# Question-9
def function9_1():
    hello_world = "Hello World"
    def function9_2():
        print(hello_world)
    function9_2()
function9_1()

# Question-10
def function10():
    list_10 = ["I", "Am", "Atomic"]
    return list_10
print(function10())

# Question-11
def function11_1():
    count = 0
    def function11_2():
        nonlocal count
        count += 1
        print(count)
    return function11_2
counter = function11_1()
counter()  # 1
counter()  # 2
counter()  # 3

# Question-12
x = 1
def outer():
    x = 2
    def inner():
        x = 3
        print(x)
    inner()
    print(x)
outer()
print(x)
# Output:- 3 ,then 2 and then 1

# Question-13
# Ans:- This happens because Python treats variables normal in for loops and list comprehensions differently in terms of scope.

# Question-14
def make_counter():
    count = 0
    def increment():
        nonlocal count  
        count += 1
        return count
    return increment
new_variable = make_counter()
print(new_variable())
print(new_variable())
print(new_variable())

# Question-15
# Ans:-because the words like 'list','str' and 'sum' because they are used in python for some built in keywords








