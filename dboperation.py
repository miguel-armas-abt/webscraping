import psycopg2

class DBWebscraping:
    def __init__(self):
        pass

class DBOferta:
    def __init__(self):
        pass

    def insert_oferta(self, connection, oferta):        
        try:
            mydb = connection.connect()
            cur = mydb.cursor()                                    
            sql = "insert into Oferta (id_webscraping, titulo,empresa,lugar,salario,oferta_detalle,url_oferta,url_pagina,fecha_creacion,fecha_modificacion) values (%s,%s,%s,%s,%s,%s,%s,%s,current_date,current_date)"            
            params = (oferta["id_carga"], oferta["puesto"].strip(), oferta["empresa"].strip(), oferta["lugar"].strip(),oferta["salario"].strip(),oferta["detalle"].strip(), oferta["url"], oferta["url_pagina"])
            cur.execute(sql, params)        
            mydb.commit()            


            sql = "SELECT last_value FROM Oferta_id_Oferta_seq"
            cur.execute(sql)  
            row_id = int(cur.fetchone()[0])  
            
            # close the communication with the PostgreSQL
            cur.close()
            mydb.close()                           

        except (Exception, psycopg2.DatabaseError) as error:                
                print ("-------------Exception, psycopg2.DatabaseError-------------------")
                print (error)
                mydb.close()
                row_id = 0  # modificacion      
            
        return row_id


class DBOfertadetalle:
    def __init__(self):
        pass

    def update_ofertadetalle(self, connection, requisito):
        mydb = connection.connect()
        mycursor = mydb.cursor()
        sql = "UPDATE OFERTA_DETALLE SET descripcion_normalizada=:1 where id_ofertadetalle=:2"
        params = (requisito["descripcion_normalizada"], requisito["iddescripcion"])

        mycursor.execute(sql, params)
        mydb.commit()

    def insertOfertaDetalle(self, connection, detalle):
        try:
            mydb= connection.connect()
            mycursor= mydb.cursor()
            sql= "insert into oferta_detalle ( id_ofertadetalle, id_oferta, descripcion, fecha_creacion, fecha_modificacion) values (DEFAULT,%s,%s,current_date,current_date)"
            params= (detalle["id_oferta"],detalle["descripcion"])
            mycursor.execute(sql, params)
            mydb.commit()
            # close the communication with the PostgreSQL
            mycursor.close()
            mydb.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print ("-------------Exception, psycopg2.DatabaseError-------------------")
            print (error)
            mydb.close()
        
        return 1

class DBKeywordSearch:
    def __init__(self):
        pass

    def get_KeywordSearch(self, connection):
        keywords = []
        try:
            mydb = connection.connect()
            mycursor = mydb.cursor()
            sql = "SELECT * FROM KEYWORD_SEARCH"
            mycursor.execute(sql)
            keywords = mycursor.fetchall()
        except (Exception, psycopg2.Error) as error :
            print ("Error while fetching data from PostgreSQL", error)
        finally:
            if(mydb):
                mycursor.close()
                mydb.close()
                print("PostgreSQL connection is closed")
        return keywords

