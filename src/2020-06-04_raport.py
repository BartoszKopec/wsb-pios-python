class First:
    def __init__(self):
        print("First constructor")
    def __del__(self): # magiczna metoda, która nadpisana wykonuje instrukcje podczas usunięcia obiektu z pamięci
        print("First destructor")

class Second:
    def __init__(self):
        print("Second constructor")
    def __del__(self):
        print("Second destructor")

obj = First()
obj2 = Second()

del obj # instrukcja ręcznego usunięcia obiektu z pamięci

# --------------------------------------------------------------
print()

class Listing:
    publicList=[] # pole nieobjęte zaufaniem prywatności
    _privateList=[] # pole objęte zaufaniem prywatności. Należy znać kod żeby wiedzieć o takim polu.
    __megaPrivateList=[] # pole objęte jeszcze większym zaufaniem prywatności. IDE nie pokazują pól "prywatnych", ale można mieć do nich dostęp

    def add(self, item):
        self.publicList.append(item)
        self._privateList.append(item)
        self.__megaPrivateList.append(item)
        
    def remove(self, index):
        if len(self.publicList) > 0:
            self.publicList.pop(index)
            self._privateList.pop(index)
            self.__megaPrivateList.pop(index)

    def printList(self):
        print('public list', self.publicList)
        print('private list', self._privateList)
        print('mega private list', self.__megaPrivateList)

listing = Listing()
listing.add('A')
listing.add('B')
listing.add('C')
listing.printList()
listing.publicList.clear() # operacja dowzolona bo pole nie jest objęte zaufaniem prywatności
listing._privateList.clear() # operacja umownie niedowzolona bo pole jest objęte zaufaniem prywatności
listing._Listing__megaPrivateList.clear() # operacja w ogóle niedowzolona bo pole jest objęte zaufaniem prywatności, a na dodatek dostęp do niego wymaga dopisania prefixu jak zostało napisane
listing.printList()

# --------------------------------------------------------------
print()

class BankAccount:
    __balance=0 # mega "prywatne" pole
  
    @property
    def balance(self):  # metoda pełniąca funkcję właściwości - bytu za pomocą można dostać się do prywatnego pola
        return self.__balance
    
    @balance.getter
    def balance(self): # wprost nadanie tej metodzie statusu gettera
        return 'Account balance is ' + str(self.__balance)
    
    @balance.setter
    def balance(self, value): # nadanie tej metodzie statusu settera
        self.__balance = value

account = BankAccount()
print(account.balance)
account.balance=150
print(account.balance)

# --------------------------------------------------------------
print()


class Statics:
    def someMethod(self): # metoda będąca częścią obiektu stworzonego z tej klasy
        print('Printed from class initialization - object of this class type')

    @classmethod
    def sum(cls, a, b):
        s = a + b
        print(s, 'This sum has been calculated in static method')

    @staticmethod # ta metoda również jest statyczna, ale nie jest oznaczona jako Metoda Klasy, nie przyjmuje pierwszego parametru "cls"
    def diff(a, b):
        s = a - b
        print(s, 'This difference has been calculated in static method')

st = Statics()
print('Method of object: ')
st.someMethod()
st.sum(1, 2) # iniciajlizacja klasy również ma dostęp do metody statycznej
st.diff(5, 3)
print('Static method: ')
Statics.sum(5, 6)
Statics.diff(10, 9)


# --------------------------------------------------------------
print()

print("Program end")
# każdy nieusunięty ręcznie obiekt zostaje automatycznie usunięty z pamięci po zakończeniu programu

