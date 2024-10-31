import os
import csv
from getpass import getpass

from bs4i mport BeautifulSoup

URL = 'https://github.com/trending'
response = requests.get(URL)

if response.status_code == 200:
    print("Requisição bem-sucedida!")
else:
    print("Falha na requisição:", response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar os 10 primeiros projetos na página
projects = soup.find_all('article', class_='Box-row')[:10]

# Lista para armazenar os dados
project_data = []

# Iterar sobre os projetos encontrados e extrair as informações necessárias
for idx, project in enumerate(projects, start=1):
    project_name = project.h2.a.get_text(strip=True).replace("\n", "").replace(" ", "")
    
    language = project.find('span', itemprop='programmingLanguage')
    language = language.get_text(strip=True) if language else "N/A"
    
    stars = project.find('a', class_='Link--muted d-inline-block mr-3')
    stars = stars.get_text(strip=True).replace(',', '') if stars else "0"
    
    forks = project.find_all('a', class_='Link--muted d-inline-block mr-3')
    forks = forks[1].get_text(strip=True).replace(',', '') if len(forks) > 1 else "0"
    
    stars_today = project.find('span', class_='d-inline-block float-sm-right')
    stars_today = stars_today.get_text(strip=True).split()[0].replace(',', '') if stars_today else "0"
    
    # Adicionar os dados à lista
    project_data.append([idx, project_name, language, stars, stars_today, forks])

# Exibir os dados extraídos
for data in project_data:
    print(data)

filename = 'github.csv'

with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['ranking', 'project', 'language', 'stars', 'stars today', 'forks'])
    writer.writerows(project_data)
