from time import sleep
import random
import re
from unicodedata import normalize
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from properties.configuration import *

from services import oferta_service
from services import oferta_detalle_service

from models import webscraping
from models import oferta as ofertaModelo
from models import oferta_detalle

from dao import webscraping_dao


class WebScrapingService():

    def __init__(self):
        self.__wscraping_dao = webscraping_dao.WebscrapingDao()
        self.__of_service = oferta_service.OfertaService()
        self.__of_detalle_service = oferta_detalle_service.OfertaDetalleService()

    def insert_then_return_latest_row(self, webscraping: webscraping.WebScraping):
        return self.__wscraping_dao.insert_then_return_latest_row(webscraping)

    def scrape_request(self):
        pagina_web = GOOGLE_JOBS["WS_PORTAL_LABORAL"]               ## google jobs
        numero_paginas = GOOGLE_JOBS["WS_PAGINAS"]                  ## 0
        numero_pagina_inicio = GOOGLE_JOBS["WS_PAGINA_INICIAL"]     ## 1
        numero_ofertas = GOOGLE_JOBS["WS_OFERTAS"]                  ## None
        area_filtro = GOOGLE_JOBS["WS_AREA"]                        ## None
        url_pagina = GOOGLE_JOBS["WS_PORTAL_LABORAL_URL"]           ## https://google.com

        ## incrusto mi keyword search en la url
        url_busqueda = "/search?q=analista+programador&ibp=htl;jobs#htivrt=jobs"
        url_busqueda = url_pagina + url_busqueda

        ## inserto el registro de webscraping
        wscraping = webscraping.WebScraping(
            '',                         # busqueda
            None,                       # busqueda_area
            pagina_web,                 # pagina_web
            url_pagina,                 # url_pagina
            url_busqueda,               # url_busqueda
            1                           # id_keyword
        )
        id_webscraping_insert = self.insert_then_return_latest_row(wscraping)

        listaOferta = self.scrape(url_pagina, url_busqueda, "", numero_pagina_inicio, numero_paginas, numero_ofertas, id_webscraping_insert)

        """"
        webscraping_googleJobs.scraping_ofertas(con, carga["url_principal"], carga["url_prefix"],
                                                          carga["url_sufix"],
                                                          carga["pagina_inicial"], carga["cant_paginas"],
                                                          carga["cant_ofertas"],
                                                          carga["id_carga"])
        """

    def scrape(self, url_principal, prefix_url, sufix_url, pagina_inicial, cant_paginas, cant_ofertas, id_carga):
        lista_oferta = []
        list_clean = []

        # CADENA_BUSQUEDA = "analista programador"
        driver = webdriver.Chrome('./chromedriver.exe')
        driver.get(prefix_url)
        scroll_empleos = driver.find_element_by_class_name("vWdgBe")  # elemento que contiene la lista de empleos

        for x in range(0, cant_paginas):
            scroll_empleos.send_keys(Keys.END)
            sleep(0.5)

        scroll_empleos.send_keys(Keys.UP)

        grupos_de_empleos = driver.find_elements_by_class_name(
            "nJXhWc")  # elemento que contiene cada grupo de 10 empleos
        titulos = driver.find_elements_by_class_name("BjJfJf")  # elemento que contiene cada titulo

        for x in titulos:
            oferta = {}
            detalle2 = ""
            # print(x.text)
            c_detalle = driver.find_element_by_class_name("jolnDe")
            x.click()
            sleep(random.uniform(0.5, 1))
            etiquetas = c_detalle.find_elements_by_class_name("sMzDkb")
            url = c_detalle.find_element_by_class_name("pMhGee").get_attribute('href')
            detalle = c_detalle.find_element_by_class_name("HBvzbc")

            try:
                masInfo = c_detalle.find_element_by_class_name("cVLgvc")
                masInfo.click()
                detalle2 = detalle.find_element_by_class_name("WbZuDe").text
                print("s" + detalle2)
            except:
                pass

            ofer = ofertaModelo.Oferta(
                id_carga,                   # id_webscraping
                'titulos test',
                'empresa test',
                'lugar test',
                'tiempo publicado test',
                'salario test',
                'modalidad trabajo test',
                'subarea test',
                url,                        # url oferta
                prefix_url,                 # url pagina
                x.text,                     # puesto? -> area
                datetime.now(),
                datetime.now(),
                detalle.text + detalle2,    # detalle
                datetime.now()
            )

            """
            oferta["id_carga"] = id_carga
            oferta["url_pagina"] = prefix_url
            oferta["url"] = url
            oferta["puesto"] = x.text
            oferta["salario"] = ""
            oferta["detalle"] = detalle.text + detalle2
            """
            try:
                """"
                oferta["empresa"] = etiquetas[0].text
                oferta["lugar"] = etiquetas[1].text
                """
                ofer.setEmpresa(etiquetas[0].text)
                ofer.setLugar(etiquetas[1].text)
            except:
                oferta["lugar"] = ""
            lista_oferta.append(oferta)

            id_oferta_insert = self.__of_service.insert_then_return_latest_row(ofer)    ## setear oferta
            #id = controller.registrar_oferta(con, oferta)

            PARRAFO = detalle.text.splitlines()

            for line in PARRAFO:
                line = line.strip()
                if (len(line) > 0):
                    if (not line[0].isalpha()):
                        line = line[1:]
                    line = line.strip().upper()
                    line = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
                                  normalize("NFD", line), 0, re.I)
                    if (not line == ""):
                        ofer_detalle = oferta_detalle.OfertaDetalle(
                            id,                             # id_oferta
                            line,                           # descripcion
                            'descripcion normalizada test',
                            3,
                            5,
                            datetime.now(),
                            datetime.now(),
                            1
                        )
                        #desc = {}
                        #desc["id_oferta"] = id
                        #desc["descripcion"] = line
                        #list_clean.append(desc)

            id_oferta_detalle_insert = self.__of_detalle_service.insert_then_return_latest_row(ofer_detalle)      ## setear of_detalle
            #controller.registrar_detalle_oferta(con, list_clean)
            # print(list_clean)
            # print()
            # print(row)
        return lista_oferta

WebScrapingService().scrape_request()