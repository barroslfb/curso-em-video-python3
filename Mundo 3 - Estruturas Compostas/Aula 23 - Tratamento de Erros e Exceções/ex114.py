import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://www.pudim.com.br/")
except urllib.error.URLError:
    print("O site Pudim não está acessível no momento.")
else:
    print("O site do pudim está no ar!")