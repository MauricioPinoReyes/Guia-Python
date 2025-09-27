class Persona():
    def __init__(self,id,nombre,edad):
        self.id=id
        self.nombre=nombre
        self.edad=edad
    
    def mostrarPersona(self):
        return "["+str(self.id)+"] ["+self.nombre+"] ["+str(self.edad)+"]"
