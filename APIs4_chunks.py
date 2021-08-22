import requests
import json

if __name__ =='main':
    url='https://static.vix.com/es/sites/default/files/g/galaxia-nebulosas-astronomia-imagen-shutterstock.jpg'

    response=requests.get(url,stream=True)#Stream=True realiza la petición y deja la conexion abierta
    with open('imagen.jpg','wb') as file:
        for chunk in response.iter_content(): #.iter_content toma el contenido del servidor y lo descarga poco a poco
            file.write(chunk)
        file.close()
    
    response.close()#cierra la conexión
