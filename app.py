#Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.


def contar_vocales(cadena):
    # Definir las vocales
    vocales = 'aeiouAEIOU'
    # Inicializar el contador
    contador = 0
    
    # Recorrer cada carácter en la cadena
    for letra in cadena:
        # Verificar si el carácter es una vocal
        if letra in vocales:
            # Incrementar el contador
            contador += 1
    
    return contador

# Ejemplo de uso
cadena = input("Introduce una palabra: ")
numero_de_vocales = contar_vocales(cadena)
print(f"Número de vocales en la palabra: {numero_de_vocales}")