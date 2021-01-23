class keywordSearch():

    def __init__(self, descripcion, id_tipokeyword):
        self.__descripcion=descripcion
        self.__id_tipokeyword=id_tipokeyword


    ## setters

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def setId_tipokeyword(self, id_tipokeyword):
        self.__id_tipokeyword = id_tipokeyword

    ## getters

    def getDescripcion(self):
        return self.__descripcion

    def getId_tipokeyword(self):
        return self.__id_tipokeyword

