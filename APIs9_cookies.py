import requests

if __name__=='__main__':
    url='http://httpbin.org/cookies'
    cookies={'my-cookie':'true'}
    response=requests.get(url,cookies=cookies)

    if response.ok: #.ok devuelve verdadero o falso dependiendo de si todo salió bien
        cookies=response.cookies
        content=response.content
        print(str(content).replace('\\n', '\n'))
