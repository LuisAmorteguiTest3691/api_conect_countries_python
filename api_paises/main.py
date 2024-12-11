from config.connection import APIConnection
from services.pais_service import PaisService
from responses.response_handler import ResponseHandler

def main():
    # Configuración de la conexión
    base_url = "http://127.0.0.1:8001/api"
    api_token = "GtqxOYJS5YhRUQurv7kkWNZc9IIeHb6Gmoegm3zQOtX3FzOYyCJQNJWowVaJ"

    connection = APIConnection(base_url, api_token)
    pais_service = PaisService(connection)

    try:
        # 1. Obtener todos los países
        print("Obteniendo todos los países:")
        respuesta = pais_service.obtener_todos()
        print(respuesta)

        # 2. Crear un nuevo país
        print("\nCreando un nuevo país:")
        respuesta = pais_service.crear("FR", "Francia")
        print(respuesta)

        # 3. Obtener un país por ID
        print("\nObteniendo país por ID:")
        respuesta = pais_service.obtener_por_id(1)
        print(respuesta)

        # 4. Actualizar un país
        print("\nActualizando un país:")
        respuesta = pais_service.actualizar(1, "ES", "España Actualizada")
        print(respuesta)

        # 5. Eliminar un país
        print("\nEliminando un país:")
        respuesta = pais_service.eliminar(1)
        print(respuesta)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
