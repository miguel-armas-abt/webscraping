from dao import webscraping_dao
from models import webscraping

class WebScrapingService():

    def __init__(self):
        self.__webscraping_dao = webscraping_dao.WebscrapingDao

    def insert(self, webscraping: webscraping.WebScraping):
        self.__webscraping_dao.insert(webscraping)

    def scrap(self):
        print('')
