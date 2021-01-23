from logging import exception
from selenium import webdriver
from time import sleep
import random
from controller import Controller
from selenium.webdriver.common.keys import Keys
import re
from unicodedata import normalize

def scraping_ofertas(con, url_principal, prefix_url, sufix_url, pagina_inicial, cant_paginas, cant_ofertas, id_carga):
    controller = Controller()
    lista_oferta = []
    list_clean =[]
    #CADENA_BUSQUEDA = "analista programador"
    driver = webdriver.Chrome('services/chromedriver.exe')
    #driver.get("https://www.google.com/search?q="+CADENA_BUSQUEDA.replace(" ","+")+"&ibp=htl;jobs#htivrt=jobs")
    driver.get(prefix_url)
    scroll_empleos = driver.find_element_by_class_name("vWdgBe") # elemento que contiene la lista de empleos
    
    for x in range(0,cant_paginas):
        scroll_empleos.send_keys(Keys.END)
        sleep(0.5)

    scroll_empleos.send_keys(Keys.UP)

    grupos_de_empleos = driver.find_elements_by_class_name("nJXhWc") # elemento que contiene cada grupo de 10 empleos
    titulos =  driver.find_elements_by_class_name("BjJfJf") #elemento que contiene cada titulo

    for x in titulos:
        oferta = {}
        detalle2 = ""
        #print(x.text)
        c_detalle = driver.find_element_by_class_name("jolnDe")
        x.click()
        sleep(random.uniform(0.5,1))
        etiquetas = c_detalle.find_elements_by_class_name("sMzDkb")
        url = c_detalle.find_element_by_class_name("pMhGee").get_attribute('href')
        detalle = c_detalle.find_element_by_class_name("HBvzbc")
        
        try:
            masInfo = c_detalle.find_element_by_class_name("cVLgvc")
            masInfo.click()
            detalle2 = detalle.find_element_by_class_name("WbZuDe").text
            print ("s"+ detalle2)
        except:
            pass
        oferta["id_carga"] = id_carga
        oferta["url_pagina"] = prefix_url
        oferta["url"] = url
        oferta["puesto"] = x.text
        oferta["salario"]= ""
        oferta["detalle"]= detalle.text + detalle2
        try:
            oferta["empresa"]= etiquetas[0].text
            oferta["lugar"]= etiquetas[1].text
        except:
            oferta["lugar"]= ""
        lista_oferta.append(oferta)
        id = controller.registrar_oferta(con, oferta)

        PARRAFO = detalle.text.splitlines()
        
        for line in PARRAFO:
            line = line.strip()
            if(len(line)>0):
                if(not line[0].isalpha()):
                    line = line [1:]
                line=line.strip().upper()
                line =re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", line), 0, re.I)
                if (not line == ""):
                    desc={}
                    desc["id_oferta"]= id
                    desc["descripcion"]= line
                    list_clean.append(desc)

        controller.registrar_detalle_oferta(con, list_clean)
        #print(list_clean)
        #print()
        #print(row)  
    return lista_oferta 
