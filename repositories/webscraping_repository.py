from dbconnection import Connection

class WebscrapingRepository():

    def __init__(self):
        self.__conexion = Connection()

    def insert_webscraping(self, webscraping):
        last_row_id = 0
        try:
            # defino la sentencia sql
            sql_insert = "INSERT INTO webscraping (busqueda, busqueda_area, pagina_web, url_pagina, url_busqueda,fecha_creacion,fecha_modificacion, id_keyword)" \
                         "VALUES (%s, %s, %s, %s, %s, current_date, current_date, %s)"

            sql_select_last = "SELECT last_value FROM webscraping_id_webscraping_seq"

            # obtengo los parametros para la query sql
            params = (
                webscraping.getBusqueda(),
                webscraping.getBusquedaArea(),
                webscraping.getPagina_web(),
                webscraping.getUrl_pagina(),
                webscraping.getUrl_busqueda(),
                webscraping.getId_keyword())

            # conecto a base de datos
            database = self.__conexion.connect()

            # ejecuto la query
            cursor = database.cursor()
            cursor.execute(sql_insert, params)

            # confirmo cambios
            database.commit()
            print("Sentencia ejecutada ejecutada")

            # obtengo el id del ultimo registro insertado
            cursor.execute(sql_select_last)
            last_row_id = int(cursor.fetchone()[0])

        except:
            # revertir en caso de error
            print("Error!, rollback")
            database.rollback()

        database.close()
        return last_row_id