from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Configuración del WebDriver de Selenium
driver = webdriver.Chrome()  # Asegúrate de tener el driver de Chrome instalado

# Abriendo la página
url = 'https://www.plazavea.com.pe/limpieza?page=2'
driver.get(url)

# Esperar a que se cargue el contenido dinámico (ajusta el tiempo según sea necesario)
time.sleep(5)  # Espera 5 segundos

# Obteniendo el contenido de la página
contenido_pagina = driver.page_source
driver.quit()

# Analizando con Beautiful Soup
soup = BeautifulSoup(contenido_pagina, 'html.parser')
divs_especificos = soup.find_all('div', class_='showcase-grid')

# Guardando los resultados
with open('divs_especificos.html', 'w', encoding='utf-8') as archivo:
    for div in divs_especificos:
        archivo.write(div.prettify())
        archivo.write('\n\n')