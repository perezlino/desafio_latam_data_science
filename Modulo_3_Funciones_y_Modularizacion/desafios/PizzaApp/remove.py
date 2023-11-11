def remover_ingrediente(ingredientes, elección):

    disponibles = ['Tomate', 'Champiñones', 'Aceituna', 'Cebolla',       
                        'Pollo', 'Jamon', 'Carne', 'Tocino', 'Queso']
	   
    quitar = disponibles[elección-1]
    
    if quitar in ingredientes['ingredientes']:    
        ingredientes['ingredientes'].remove(quitar)
        print(f'El ingrediente {quitar} ha sido removido') 
    elif len(ingredientes['ingredientes']) == 0:
        print('No hay ningun ingrediente que quitar')                
    else: 
        print(f'El ingrediente {quitar} no se encuentra en su selección, por tanto, no podemos removerlo')
    
    return ingredientes

if __name__ == '__main__':
    ingredientes_prueba = { 'masa':'Masa Tradicional',
                        'salsa':'Salsa de Tomate',
                        'ingredientes': ['Queso']
                        }

    eleccion = int(input('''Seleccione su ingrediente:
                    1) Tomate
                    2) Champiñones
                    3) Aceituna
                    4) Cebolla                  
                    5) Pollo
                    6) Jamon
                    7) Carne
                    8) Tocino
                    9) Queso
                    > '''))
    
    ingredientes = remover_ingrediente(ingredientes_prueba, eleccion)

    print(ingredientes)