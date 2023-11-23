from masa import tipo_masa
from salsa import tipo_salsa
from add import agregar_ingrediente
from remove import remover_ingrediente
from show import mostrar_ingrediente
from tiempo import estimar_tiempo

import sys
import os
import time

## Esta linea va a funcionar para ir limpiando la pantalla en consola
## Desde consola ingreso al directorio cd C:\github\desafio_latam_data_science\Modulo_3_Funciones_y_Modularizacion\desafios\PizzaApp
## Luego escribo ----> python main.py
clear = 'cls' if sys.platform == 'win32' else 'clear'

ingredientes_orden = { 'masa':'Masa Tradicional',
        			   'salsa':'Salsa de Tomate',
		        	   'ingredientes': ['Queso']
		             }

while True:

    os.system(clear)

    opcion = input('''¿Qué desea realizar?
                    1.	Cambiar tipo de Masa
                    2.	Cambiar tipo de Salsa
                    3.	Agregar Ingredientes
                    4.	Eliminar Ingredientes
                    5.	Ordenar con los Ingredientes Actuales	
                    0.	Consultar ingredientes de la pizza
                    Otro Número cancelará el pedido.
                    > ''')

    if opcion == '1':
        eleccion = input('''Escoja el tipo de masa:
                        T) Masa Tradicional
                        D) Masa Delgada
                        B) Masa con Bordes de Queso
                        > ''').upper()
        
        ingredientes_orden = tipo_masa(ingredientes_orden, eleccion)

    elif opcion == '2':
        eleccion = input('''Escoja el tipo de salsa:
                        T) Salsa de tomate
                        A) Salsa Alfredo
                        B) Salsa Barbecue
                        P) Salsa Pesto                    
                        > ''').upper()
        
        ingredientes_orden = tipo_salsa(ingredientes_orden, eleccion)    

    elif opcion == '3':        
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
        
        ingredientes_orden = agregar_ingrediente(ingredientes_orden, eleccion)

    elif opcion == '4':        
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
        
        ingredientes_orden = remover_ingrediente(ingredientes_orden, eleccion)        

    elif opcion == '5':         
        tiempo = estimar_tiempo(ingredientes_orden)
        print(f'Su Pizza se demorará {tiempo} minutos')
        ordenar = input('Desea ordenar ahora (S/N): ').upper()
        if ordenar == 'S':
            print('Disfrute su pizza!')
            break

    elif opcion == '0':         
        mostrar_ingrediente(ingredientes_orden)
        time.sleep(5) ## Para que la pantalla de ingredientes se mantenga en pantalla 5 segundos

    else:
        print('Pedido cancelado')
        break