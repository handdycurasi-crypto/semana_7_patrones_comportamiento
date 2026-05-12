class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"{self.nombre} recibio una notificacion: {mensaje}")


class Chat:
    def __init__(self):
        self.usuarios = []

    def registrar(self, usuario):
        self.usuarios.append(usuario)

    def eliminar(self, usuario):
        self.usuarios.remove(usuario)

    def notificar(self, mensaje):
        for usuario in self.usuarios:
            usuario.actualizar(mensaje)


chat = Chat()

usuario1 = Usuario("Handdy")
usuario2 = Usuario("Carlos")
usuario3 = Usuario("Lucia")

chat.registrar(usuario1)
chat.registrar(usuario2)
chat.registrar(usuario3)

chat.notificar("Nuevo mensaje en el grupo de POO2")
