from os import error
import json

class Files:
    @staticmethod
    def load_data():
        try:
            # Abrir el archivo en modo lectura
            with open('C:/Users/Julian/OneDrive/Escritorio/Proyecto-grafos/assets/info.json', 'r') as archivo_json:
                contenido = archivo_json.read()
                archivo_json.close()

            # Cargar el contenido en un objeto de Python
            return json.loads(contenido)
        except error:
            return None
