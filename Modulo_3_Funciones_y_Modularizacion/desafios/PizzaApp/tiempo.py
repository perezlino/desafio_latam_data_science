def estimar_tiempo(ingredientes):
    n_ingredientes = len(ingredientes['ingredientes'])
    tiempo = 20 + 2 * n_ingredientes
    return tiempo

if __name__ == '__main__':
    ingredientes_prueba = { 'masa':'Masa Tradicional',
                        'salsa':'Salsa de Tomate',
                        'ingredientes': ['Queso']
                        }

    print(estimar_tiempo(ingredientes_prueba))    