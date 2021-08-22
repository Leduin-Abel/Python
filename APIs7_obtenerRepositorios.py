import requests

client_id='88a40bae1ed73e297ca3'

client_secret= '3dc49c8551e406198caa9dd9e37ea12642caa82b'

code='cfa0b260c5e36d95f788' #me da el token de acceso
access_token='f23b879642b20714fcb56f0f2014c6f9825c7da9'

if __name__=='__main__':
    url='http://api.github.com/user/repos'
    headers={'Authorization':'token f23b879642b20714fcb56f0f2014c6f9825c7da9'}

response=requests.get(url, headers=headers)

if response.status_code==200:
    payload=response.json()
    
    for project in payload:
        name=project['name']
        print(name)
else:
    content=response.content
    print(str(content).replace('\\n', '\n'))