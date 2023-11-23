import sys

with open("lorem_ipsum.txt", "r") as file:
    lorem_ipsum=file.read()
    #print(lorem_ipsum)
    
    #Nota: esta parte la imprimo 3 veces porque iba verificando que el código hiciera lo que quería.
    palabras_separadas= lorem_ipsum.split()
    #print(palabras_separadas)

    cantidad_palabras=len(palabras_separadas)
    #print(cantidad_palabras)

    #para que considere las palabras distintas debo transformar esta lista en un set

    palabras_distintas = set(palabras_separadas)
    #print(palabras_distintas)

    cantidad_palabras_distintas = len(palabras_distintas)
    print(f"El número de palabras distintas es: {cantidad_palabras_distintas}")

    #Al final comenté los prints demás para que el output fuese como lo habian pedido 

    #ahora para separar letra por letra debo tomar la primera lista original y pasarla a set y luego contar
    
    letras_caracteres= set(lorem_ipsum)
    print(f"El número de caracteres distintos es: {len(letras_caracteres)}")
