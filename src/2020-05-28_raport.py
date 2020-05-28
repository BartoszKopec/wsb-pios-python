list = ['a', 'b', 'c', 'c'] # stworzenie kolekcji która ma 4 elementy
print(list)
setFromList = set(list) # stworzenie zbioru z kolekcji który ma 3 elementy, ponieważ zostały zignorowane dane powtarzające się
print(setFromList)
setFromList.add('d')
print(setFromList)
setFromList.remove('a')
print(setFromList) # dodanie elementu do zbioru i usunięcie elementu ze zbioru
print('a' in setFromList) # wyrażenie logiczne pozwalające sprawdzić czy dana wartość jest w zbiorze

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 | set2) # logiczna suma zbiorów
print(set1 - set2) # logiczna różnica zbioru 1 i zbioru 2
print(set2 - set1) # logiczna różnica zbioru 2 i zbioru 3
print(set2 ^ set1) # zwrócenie zbioru zawierającego wartości niepowatrzające się w obu zbiorach

# --------------------------------------------------------------

class Vehicle: # klasa
    _wheels = 0 # jej pole "prywatne"

    def __init__(self, wheels): # metoda inicjalizująca z jednym parametrem
        self._wheels = wheels

    def getWheels(self): # getter zwracający wartość pola 
        return self._wheels

v1 = Vehicle(2)
print(v1)
print(v1.getWheels())

# --------------------------------------------------------------
    
class Car(Vehicle): # klasa dziedzicząca właściwości po klasie Vehicle
    _name=''

    def __init__(self, name): # zastąpienie konstruktora rodzica własnym konstruktorem
        super().__init__(4) # wywołanie konstruktora rodzica
        self._name = name

    def getName(self):
        return self._name

c1 = Car('Fiat')
print(c1.getName())
print(c1.getWheels())

# --------------------------------------------------------------

class PartVehicle(Vehicle):
    def __add__(self, secondVehicle): # magiczna metoda - operator dodawania dwóch wartości
        return PartVehicle(self.getWheels() + secondVehicle.getWheels())
    def __eq__(self, secondVehicle):
        return self.getWheels() == secondVehicle.getWheels()
    def __len__(self):
        return self.getWheels()


p1 = PartVehicle(4) # pojazd o 4 kołach (np. samochód ciężarowy)
p2 = PartVehicle(6) # pojazd o 6 kołach (np. naczepa)
p3 = p1 + p2 # zespół pojazdów
print(p3.getWheels())
print(p3 == p1 + p2)
print(len(p3))