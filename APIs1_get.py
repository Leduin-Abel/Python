import requests
import json

#if __name__=='__main__':
    #   url='https://www.google.com/' #hago solicitud a los servidores a google
    #  response=requests.get(url) #.get me devuelve un objeto tipo response, lo que es un status y se representa con un valor numerico
    #200 significa que todo bien

#if response.status_code==200:#ahí es donde se almacena el status
    #   content=response.content#Todo lo que contiene la pagina (html5)
    #  file=open('google.hmtl','wb')
    # file.write(content)
    #file.close()

#cambio de url/sin querys
#if __name__=='__main__':
 #   url='http://httpbin.org/get'
  #  response=requests.get(url)

   # if response.status_code==200:
    #    content=response.content
     #   print(content)

#utilizando querys
if __name__=='__main__':
    #url='http://httpbin.org/get?nombre=Leduin&curso=python'#esto no es optimo
    url='http://httpbin.org/get'
    args={'nombre':'Leduin','curso':'python','nivel':'bajo'}
    #response=requests.get(url)
    response=requests.get(url,params=args) #con esto el metodo se encarga de tomar los argumentos y ponerlos dentro de la url
    print(response.url)
    if response.status_code==200:
        #content=response.content
        #print(str(content).replace('\\n', '\n'))

        #obtener JSON sin libreria JSON
        #response_json=response.json() #Dic
        #origin=response_json['origin']
        #print(origin)

        #Obtener JSON con libreria JSON
        response_json=json.loads(response.text)
        origin=response_json['origin']
        print(origin)
