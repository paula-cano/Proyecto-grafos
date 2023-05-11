from os import error
import json

class Archivos:
    @staticmethod
    def cargar_grafo(nombre_archivo):
        try:
            with open('./data/{0}'.format(nombre_archivo)) as file:
                data = json.load(file)
                return data
        except error:
            return None

    @staticmethod
    def cargar_coordenadas(nombre_archivo):
        try:
            with open('./data/{0}'.format(nombre_archivo)) as file:
                data = json.load(file)
                return data
        except error:
            return None



