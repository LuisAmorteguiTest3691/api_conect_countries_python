from config.connection import APIConnection
from services.pais_service import PaisService
import pandas as pd

def main():
    # Configuración de la conexión
    base_url = "http://127.0.0.1:8001/api"
    api_token = "GtqxOYJS5YhRUQurv7kkWNZc9IIeHb6Gmoegm3zQOtX3FzOYyCJQNJWowVaJ"

    connection = APIConnection(base_url, api_token)
    pais_service = PaisService(connection)

    # Leer Excel
    df = pd.read_excel('C:/python/data_a_excel/paises.xlsx')

    # Manejar valores NaN: eliminar filas con NaN en columnas clave
    df = df.dropna(subset=["ISO", "Nombre"])  # Elimina filas con NaN en 'ISO' o 'Nombre'
    df = df.fillna("")  # Reemplaza otros NaN con cadenas vacías para evitar problemas

    contador = 0

    # Obtener todos los registros existentes
    respuestaTodos = pais_service.obtener_todos()
    if not respuestaTodos.get('success'):
        print("Error al obtener los registros existentes")
        return
    
    registros_existentes = respuestaTodos.get('data', [])
    print("Registros existentes obtenidos")

    for fila in df.itertuples(index=True, name='ExcelRow'):
        iso = fila.ISO
        nombre = fila.Nombre

        # Validar si ISO o Nombre están vacíos
        if not iso or not nombre:
            print(f"Datos inválidos: ISO='{iso}', Nombre='{nombre}'. Se omite esta fila.")
            continue

        # Validar si el registro ya existe
        duplicado = any(
            registro['iso'] == iso or registro['name'].lower() == nombre.lower()
            for registro in registros_existentes
        )

        if duplicado:
            print(f"El país con ISO '{iso}' o Nombre '{nombre}' ya existe. Se omite.")
            continue

        # Crear países si no están duplicados
        print(f'\nCreando País: ISO={iso}, Nombre={nombre}')
        try:
            respuestaCrear = pais_service.crear(iso, nombre)
            print(respuestaCrear)
            contador += 1
        except Exception as e:
            print(f"Error al crear el país {iso}-{nombre}: {e}")

    print(f'El total de filas procesadas y creadas es de {contador}')
    
if __name__ == "__main__":
    main()
