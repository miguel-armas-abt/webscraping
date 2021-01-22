from repositories import webscraping_repository
from models import webscraping

wscraping = webscraping.WebScraping(
    '',
    None,
    'google jobs',
    'https://google.com',
    'https://google.com/search?q=analista+programador&ibp=htl;jobs#htivrt=jobs',
    1
)

db = webscraping_repository.WebscrapingRepository()
print(db.insert_webscraping2(wscraping))
