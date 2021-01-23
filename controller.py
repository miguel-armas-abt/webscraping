import preprocessing
from nltk import word_tokenize
from dboperation import DBOferta
from dboperation import DBOfertadetalle
from dboperation import DBKeywordSearch
from dao import webscraping_dao
from models import webscraping

class Controller:
    def __init__(self):
        self.dbwebscraping = webscraping_dao.WebscrapingDao()
        self.dboferta = DBOferta()
        self.dbofertadetalle = DBOfertadetalle()
        self.dbkeywordsearch = DBKeywordSearch()

    def registrar_webscraping(self, webscrapingTupla):

        webscrapingModel = webscraping.WebScraping(
            webscrapingTupla["busqueda"],
            webscrapingTupla["busqueda_area"],
            webscrapingTupla["pagina"],
            webscrapingTupla["url_principal"],
            webscrapingTupla["url_prefix"],
            1
        )
        id = self.dbwebscraping.insert_then_return_latest_row(webscrapingModel)
        return id

    def registrar_oferta(self, con, oferta):        
        return self.dboferta.insert_oferta(con, oferta)

    ##metodo añadido para insertar las tuplas del detalle de la oferta
    def registrar_detalle_oferta(self, con, listaDetalle):
        #print(listaDetalle)
        for detalle in listaDetalle:
            print("----------------analizando el detalle en tuplas---------------------")
            print(detalle)
            idOfertaDetalle=self.dbofertadetalle.insertOfertaDetalle(con, detalle)            

    def registrar_ofertas(self, con, lista_oferta):
        print(len(lista_oferta))
        for oferta in lista_oferta:
            print("----------------analizando que hay en lista oferta---------------------")
            print(oferta)
            idPuesto = self.dboferta.insert_oferta(con, oferta)     

    def generar_insert_ofertadetalle(self, oferta):
        sql_insert = "INSERT INTO OFERTA_DETALLE (id_oferta,descripcion,fecha_creacion,fecha_modificacion) VALUES (%s,'%s',sysdate,sysdate);"
        sql_result = ""
        for ed in oferta["listaDescripcion"]:
            sql = sql_insert % (oferta["idPuesto"], ed)
            sql_result = sql_result + sql
        return sql_result

    def registrar_normalizado(self, con, lista):
        for element in lista:
            new_words = preprocessing.normalize_words(word_tokenize(element["descripcion"]))
            descripcion_normalizada = " ".join(new_words)
            element["descripcion_normalizada"] = descripcion_normalizada
        # DBOfertadetalle.update_requisito(con, element)

    #prepara descripcion en una lista de diccionarios para el insert en oferta_detalle
    def analizaSegundoLi(self,tuplas, row):
        tuplafinal=[]
        avisotupla=str(tuplas).replace("<li>","").replace("</li>","").split("<br/>")
        for aviso in avisotupla:
            a={}
            if aviso.strip():
                a["id_oferta"]= row
                a["descripcion"]=aviso.strip()
                tuplafinal.append(a)
        return tuplafinal
    
    def obtenerpalabrasClave (self,con):
        return self.dbkeywordsearch.get_KeywordSearch(con)
