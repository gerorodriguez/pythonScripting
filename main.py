from selenium import webdriver
import chromedriver_autoinstaller
import time
import helium as he
import csv
import json
import os

chromedriver_autoinstaller.install()
start = str(input("¿Desea buscar los precios de cables para instrumentos de cuerdas mas baratos o mas caros? Si la respuesta es mas baratos ingrese 'MIN' y si quiere lo contrario ingrese 'MAX':  ")).upper()
while start != 'MAX' and start != 'MIN':
    print("Respuesta invalida")
    start = str(input("¿Desea buscar los precios de cables para instrumentos de cuerdas mas baratos o mas caros? Si la respuesta es mas baratos ingrese 'MIN' y si quiere lo contrario ingrese 'MAX':  ")).upper()

# Minimo Precio -------------------M
if start == 'MIN':
    # Primera página: Todo Musica
    he.start_chrome(
        "https://todomusica.com.ar/6-musica/s-1/ofertas-oferta_del_mes")
    time.sleep(2)

    # Buscar los elementos de precio en descuento y referencia de producto
    precios_descuento_elements = he.find_all(he.S(".product-price"))
    referencias_elements = he.find_all(he.S(".product-reference"))

    # Obtener los precios y referencias de los primeros 5 productos en descuento
    productos_descuento = []
    for i in range(5):
        if i < len(precios_descuento_elements) and i < len(referencias_elements):
            precio_text = precios_descuento_elements[i].web_element.text
            referencia_text = referencias_elements[i].web_element.text
            productos_descuento.append(
                {"Referencia": referencia_text, "Precio": precio_text})

    # Segunda página: Kairon Music
    he.go_to(
        "https://www.kaironmusic.com.ar/cables-y-adaptadores-de-audio-y-video/?sort_by=price-ascending")
    time.sleep(2)

    # Buscar los elementos de nombre y precio de producto en Kairon Music
    nombres_productos_elements = he.find_all(
        he.S(".js-item-name.item-name.mb-3"))
    precios_productos_elements = he.find_all(
        he.S(".js-price-display.item-price"))

    # Obtener los nombres y precios de los primeros 5 productos en Kairon Music
    productos_kairon = []
    for i in range(5):
        if i < len(nombres_productos_elements) and i < len(precios_productos_elements):
            nombre_text = nombres_productos_elements[i].web_element.text
            precio_text = precios_productos_elements[i].web_element.text
            productos_kairon.append(
                {"Nombre": nombre_text, "Precio": precio_text})

    # Tercera página: Musica Pilar
    he.go_to("https://www.musicapilar.com.ar/shop?idRubro=21&sort=price&sort_type=asc")
    time.sleep(2)

    # Buscar los elementos de nombre y precio de producto en Musica Pilar
    nombres_pilar_elements = he.find_all(he.S(".item-description h2"))
    precios_pilar_elements = he.find_all(he.S(".finalPrice"))

    # Obtener los nombres y precios de los primeros 5 productos en Musica Pilar
    productos_pilar = []
    for i in range(5):
        if i < len(nombres_pilar_elements) and i < len(precios_pilar_elements):
            nombre_text = nombres_pilar_elements[i].web_element.text
            precio_text = precios_pilar_elements[i].web_element.text
            productos_pilar.append(
                {"Nombre": nombre_text, "Precio": precio_text})

    # Imprimir resultados de todas las páginas
    if productos_descuento:
        print("Productos en descuento de Todo Musica:")
        for producto in productos_descuento:
            print("Referencia:", producto["Referencia"])
            print("Precio:", producto["Precio"])
            print("-" * 30)
    else:
        print("No se encontraron productos en descuento en Todo Musica")

    if productos_kairon:
        print("-" * 30)
        print("Cambio de pagina...")
        print("-" * 30)
        print("-" * 30)
        print("Productos de Kairon Music:")
        for producto in productos_kairon:
            print("Nombre:", producto["Nombre"])
            print("Precio:", producto["Precio"])
            print("-" * 30)
    else:
        print("No se encontraron productos en Kairon Music")

    if productos_pilar:
        print("-" * 30)
        print("Cambio de pagina...")
        print("-" * 30)
        print("-" * 30)
        print("Productos de Musica Pilar:")
        for producto in productos_pilar:
            print("Nombre:", producto["Nombre"])
            print("Precio:", producto["Precio"])
            print("-" * 30)
    else:
        print("No se encontraron productos en Musica Pilar")

    with open('resultados_min.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Referencia', 'Precio']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for producto in productos_descuento:
            writer.writerow(producto)

    with open('resultados_min.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(productos_descuento, jsonfile, ensure_ascii=False, indent=4)

    os.system('start resultados_min.json')


# Maximo Precio -------------------
elif start == 'MAX':
    # Primera página: Todo Musica
    he.start_chrome(
        "https://todomusica.com.ar/module/iqitsearch/searchiqit?order=product.price.desc&s=CABLES+plug")
    time.sleep(2)

    # Buscar los elementos de precio en descuento y referencia de producto
    precios_descuento_elements = he.find_all(he.S(".product-price"))
    referencias_elements = he.find_all(he.S(".product-reference"))

    # Obtener los precios y referencias de los primeros 5 productos en descuento
    productos_descuento = []
    for i in range(5):
        if i < len(precios_descuento_elements) and i < len(referencias_elements):
            precio_text = precios_descuento_elements[i].web_element.text
            referencia_text = referencias_elements[i].web_element.text
            productos_descuento.append(
                {"Referencia": referencia_text, "Precio": precio_text})

    # Segunda página: Kairon Music
    he.go_to(
        "https://www.kaironmusic.com.ar/cables-y-adaptadores-de-audio-y-video/?sort_by=price-descending")
    time.sleep(2)

    # Buscar los elementos de nombre y precio de producto en Kairon Music
    nombres_productos_elements = he.find_all(
        he.S(".js-item-name.item-name.mb-3"))
    precios_productos_elements = he.find_all(
        he.S(".js-price-display.item-price"))

    # Obtener los nombres y precios de los primeros 5 productos en Kairon Music
    productos_kairon = []
    for i in range(5):
        if i < len(nombres_productos_elements) and i < len(precios_productos_elements):
            nombre_text = nombres_productos_elements[i].web_element.text
            precio_text = precios_productos_elements[i].web_element.text
            productos_kairon.append(
                {"Nombre": nombre_text, "Precio": precio_text})

    # Tercera página: Musica Pilar
    he.go_to(
        "https://www.musicapilar.com.ar/shop?idRubro=21&sort=price&sort_type=desc")
    time.sleep(2)

    # Buscar los elementos de nombre y precio de producto en Musica Pilar
    nombres_pilar_elements = he.find_all(he.S(".item-description h2"))
    precios_pilar_elements = he.find_all(he.S(".finalPrice"))

    # Obtener los nombres y precios de los primeros 5 productos en Musica Pilar
    productos_pilar = []
    for i in range(5):
        if i < len(nombres_pilar_elements) and i < len(precios_pilar_elements):
            nombre_text = nombres_pilar_elements[i].web_element.text
            precio_text = precios_pilar_elements[i].web_element.text
            productos_pilar.append(
                {"Nombre": nombre_text, "Precio": precio_text})

    # Imprimir resultados de todas las páginas
    if productos_descuento:
        print("Productos en descuento de Todo Musica:")
        for producto in productos_descuento:
            print("Referencia:", producto["Referencia"])
            print("Precio:", producto["Precio"])
            print("-" * 30)
    else:
        print("No se encontraron productos en descuento en Todo Musica")

    if productos_kairon:
        print("-" * 30)
        print("Cambio de pagina...")
        print("-" * 30)
        print("-" * 30)
        print("Productos de Kairon Music:")
        for producto in productos_kairon:
            print("Nombre:", producto["Nombre"])
            print("Precio:", producto["Precio"])
            print("-" * 30)
    else:
        print("No se encontraron productos en Kairon Music")

    if productos_pilar:
        print("-" * 30)
        print("Cambio de pagina...")
        print("-" * 30)
        print("-" * 30)
        print("Productos de Musica Pilar:")
        for producto in productos_pilar:
            print("Nombre:", producto["Nombre"])
            print("Precio:", producto["Precio"])
            print("-" * 30)
    else:
        print("No se encontraron productos en Musica Pilar")

    with open('resultados_max.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Referencia', 'Precio']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for producto in productos_descuento:
            writer.writerow(producto)

    with open('resultados_max.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(productos_descuento, jsonfile, ensure_ascii=False, indent=4)

    os.system('start resultados_max.json')

input("Presione ENTER para cerrar el programa...")

# Cerrar el navegador
he.kill_browser()
