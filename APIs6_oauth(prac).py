#protocolo oauth sirve para metodos de autenticacion utilizando terceros

import requests

client_id='88a40bae1ed73e297ca3'

client_secret= '3dc49c8551e406198caa9dd9e37ea12642caa82b'

code='ca8cb7e88a49f9e5a5e1' #me da el token de acceso
#access_token='f23b879642b20714fcb56f0f2014c6f9825c7da9' #el token del usuario autenticado, me permite obtener la info del usuario
#https://github.com/login/oauth/authorize?client_id=88a40bae1ed73e297ca3&scope=repo #url de auntenticación
if __name__=='__main__':
    url='https://github.com/login/oauth/access_token'
    
    payload={'client_id':client_id,'client_secret':client_secret,'code':code}
    headers={'Accept':'application/json'}
    response=requests.post(url,json=payload,headers=headers)

    if response.status_code==200:
        response_json=response.json()

        access_token=response_json['access_token']



        

        

        print(access_token)
