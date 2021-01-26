from dao import oferta_dao
from models import oferta


class OfertaService():

    def __init__(self):
        self.__oferta_dao = oferta_dao.OfertaDao()

    def insert_then_return_latest_row(self, oferta: oferta.Oferta):
        if self.existe_registro(self, '1'):
            return 'No se registra'
        else:
            return self.__oferta_dao.insert_then_return_latest_row(oferta)

    def existe_registro(self, id_anuncioempleo):
        return self.__oferta_dao.existe_registro(id_anuncioempleo)
