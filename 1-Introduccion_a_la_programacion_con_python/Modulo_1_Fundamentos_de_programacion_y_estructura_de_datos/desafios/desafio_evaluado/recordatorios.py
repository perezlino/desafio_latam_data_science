# Base para crear el código
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]
#----------------------------------------------------------------
#LO QUE  HAY QUE HACER:
#Agregar en la posición 1: ['2021-02-02', "06:00", "Empezar el Año"]
#Reemplazar en la posición 3: ['2021-07-16']
#Eliminar la futura posición 2
#Agregar en la posición -2: ['2021-12-24', "22:00", "Cena de Navidad"]
#Agregar en la posición -1: ['2021-12-31', "22:00", "Cena de Año Nuevo"]
#RECONOCIENDO LA LISTA
#print(recordatorios)

#Aquí agrego el primer requerimiento, y de una vez elimino el tercer requerimiento reemplazandolo  a la vez
recordatorios[1]=['2021-02-02', "06:00", "Empezar el Año"]
#Imprimí para verificar
#print(recordatorios)

#Eliminé el elemento de la posición 2 para luego insertar en esa posición el elemento nuevo
del recordatorios[2]
recordatorios.insert(2,['2021-07-16', '13:00', 'No hacer nada es feriado'])

#Agregaré cena de navidad con el insert en la posición 4 y luego con append agregaré cena de año nuevo
recordatorios.insert(4,['2021-12-24', "22:00", "Cena de Navidad"])
recordatorios.append(['2021-12-31', "22:00", "Cena de Año Nuevo"])

#print(recordatorios)

recordatorios_ordenado = ""
for r in recordatorios:
    recordatorios_ordenado = recordatorios_ordenado + str(r) + "\n"

print(recordatorios_ordenado)