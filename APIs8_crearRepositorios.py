import requests

if __name__=='__main__':
    client_id='88a40bae1ed73e297ca3'

client_secret= '3dc49c8551e406198caa9dd9e37ea12642caa82b'

code='cfa0b260c5e36d95f788' 
access_token='f23b879642b20714fcb56f0f2014c6f9825c7da9'
url='http://api.github.com/user/repos'

payload={'name':'git_api_cf_comunidad567'}
headers={'Accept':'application/json','Authorization':'token'+ access_token}

response=requests.post(url,headers=headers,json=payload)

if response.status_code==200:
    print(response.json())
else:
        content=response.content
        print(str(content).replace('\\n', '\n'))