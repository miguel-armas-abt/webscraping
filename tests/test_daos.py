from models import webscraping
from models import oferta
from models import oferta_detalle
from models import ofertaperfil_tipo

from dao import oferta_dao
from dao import webscraping_dao
from dao import oferta_detalle_dao
from dao import ofertaperfil_dao, keyword_search_dao

from datetime import datetime


# #################################################### insertar webscraping
# wscraping = webscraping.WebScraping(
#     '',
#     None,
#     'google jobs',
#     'https://google.com',
#     'https://google.com/search?q=analista+programador&ibp=htl;jobs#htivrt=jobs',
#     1
# )
# print(webscraping_dao.WebscrapingDao().insert_then_return_latest_row(wscraping))
#
#
# #################################################### insertar oferta
# oferta = oferta.Oferta(
#     2,
#     'titulos test',
#     'empresa test',
#     'lugar test',
#     'tiempo publicado test',
#     'salario test',
#     'modalidad trabajo test',
#     'subarea test',
#     'url oferta test',
#     'url pagina test',
#     'area test',
#     datetime.now(),
#     datetime.now(),
#     'oferta detalle test',
#     datetime.now()
# )
# print(oferta_dao.OfertaDao().insert_then_return_latest_row(oferta))
#
#
#
# #################################################### insertar ofertaperfiltipo
# ofertaperfil_tipo = ofertaperfil_tipo.OfertaPerfilTipo(
#     1,
#     'y',
#     'n'
# )
# print(ofertaperfil_dao.OfertaDao().insert(ofertaperfil_tipo))
#
#
# #################################################### insertar ofertadetalle
# of_detalle = oferta_detalle.OfertaDetalle(
#     9,
#     'descripcion test',
#     'descripcion normalizada test',
#     3,
#     5,
#     datetime.now(),
#     datetime.now(),
#     1
# )
# print(oferta_detalle_dao.OfertaDetalleDao().insert_then_return_latest_row(of_detalle))

# print(keyword_search_dao.KeywordSearchDao().select_keyword_search())

print(oferta_dao.OfertaDao().existe_registro("a104ddc4dbc15936cdf41e125728c451"))