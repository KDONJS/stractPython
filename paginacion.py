from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Configuración del WebDriver de Selenium
driver = webdriver.Chrome()

# Abriendo la página
url = 'https://www.plazavea.com.pe/limpieza?page=2'
driver.get(url)

# Esperar a que se cargue el contenido dinámico
time.sleep(5)

# Obteniendo el contenido de la página
contenido_pagina = driver.page_source
driver.quit()

# Analizando con Beautiful Soup
soup = BeautifulSoup(contenido_pagina, 'html.parser')
divs_especificos = soup.find_all('div', class_='HA Showcase Showcase--food')

# Procesando cada bloque
# Procesando cada bloque
for div in divs_especificos:
    # Extrayendo la imagen
    imagen = div.find('img', class_='showcase__image')['src'] if div.find('img', class_='showcase__image') else 'Imagen no disponible'

    # Extrayendo el texto de la marca
    marca_elemento = div.find('div', class_='Showcase__brand')
    marca = marca_elemento.get_text(strip=True) if marca_elemento else 'Marca no disponible'

    # Extrayendo el nombre del producto
    nombre_producto_elemento = div.find('a', class_='Showcase__name')
    nombre_producto = nombre_producto_elemento.get_text(strip=True) if nombre_producto_elemento else 'Producto no disponible'

    # Extrayendo el precio
    simbolo_moneda_elemento = div.find('span', class_='currency-symbol')
    simbolo_moneda = simbolo_moneda_elemento.get_text(strip=True) if simbolo_moneda_elemento else 'S/'

    precio_entero_elemento = div.find('span', class_='price')
    precio_entero = precio_entero_elemento.contents[1] if precio_entero_elemento and len(precio_entero_elemento.contents) > 1 else '0'

    precio_decimal_elemento = div.find('span', class_='decimal-price')
    precio_decimal = precio_decimal_elemento.get_text(strip=True) if precio_decimal_elemento else '00'

    precio = f"{simbolo_moneda}{precio_entero}{precio_decimal}"

    # Imprimiendo los resultados
    print(f"Imagen: {imagen}")
    print(f"Marca: {marca}")
    print(f"Producto: {nombre_producto}")
    print(f"Precio: {precio}")
    print("-------")