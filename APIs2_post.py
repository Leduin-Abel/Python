import requests
import json

#uso posts
"""if __name__=='__main__':
    url='http://httpbin.org/post'
    payload={'nombre':'Leduin','curso':'python','nivel':'bajo'}

    response=requests.post(url, json=payload) #crear recursos dentro del servidor
    #si hago data=payload, no se serializa y se envia dentro de forms
    #si hago data= json.dumps(payload) se serializa y se envia dentro de data
    if response.status_code==200:
        content=response.content
        print(str(content).replace('\\n', '\n')) """

#headers
if __name__=='__main__':
    url='http://httpbin.org/post'
    payload={'nombre':'Leduin','curso':'python','nivel':'bajo'}
    headers={'Content-Type':'application/json','access-token':'12345'}

    response=requests.post(url,data=json.dumps(payload),headers=headers)

    print(response.url)

    if response.status_code==200:
        #content=response.content
        #print(str(content).replace('\\n', '\n'))
        #lectura encabezados
        headers_response=response.headers #Dic
        print(str(headers_response).replace('\\n','\n'))
        server=headers_response['Server']
        print(server)


