def readFile(filePath): # funkcja pozwalająca przeczytać całość podanego pliku
    print()
    print(filePath, "content:")
    file = open(filePath, "r")
    if file.readable():
        print(file.read())
    file.close()

def writeNewContentToFile(filePath, text): # funkcja pozwalająca zapisać nową zawartość do podanego pliku
    file = open(filePath, "w")
    if file.writable():
        file.write(text)
    file.close()

def addContentToFile(filePath, text): # funkcja pozwalająca dodać nową zawartość do już istniejącej 
    file = open(filePath, "a")
    if file.writable():
        file.write(text)
    file.close()

def readFileWithLines(filePath): # funkcja pozwalająca przeczytać linijka po linijce zawartość pliku
    print()
    print(filePath, "content with lines:")
    file = open(filePath, "r")
    if file.readable():
        i=1
        fileText=""
        for line in file.readlines():
            fileText += str(i)+": " + line
            i+=1
        print(fileText)
    file.close()

filePath = "file.txt"

file = open(filePath) # próba domyślnego otwarcia pliku bez flagi "w" lub "a" nie pozwoli zapisać zawartości do pliku
if not file.writable():
    print("File is not writable")
file.close()

writeNewContentToFile(filePath, "Name: ")
print("File is writable now. Can be modifing")
addContentToFile(filePath, input("Write name: ") + "\n")

readFile(filePath)

addContentToFile(filePath, "City: ")
addContentToFile(filePath, input("Write city: ") + "\n")

readFileWithLines(filePath)

################################################################


data = {
    "name": "Jan",
    "city": "Wroclaw",
    "country": "Poland"
}
# print(data[1]) nie ma takich indeksów 
# print(data[2])
print(data["name"])
print(data["city"])

data = {
    0: "Jan",
    1: "Wroclaw",
    5: "Poland"
}
print(data.get(0)) # teraz już są
print(data.get(1))
print(data.get(2, "There isn't 2 index"))
print(data.get(5))

data.pop(0)
print(data.get(0, "There isn't 0 index"))

################################################################

tuple = ("a", "b", "c", "a", "d", "e")
print(tuple[0])
print(tuple[1])
print(tuple[2])
print(tuple)

# tuple[0]="d"  nie można przypisywać nowych wartość elementom krotki

print(tuple.count("a")) # liczenie ilości wystąpień parametru
print(tuple.index("a")) # zwrócenie pierwszego znalezionego indeksu pod którym znajduje się parametr
print(tuple[0:3]) # wyświetlenie podanego zakresu w formie <x1,x2) czyli index po ":" nie jest uwzględniany
print(tuple[::2]) # wyświetlenie co drugiego elementu
print(tuple[::-1]) # wyświetlenie odwróconej krotki