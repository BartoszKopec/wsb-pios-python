x = 1
s = 'text' #zwykłe zmienne

l = [x, s, True, 0.4] #lista elementów dowolnego typu
print(l)

print('element pierwszy: ', l[0]) #odwołanie do elementów za pomocą przypisanych do nich indeksów (od 0 w górę)

l[0] = 9 #przypisanie nowej wartości elementowi o indeksie 0
print('nowa wartość elementu', l)

l.append(10) #dodanie nowego elementu na końcu listy
print(l)

l.insert(0, 'str') #dodanie nowego elementu na początku listy
print(l)

print('Ilość elemenów: ',len(l))

numbers = [1,5,7,3,89,3,0]
print('Element mininalny: ',min(numbers), '\nElement maksymalny: ', max(numbers))
print('Liczba wystąpień trójek: ', numbers.count(3))
numbers.reverse() #odwrócenie listy
print(numbers)

matrix = [ [1,2,3], [4,5,6], [7,8,9] ] #lista list, macierz
print(matrix[2][2]) #odwołanie do ostatniego elementu - 9
print(matrix[0].index(3)) #indeks trójki z pierwszej listy
matrix.remove(matrix[0]) #usunięcie pierwszego elementu listy
print(matrix)


print()
print()
print()


for number in numbers: #wyświetlenie wszystkich elementów listy
    print(number)
print()

print(list(range(1, 10, 2))) #wygenerowanie listy
for number in range(10): #wyświetlenie wygenerowanych elementów
    print(number)
print()

for i in range(len(numbers)): #wyświetlenie wszystkich elementów listy
    print(numbers[i])
print()