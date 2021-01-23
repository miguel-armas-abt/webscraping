from models import webscraping
from models import oferta
from models import oferta_detalle
from models import ofertaperfil_tipo

from services import oferta_service
from services import oferta_detalle_service
from services import webscraping_service

from datetime import datetime

#################################################### insertar webscraping
wscraping = webscraping.WebScraping(
    '',
    None,
    'google jobs',
    'https://google.com',
    'https://google.com/search?q=analista+programador&ibp=htl;jobs#htivrt=jobs',
    1
)
print(webscraping_service.WebScrapingService().insert_then_return_latest_row(wscraping))


#################################################### insertar oferta
oferta = oferta.Oferta(
    2,
    'titulos test',
    'empresa test',
    'lugar test',
    'tiempo publicado test',
    'salario test',
    'modalidad trabajo test',
    'subarea test',
    'url oferta test',
    'url pagina test',
    'area test',
    datetime.now(),
    datetime.now(),
    'oferta detalle test',
    datetime.now()
)
print(oferta_service.OfertaService().insert_then_return_latest_row(oferta))



#################################################### insertar ofertadetalle
of_detalle = oferta_detalle.OfertaDetalle(
    9,
    'descripcion test',
    'descripcion normalizada test',
    3,
    5,
    datetime.now(),
    datetime.now(),
    1
)
print(oferta_detalle_service.OfertaDetalleService().insert_then_return_latest_row(of_detalle))
