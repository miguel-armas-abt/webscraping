class keywordSearch():

    def __init__(self, id_keyword, descripcion, id_tipokeyword):
        self.__id_keyword=id_keyword
        self.__descripcion=descripcion
        self.__id_tipokeyword=id_tipokeyword


    ## setters

    def setId_keyword(self, id_keyword):
        self.__id_keyword = id_keyword

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def setId_tipokeyword(self, id_tipokeyword):
        self.__id_tipokeyword = id_tipokeyword

    ## getters
    def getId_keyword(self):
        return self.__id_keyword

    def getDescripcion(self):
        return self.__descripcion

    def getId_tipokeyword(self):
        return self.__id_tipokeyword

