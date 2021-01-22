from repositories import repository
from models import oferta_detalle

class OfertaDetalleDao():

    def __init__(self):
        self.__repository = repository.Repository()

    def insert(self, oferta_detalle: oferta_detalle.OfertaDetalle):
        # defino las sentencia sql
        sql_insert = "INSERT INTO public.oferta_detalle(id_oferta, descripcion, descripcion_normalizada, ind_activo," \
                     " motivo_inactivo, fecha_creacion, fecha_modificacion, ofertaperfil_id) " \
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

        params = (
            oferta_detalle.getIdOferta(),
            oferta_detalle.getDescripcion(),
            oferta_detalle.getDescripcionNormalizada(),
            oferta_detalle.getIndActivo(),
            oferta_detalle.getMotivoInactivo(),
            oferta_detalle.getFechaCreacion(),
            oferta_detalle.getFechaModificacion(),
            oferta_detalle.getOfertaPerfilId()
            )

        self.__repository.insert(params, sql_insert)