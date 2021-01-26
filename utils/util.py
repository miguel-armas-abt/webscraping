class Utils():

    def limpiar_cadena(self, cadena):
        return cadena.replace(" ","+")

    def obtenerModalidad(self, parrafo, titulo):
        for linea_descripcion in parrafo:
            linea_descripcion = linea_descripcion.strip()
            if self.isModalidad(linea_descripcion, titulo) == "REMOTO":
                return "Remoto"
            if self.isModalidad(linea_descripcion, titulo) == "PRESENCIAL":
                return "Presencial"

    def obtenerSalario(self, parrafo):
        for linea_descripcion in parrafo:
            linea_descripcion = linea_descripcion.strip()
            if self.isSalario(linea_descripcion):
                return linea_descripcion

    def isModalidad(self, lineaTexto, titulo):
        modalidad_remoto = ["REMOTO", "REMOTA", "TELETRABAJO"]
        modalidad_presencial = ["PRESENCIAL"]
        for modalidad in modalidad_remoto:
            if (modalidad.lower() in lineaTexto.lower()) or (modalidad.lower() in titulo.lower()):
                return "REMOTO"

        for modalidad in modalidad_presencial:
            if (modalidad.lower() in lineaTexto.lower()):
                return "PRESENCIAL"

    def isSalario(self, lineaTexto):
        salario_keywords = ["SUELDO", "SALARIO", "REMUNERACION", "REMUNERACIÓN", "ESTIPENDIO"
                            "RETRIBUCION", "RETRIBUCIÓN", "HONORARIO", "GRATIFICACION",
                            "GRATIFICACIÓN", "SUBVENCION", "SUBVENCIÓN", "PENSION", "PENSIÓN"]
        for salario in salario_keywords:
            if (salario.lower() in lineaTexto.lower()):
                return True



# print(Utils().obtenerModalidad("Oferta laboral \n modo presencial \n fin de oferta".splitlines(), "titulooooo"))
# print(Utils().isModalidad2("Oferta laboral \n modo presencial \n fin de oferta", "titulooooo"))

print(Utils().obtenerSalario("Oferta laboral \n modo presencial \n salrio s/5000".splitlines()))