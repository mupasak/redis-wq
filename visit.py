from bs4 import BeautifulSoup
from urllib import request
import lxml

def visit(vis):
    print('1111')
    url = request.urlopen(vis)
    print ('22222')
    soup = BeautifulSoup(url.read().decode(), "lxml")
    print ('33333')
    text = None
    for data in soup.find_all('div'):
        text = data.text
        print(text)
    return text
