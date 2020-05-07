def simpleFunc(): #najprostsza kontrukcja funkcji
    print("foo") #jej ciało musi być wcięte w prawą stronę tak jak ma to miejsce w przypadku pętli lub instrukcji warunkowych
simpleFunc()

def add(a, b): #dowolna ilość parametrów może być przekazana. Są one traktowane jako zmienne lokalne 
    return a+b #standardowa instrukcja zwrócenia wartości z funkcji
print(add(1, 5))

def F(x):
    return 2*(x**3) + 5*x
print(F(7))

def strong(x): #przykład rekurencji: silnia
    if x==1:
        return 1
    return x * strong(x-1)
print(strong(6))

def fib(n): #n-ty element ciągu fibonacciego metodą rekurencyjną
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 1
    return fib(n-2)+fib(n-1)
print(fib(6))


import random #import całego modułu/biblioteki
print(random.randint(1, 10))

from math import pi #import konkretnej funkcji z modułu math
print(pi)

from math import sqrt as square #import konkretnej funkcji z modułu math z nadaniem jej nowego aliasu obowiązującego w tym skrypcie
print(square(16))