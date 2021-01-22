from repositories import repository
from models import ofertaperfil_tipo

class OfertaDao():

    def __init__(self):
        self.__repository = repository.Repository()

    def insert(self, ofertaperfil: ofertaperfil_tipo.OfertaPerfilTipo):
        # defino las sentencia sql
        sql_insert = "INSERT INTO ofertaperfil_tipo(ofertaperfil_id, ofertaperfil_desc, ofertaperfil_min) " \
                     "VALUES (%s, %s, %s);"

        # obtengo los parametros para la query sql
        params = (
            ofertaperfil.getOfertaPerfilId(),
            ofertaperfil.getOfertaPerfilDesc(),
            ofertaperfil.getOfertaPerfilMin())

        self.__repository.insert(params, sql_insert)