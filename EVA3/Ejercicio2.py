#2.	Función que reciba un texto de caracteres y cuente cuántas vocales contiene

def ingresarTexto():
    return input("Ingrese texto : ").lower()

def contarVocales(texto):
    contador = 0
    for letra in texto:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            contador+=1
    return contador

def main():
    texto = ingresarTexto()
    cantVocales = contarVocales(texto)
    print(f"La cantidad de vocales es: {cantVocales}")
    
##PP
main()