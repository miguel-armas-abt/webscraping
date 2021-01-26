from repositories import repository
from models import oferta

class OfertaDao():

    def __init__(self):
        self.__repository = repository.Repository()

    def insert_then_return_latest_row(self, oferta):
        # defino las sentencia sql
        sql_insert = "INSERT INTO public.oferta(id_webscraping, titulo, empresa, lugar, tiempo_publicado, " \
                     "salario, modalidad_trabajo, subarea, url_oferta, url_pagina, area, fecha_creacion, " \
                     "fecha_modificacion, oferta_detalle, fecha_publicacion, id_anuncioempleo) " \
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        sql_select_last = "SELECT last_value FROM oferta_id_oferta_seq"

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
            oferta.getOfertaFechaPublicacion(),
            oferta.getIdAnuncioEmpleo())

        return self.__repository.insert_then_return_latest_row(params, sql_insert, sql_select_last)

    def existe_registro(self, id_anuncioempleo):
        # defino las sentencia sql
        sql_select = "SELECT EXISTS (SELECT id_anuncioempleo FROM public.oferta WHERE id_anuncioempleo = %s);"

        # obtengo los parametros para la query sql
        params = (id_anuncioempleo,)

        return self.__repository.existe_registro(params, sql_select)[0]