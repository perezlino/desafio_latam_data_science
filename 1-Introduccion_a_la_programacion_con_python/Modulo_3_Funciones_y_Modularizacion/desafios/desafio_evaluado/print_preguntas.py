import preguntas as p
from pprint import pprint

def print_pregunta(enunciado, alternativas):
    
    alternativas_elegir = ['A', 'B', 'C', 'D']
    
    print(f'{enunciado[0]}\n')
    
    for alternativas_diponibles in zip(alternativas_elegir, alternativas):
        print(f'{alternativas_diponibles[0]}. {alternativas_diponibles[1][0]}')
    
        
if __name__ == '__main__':
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4


    ###############################################################
    # EXPLICACION EN DETALLE
    ###############################################################

    # pregunta = p.pool_preguntas['basicas'] ===> preguntas_basicas 
    # pregunta = {
    # 'pregunta_1': {'enunciado':['Enunciado básico 1'],
    # 'alternativas': [['alt_1', 0], 
    #                  ['alt_2', 1], 
    #                  ['alt_3', 0], 
    #                  ['alt_4', 0]]},
    # 'pregunta_2': {'enunciado':['Enunciado básico 2'],
    # 'alternativas': [['alt_1', 0], 
    #                  ['alt_2', 1], 
    #                  ['alt_3', 0], 
    #                  ['alt_4', 0]]}
    # 'pregunta_3': {'enunciado':['Enunciado básico 3'],
    # 'alternativas': [['alt_1', 0], 
    #                      ['alt_2', 1], 
    #                      ['alt_3', 0], 
    #                      ['alt_4', 0]]}
    # }

    ###############################################################
    # 
    # pregunta = p.pool_preguntas['basicas']['pregunta_1']
    # pregunta = {'enunciado':['Enunciado básico 1'],
    #             'alternativas': [['alt_1', 0], 
    #                             ['alt_2', 1], 
    #                             ['alt_3', 0], 
    #                             ['alt_4', 0]]}
    # 
    ###############################################################
    # 
    # pregunta['enunciado'] ===> ['Enunciado básico 1'] 
    # 
    # pregunta['alternativas'] ===> [['alt_1', 0], 
    #                                ['alt_2', 1], 
    #                                ['alt_3', 0], 
    #                                ['alt_4', 0]]

    ###############################################################
    #
    # print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    #
    #  ENTONCES, desmenucemos la función:
    #
    # def print_pregunta(enunciado, alternativas):
    #
    #   alternativas_elegir = ['A', 'B', 'C', 'D']
    #
    #   print(f'{enunciado[0]}\n')  ===> Enunciado básico 1 + un salto de linea
    #
    #   for alternativas_diponibles in zip(alternativas_elegir, alternativas): ===> ('A', ['alt_1', 0])
    #                                                                               ('B', ['alt_2', 1])
    #                                                                               ('C', ['alt_3', 0])
    #                                                                               ('D', ['alt_4', 0])
 
    #
    #   for alternativas_diponibles in zip(alternativas_elegir, alternativas):
    #       print(f'{alternativas_diponibles[0]}. {alternativas_diponibles[1][0]}') ===>  A. alt_1
    #                                                                                     B. alt_2
    #                                                                                     C. alt_3
    #                                                                                     D. alt_4