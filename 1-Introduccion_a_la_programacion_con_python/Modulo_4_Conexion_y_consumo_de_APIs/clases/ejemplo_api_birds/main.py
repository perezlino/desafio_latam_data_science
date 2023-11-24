import requests
import json
from get_module import requests_get
from string import Template
from pprint import pprint

url = 'https://aves.ninjas.cl/api/birds'
response = requests_get(url)[:10] # Utilizaremos solo las 10 primeras aves

img_template = Template('<img src="$url">') # Luego con la funcion 'substitute' puedo dar otro valor a $url

html_template = Template('''
                         <!DOCTYPE html>
                                <html>
                                    <head>
                                    <tile> Titulo de la pagina </title>
                                    </head>
                                <body>

                                $body
                        
                                </body>
                                </html>
                        ''')

# Como son 10 aves, nos devuelve el tipo de cada elemento de esas 10 aves, que corresponde a un diccionario
for elemento in response:
    print(type(elemento)) # <class 'dict'>
                          # <class 'dict'>
                          # <class 'dict'>
                          # <class 'dict'>
                          # <class 'dict'>
                          # <class 'dict'>
                          # <class 'dict'>
                          # <class 'dict'>
                          # <class 'dict'>
                          # <class 'dict'>

lista_url = [elemento['images']['full'] for elemento in response]
pprint(lista_url) # ['https://aves.ninjas.cl/api/site/assets/files/3099/17082018024245aguilucho_chico_tomas_rivas_web.jpg',
                  #  'https://aves.ninjas.cl/api/site/assets/files/3102/18082018072023pato_juarjual_pedro_valencia_web.jpg',
                  #  'https://aves.ninjas.cl/api/site/assets/files/3105/17082018103640cisne_coscoroba_alejandro_labranque_3_web.jpg',  
                  #  'https://aves.ninjas.cl/api/site/assets/files/3109/13082018073638gaviota_austral_paula_de_marco_web.jpg',
                  #  'https://aves.ninjas.cl/api/site/assets/files/3111/18082018074355perdiz_chilena_pedro_valencia_web.jpg',
                  #  'https://aves.ninjas.cl/api/site/assets/files/3115/13082018100708tucuquere_camilo_maldonado_marin_web.jpg',       
                  #  'https://aves.ninjas.cl/api/site/assets/files/3118/04082018091522gaviota_dominicana_leslie_brackenridge_b.jpg',   
                  #  'https://aves.ninjas.cl/api/site/assets/files/3121/18082018075423perrito_pedro_valencia_web.jpg',
                  #  'https://aves.ninjas.cl/api/site/assets/files/3124/06082018101359pilpilen_leslie_brackenridge_b.jpg',
                  #  'https://aves.ninjas.cl/api/site/assets/files/3126/13082018101547zarapito_pico_recto_leslie_brackenridge_web.jpg']


imagenes = ''

for url in lista_url:
    imagenes += img_template.substitute(url = url) + '\n'

print(imagenes) # <img src="https://aves.ninjas.cl/api/site/assets/files/3099/17082018024245aguilucho_chico_tomas_rivas_web.jpg">
                # <img src="https://aves.ninjas.cl/api/site/assets/files/3102/18082018072023pato_juarjual_pedro_valencia_web.jpg">
                # <img src="https://aves.ninjas.cl/api/site/assets/files/3105/17082018103640cisne_coscoroba_alejandro_labranque_3_web.jpg">
                # <img src="https://aves.ninjas.cl/api/site/assets/files/3109/13082018073638gaviota_austral_paula_de_marco_web.jpg">
                # <img src="https://aves.ninjas.cl/api/site/assets/files/3111/18082018074355perdiz_chilena_pedro_valencia_web.jpg">
                # <img src="https://aves.ninjas.cl/api/site/assets/files/3115/13082018100708tucuquere_camilo_maldonado_marin_web.jpg">
                # <img src="https://aves.ninjas.cl/api/site/assets/files/3118/04082018091522gaviota_dominicana_leslie_brackenridge_b.jpg">
                # <img src="https://aves.ninjas.cl/api/site/assets/files/3121/18082018075423perrito_pedro_valencia_web.jpg">
                # <img src="https://aves.ninjas.cl/api/site/assets/files/3124/06082018101359pilpilen_leslie_brackenridge_b.jpg">
                # <img src="https://aves.ninjas.cl/api/site/assets/files/3126/13082018101547zarapito_pico_recto_leslie_brackenridge_web.jpg">    


html = html_template.substitute(body = imagenes)

# Vamos a guardarlo en un archivo .html
with open('birds.html', 'w') as f:
    f.write(html)