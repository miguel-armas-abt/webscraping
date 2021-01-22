from dao import oferta_detalle_dao
from models import oferta_detalle

class OfertaService():

    def __init__(self):
        self.__oferta_detalle_dao = oferta_detalle_dao.OfertaDetalleDao()

    def insert(self, oferta_detalle: oferta_detalle.OfertaDetalle):
        self.__oferta_dao.insert(oferta_detalle)