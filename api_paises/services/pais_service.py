from config.connection import APIConnection

class PaisService:
    def __init__(self, connection: APIConnection):
        self.connection = connection

    def obtener_todos(self):
        endpoint = "paises"
        response = self.connection.get(endpoint)
        return response.json()

    def crear(self, iso, name):
        endpoint = "paises"
        data = {
            "iso": iso,
            "name": name,
        }
        response = self.connection.post(endpoint, data)
        return response.json()

    def obtener_por_id(self, id):
        endpoint = f"paises/{id}"
        response = self.connection.get(endpoint)
        return response.json()

    def actualizar(self, id, iso, name):
        endpoint = f"paises/{id}"
        data = {
            "iso": iso,
            "name": name,
        }
        response = self.connection.put(endpoint, data)
        return response.json()

    def eliminar(self, id):
        endpoint = f"paises/{id}"
        response = self.connection.delete(endpoint)
        return response.json()
