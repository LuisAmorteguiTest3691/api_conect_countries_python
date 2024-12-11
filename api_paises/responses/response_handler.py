class ResponseHandler:
    @staticmethod
    def manejar_respuesta(response):
        if response.status_code in [200, 201]:
            return response
        elif response.status_code == 401:
            raise Exception("Unauthorized: Verifique el token de autenticación.")
        elif response.status_code == 404:
            raise Exception("Not Found: El recurso solicitado no existe.")
        elif response.status_code >= 500:
            raise Exception("Server Error: Ha ocurrido un error en el servidor.")
        else:
            raise Exception(f"Error desconocido: {response.status_code} - {response.text}")
