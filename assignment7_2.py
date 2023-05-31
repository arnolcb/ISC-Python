# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line)

#Buscar el codigo que acompaña a X-DSPAM-Confidence, dentro del txt
#Encontrar espacio
espacio = line.find(" ")

#Extraer numero
numero = 0
contNumero = 0
sumaNumeros = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    numero = line[espacio+4:]
    numero = float(numero)
    contNumero = contNumero + 1
    sumaNumeros = sumaNumeros + numero

print("Average spam confidence:", sumaNumeros)


print("Done")