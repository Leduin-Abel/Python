import requests

if __name__=='__main__':
    url='https://api.github.com/user'

    session=requests.session()#objeto tipo session
    session.auth=('flabper@gmail.com','leduinabel1008')

    response=session.get(url)

    if response.ok:
        content=response.content
        print(str(content).replace('\\n', '\n'))

        print('\n', response.cookies)
        
