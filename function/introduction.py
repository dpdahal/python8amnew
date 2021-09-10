# define function
# def message():
#     # function body part
#     print("Hello function")
#
#
# # calling function
# message()

#  name='' optional

# def user(name, age=0):
#     print(name)
#     print(age)
#
#
# user('sophia',20)

# def users(names):
#     print(names)
#
#
# users(['ram','sita','gita'])

# * array arguments
# ** keywords


# def users(*names, **user):
#     print(names)
#     print(user)
#
#
# users('ram', 'sita', 'gita', 'hari', name='gopal', age=20)


# # function return value not a variable
# def add(x, y):
#     return x + y
#
#
# print(add(10, 20))


# def message(name):
#     return f"welcome {name}"
#
#
#
# print(message('sophia'))
# print(message('hari'))


# def add_sub(x, y):
#     sum = x + y
#     sub = x - y
#     return [sum, sub]
#
#
# print(add_sub(20, 10))


# function scope: local, global

# x = 10
#
#
# def test():
#     global x
#     x = x + 20
#     print(x)
#
#
# test()


# def display(**kwargs):
#     print(kwargs)
#     for i in kwargs:
#         print(kwargs[i])
#
#
# display(emp="Kelly", salary=9000)

#
# def user():
#     def get_name(name):
#         return f"my name is {name}"
#
#     return get_name
#
#
#
# # print(user()('ram'))
# obj = user()
# print(obj('sophia'))


# total = lambda x, y: x + y
#
# print(total(10, 20))
#
# def total(x,y):
#     return  x+y


# def num(n):
#     if n < 1:
#         return 1
#
#     return n * num(n - 1)
#
#
# print(num(5))

# 5-1 = 4 =20
#  4-1 = 3 = 60
# 3-1 = 2 = 120
# 2-1=1

# def any_function(fun):
#     def inner_function():
#         print(fun.__doc__)
#
#     return inner_function
#
#
# @any_function
# def test():
#     """
#     this is test function
#
#     """
#     return 'hello'
#
#
# test()

# print(test.__doc__)


# print(print.__doc__)

# x = 10
#
# print(dir(x))

# def check_zero_value(any):
#     def inner(x, y):
#         if y == 0:
#             return "Y is zero"
#         return any(x, y)
#
#     return inner
#
#
# @check_zero_value
# def div(x, y):
#     return x / y
#
#
# print(div(10, 1))


