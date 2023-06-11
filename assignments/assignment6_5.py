#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.

text = "X-DSPAM-Confidence:    0.8475"

# Desired output: 0.8475

#Encontrar espacio
espacio = text.find("   ")

#Extraer numero
numero = text[espacio+4:]

numero = float(numero)

print(numero)