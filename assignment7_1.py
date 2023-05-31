# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

#Funcion para imprimir el archivo
def printFile(file):
    for line in file:
        print(line.upper().rstrip())

printFile(fh)