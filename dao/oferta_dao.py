from repositories import repository
from models import oferta

class OfertaDao():

    def __init__(self):
        self.__repository = repository.Repository()

    def insert(self, oferta):
        # defino las sentencia sql
        sql_insert = "INSERT INTO public.oferta(id_webscraping, titulo, empresa, lugar, tiempo_publicado, " \
                     "salario, modalidad_trabajo, subarea, url_oferta, url_pagina, area, fecha_creacion, " \
                     "fecha_modificacion, oferta_detalle, fecha_publicacion) " \
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        # obtengo los parametros para la query sql
        params = (
            oferta.getId_webscraping(),
            oferta.getTitulo(),
            oferta.getEmpresa(),
            oferta.getLugar(),
            oferta.getTiempo_publicado(),
            oferta.getSalario(),
            oferta.getModalidad_trabajo(),
            oferta.getSubarea(),
            oferta.getUrl_oferta(),
            oferta.getUrl_pagina(),
            oferta.getArea(),
            oferta.getFecha_creacion(),
            oferta.getFecha_modificacion(),
            oferta.getOferta_detalle(),
            oferta.getOfertaFechaPublicacion())

        self.__repository.insert(params, sql_insert)