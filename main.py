#Завдання 10.3.1
def isIterable(obj):
    return hasattr(obj, '__iter__') or hasattr(obj, '__getitem__')

print("10.3.1 — isIterable")
for value in [123, "abc", [1, 2], {1: 1}, 5.5, (x for x in range(5))]:
    print(f"{value} => {isIterable(value)}")
print()


#Завдання 10.3.2
def print_class_name(obj):
    print("Class name:", obj.__class__.__name__)

print("10.3.2 — class name")
print_class_name(123)
print_class_name("hello")
print_class_name(print)
print()


#Завдання 10.3.3
def function_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@function_decorator
def say_hello(name):
    print(f"Hello, {name}!")

print("10.3.3 — function decorator")
say_hello("Illia")
print()


#Завдання 10.3.4
def class_decorator(cls):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            print(f"Creating instance of class: {cls.__name__}")
            super().__init__(*args, **kwargs)
    return NewClass

@class_decorator
class Student:
    def __init__(self, name):
        self.name = name
        print(f"Student created: {self.name}")

print("10.3.4 — class decorator")
s = Student("Illia")