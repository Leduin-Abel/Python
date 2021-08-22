import requests
import json

if __name__=='__main__':
    url='http://httpbin.org/put'
    payload={'nombre':'Leduin','curso':'python','nivel':'bajo'}
    headers={'Content-Type':'application/json','access-token':'12345'}

    response=requests.put(url,data=json.dumps(payload),headers=headers) #actualiza informacion

    print(response.url)

    if response.status_code==200:
        #content=response.content
        #print(str(content).replace('\\n', '\n'))
        #lectura encabezados
        headers_response=response.headers #Dic
        #print(str(headers_response).replace('\\n','\n'))
        server=headers_response['Server']
        print(server)

if __name__=='__main__':
    url='http://httpbin.org/delete'
    payload={'nombre':'Leduin','curso':'python','nivel':'bajo'}
    headers={'Content-Type':'application/json','access-token':'12345'}

    response=requests.delete(url,data=json.dumps(payload),headers=headers)#borra informacion

    print(response.url)

    if response.status_code==200:
        #content=response.content
        #print(str(content).replace('\\n', '\n'))
        #lectura encabezados
        headers_response=response.headers #Dic
       # print(str(headers_response).replace('\\n','\n'))
        server=headers_response['Server']
        print(server)