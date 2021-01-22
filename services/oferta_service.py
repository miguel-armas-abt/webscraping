from dao import oferta_dao
from models import oferta

class OfertaService():

    def __init__(self):
        self.__oferta_dao = oferta_dao.OfertaDao()

    def insert(self, oferta: oferta.Oferta):
        self.__oferta_dao.insert(oferta)