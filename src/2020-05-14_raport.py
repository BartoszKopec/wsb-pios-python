x = 5
y = 0
try:
    z = x / y #operacja niedozwolona - dzielenie przez 0
except ZeroDivisionError:
    print(x, '/', y, 'ZeroDivisionError')

list=[]
e=Exception
try:
    print(list[3])
except IndexError: #wyjątek wyrzucony podczas przekroczenia rozmiaru kolekcji
    print('List count',len(list))

import sys
operation=input('Type any python operation (in example "10/0" and enter or nothing and enter to skip): ') #zdobycie od usera dowolnej operacji (np. matematycznej)
try:
    eval(operation) #interpretacja wpisanej operacji
except: #przechwycenie wyjątku dowolnego typu jeżeli jakiś wystąpił podczas interpretacji wyżej
    e = sys.exc_info()[0] #zdobycie typu wyrzuconego wyjątku
    print('There was an error while evaluating typed operation. Error type: ', e)
finally: #instrukcje w bloku finally wykonają się zawsze
    print('Evaluated typed operation')

#---------------------------------------------------------------

list = [1,2,3,4,5] #lista o rozmiarze 5
def getElementWithAssertion(i): #funkcja zwracająca i-ty element listy chyba że rozmiar został przekroczony
    assert i < len(list), '"i" must be less than length of list'
    return list[i]

def getElementWithRaise(i):
    if i > len(list):
        raise Exception('"i" must be less than length of list')
    return list[i]

try:
    getElementWithAssertion(6)
except AssertionError as e:
    print('Assertion: ', e.args[0])

try:
    getElementWithRaise(6)
except Exception as e:
    print('Raise: ', e.args[0])
