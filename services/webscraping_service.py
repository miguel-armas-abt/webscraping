from dao import webscraping_dao
from models import webscraping

class OfertaService():

    def __init__(self):
        self.__webscraping_dao = webscraping_dao.WebscrapingDao

    def insert(self, webscraping: webscraping.WebScraping):
        self.__webscraping_dao.insert(webscraping)

