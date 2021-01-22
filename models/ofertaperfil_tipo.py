class OfertaPerfilTipo():

    def __init__(self, ofertaperfil_id, ofertaperfil_desc, ofertaperfil_min):
        self.__ofertaperfil_id = ofertaperfil_id
        self.__ofertaperfil_desc = ofertaperfil_desc
        self.__ofertaperfil_min = ofertaperfil_min

    ## getters
    def getOfertaPerfilId(self):
        return self.__ofertaperfil_id

    def getOfertaPerfilDesc(self):
        return self.__ofertaperfil_desc

    def getOfertaPerfilMin(self):
        return self.__ofertaperfil_min