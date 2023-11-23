def validate(opciones, eleccion):
    while True:
        if eleccion in opciones:
            return eleccion
        else:
            print('Opción no válida, ingrese una de las opciones válidas')
            eleccion = input('Ingresa una Opción: ').lower()

##########################
# También podriamos hacerlo asi, se nos repetirá la pregunta hasta ingresar una eleccion correcta
#
# def validate(opciones, eleccion):
#     
#     while eleccion not in opciones:
#         eleccion = input('Ingresa una Opción: ').lower()
        
#     return eleccion



if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
