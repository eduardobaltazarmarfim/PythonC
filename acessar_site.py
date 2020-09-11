import urllib
import urllib.request

try:

    site=urllib.request.urlopen('https://www.demarchisaopaulo.com.br')

except urllib.request.URLError:

    print('Deu erro')

else:

    print('Deu certo')
   