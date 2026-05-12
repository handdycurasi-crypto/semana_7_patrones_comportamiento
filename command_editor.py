class Command:
    def ejecutar(self):
        pass

    def deshacer(self):
        pass


class EditorTexto:
    def __init__(self):
        self.contenido = ""

    def escribir(self, texto):
        self.contenido += texto

    def borrar(self, cantidad):
        self.contenido = self.contenido[:-cantidad]

    def guardar(self):
        print("Documento guardado:", self.contenido)


class EscribirCommand(Command):
    def __init__(self, editor, texto):
        self.editor = editor
        self.texto = texto

    def ejecutar(self):
        self.editor.escribir(self.texto)

    def deshacer(self):
        self.editor.borrar(len(self.texto))


class GuardarCommand(Command):
    def __init__(self, editor):
        self.editor = editor

    def ejecutar(self):
        self.editor.guardar()

    def deshacer(self):
        print("La accion guardar no se puede deshacer")


class Invocador:
    def __init__(self):
        self.historial = []

    def ejecutar(self, comando):
        comando.ejecutar()
        self.historial.append(comando)

    def deshacer(self):
        if len(self.historial) > 0:
            comando = self.historial.pop()
            comando.deshacer()


editor = EditorTexto()
invocador = Invocador()

invocador.ejecutar(EscribirCommand(editor, "Hola "))
invocador.ejecutar(EscribirCommand(editor, "POO2"))
invocador.ejecutar(GuardarCommand(editor))

print("Contenido actual:", editor.contenido)

invocador.deshacer()
invocador.deshacer()

print("Contenido despues de deshacer:", editor.contenido)
