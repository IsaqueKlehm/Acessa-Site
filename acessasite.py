import os

# Coloca apenas o nome Exemplo: youtube (ja auto completa com youtube.com)
site = input('Digite o site: ')

os.system(f'start chrome https://{site.lower().replace(' ', '')}.com')