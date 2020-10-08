import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time


with open ('who_watches_colab55.txt', 'w') as whc:
    while True:
        try:
            response = requests.get('https://www.colab55.com/@tobefonseca/tees/love-is-art-frida-kahlo-and-van-gogh')

            soup = BeautifulSoup(response.text, 'html.parser')

            texto_usuarios_olhando = soup.find_all('td')[15].text
            numero_usuarios_olhando = texto_usuarios_olhando[texto_usuarios_olhando.\
                find('Mais de ') + len('Mais de ') : texto_usuarios_olhando.find('pessoas') - 1]

            whc.write(numero_usuarios_olhando + '\t' + str(datetime.now()) +'\n')
            whc.flush()
                
            print(numero_usuarios_olhando)

        except:
            whc.write('ERRO' + '\n')
            
        time.sleep(30)
