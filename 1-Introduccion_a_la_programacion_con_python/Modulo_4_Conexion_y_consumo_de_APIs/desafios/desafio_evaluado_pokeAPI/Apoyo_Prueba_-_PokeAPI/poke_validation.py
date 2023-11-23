import data as d # ---> Este modulo debemos crearlo nosotros

with open("pokemon_list.txt", "r") as f:
    pokemon_lista = f.readlines()
    
# En una lista se guardaran los nombres del archivo pokemon_list.txt
# Con la funcion "strip()" eliminamos el \n que se agrega por defecto al nombre de cada Pokemon en el archivo
pokemon_lista = [elemento.strip('\n') for elemento in pokemon_lista]

# ESTA ES OTRA FORMA PARA HACER LO MISMO
# lista = []
# archivo = open('pokemon_list.txt', 'r', encoding='UTF-8')
# for elemento in archivo.readlines():
#     lista.append(elemento.strip('\n'))

def validate(name, p_l = pokemon_lista, mensaje = d.validacion_pokemon):
    if name =='codigo-cero':
        name = 'type-null'
    while name not in p_l:
        name = input(mensaje).lower()
    return name


if __name__ == '__main__':
    name = 'codigo-cero'
    print(validate(name))
