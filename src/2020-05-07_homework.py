from datetime import datetime

def getCurrentTime():
    return datetime.now().strftime("%H:%M:%S")
print(getCurrentTime())

def func(x, y):
    return x**4 + x**2 + 2*y
print(func(2, 3))

def fibonacci(n): 
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)
print(fibonacci(12))
