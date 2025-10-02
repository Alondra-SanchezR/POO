import os
os.system("cls")

# Clase Alumno
class Alumno:
    def __init__(self, nombre, edad, matricula):
        self.__nombre = nombre
        self.__edad = edad
        self.__matricula = matricula


    def inscribirse(self, curso):
        print(f"El alumno {self.__nombre} se ha inscrito a {curso.get_nombre()}")
        # return "El alumno se esta inscribiendo a un curso" 

    def estudiar(self):
        print(f"El alumno {self.__nombre} esta estudiando")


    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad 
    
    def get_matricula(self):
        return self.__matricula 
    
    #faltan setters

# Clase Profesor
class Profesor:
    def __init__(self, nombre, experiencia, num_profesor):
        self.__nombre = nombre
        self.__experiencia = experiencia
        self.__num_profesor = num_profesor

 
    def impartir(self, curso):
        print(f"El profesor {self.__nombre} imparte el curso de {curso.get_nombre()}")

    def evaluar(self, alumno):
        print(f"El profesor {self.__nombre} esta evaluando a {alumno.get_nombre()}")

 
    def get_nombre(self):
        return self.__nombre
    
    def get_experiencia(self):
        return self.__experiencia
    
    def get_num_profesor(self):
        return self.__num_profesor
    
# Clase Curso
class Curso:
    def __init__(self, nombre, codigo, creditos):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__creditos = creditos

    
    def asignar(self, profesor):
        print(f"El curso {self.__nombre} tiene al profesor {profesor.get_nombre()}")

  
    def get_nombre(self):
        return self.__nombre
    
    def get_codigo(self):
        return self.__codigo
    
    def get_creditos(self):
        return self.__creditos

# Alumnos
alumno1 = Alumno("Alondra Sánchez", 19, 3141240257)
alumno2 = Alumno("Abigail Rodríguez", 18, 3142561987)

# Profesores
profesor1 = Profesor("Alicia", 4, 243672)
profesor2 = Profesor("Juanito", 2, 222445)

# Cursos
curso1 = Curso("Algebra", 233, 54)
curso2 = Curso("Redes", 127, 52)
