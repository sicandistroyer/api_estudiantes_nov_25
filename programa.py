import requests
import json
import time

# URL base de la API de prueba que usaremos
BASE_URL = 'http://localhost:5010/estudiantes'

def get_posts():
    """Realiza una petición GET para obtener uno o todos los posts."""
    post_id = input("Ingresa el número de control para obtener un estudiante (deja en blanco para todos): ")
    url = f"{BASE_URL}/{post_id}" if post_id.isdigit() else BASE_URL
    print(f"\n--- Realizando GET a: {url} ---")
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("GET exitoso. Código de estado:", response.status_code)
        print("Datos recibidos:")
        print(json.dumps(response.json(), indent=2))
    except requests.exceptions.RequestException as e:
        print(f"Error durante la petición GET: {e}")

def create_post():
    """Realiza una petición POST para crear un nuevo post."""
    title = input("Ingresa el título del nuevo post: ")
    body = input("Ingresa el cuerpo del nuevo post: ")
    user_id = input("Ingresa el ID de usuario: ")
    payload = {
        'title': title,
        'body': body,
        'userId': int(user_id) if user_id.isdigit() else 1
    }
    print(f"\n--- Realizando POST a: {BASE_URL} ---")
    print("Enviando datos:", payload)
    try:
        response = requests.post(BASE_URL, json=payload)
        response.raise_for_status()
        print("POST exitoso. Código de estado:", response.status_code)
        print("Nuevo post creado:")
        print(json.dumps(response.json(), indent=2))
    except requests.exceptions.RequestException as e:
        print(f"Error durante la petición POST: {e}")

def update_post():
    """Realiza una petición PATCH para actualizar un post."""
    post_id = input("Ingresa el ID del post a actualizar: ")
    title = input("Ingresa el nuevo título (deja en blanco para no cambiar): ")
    body = input("Ingresa el nuevo cuerpo (deja en blanco para no cambiar): ")
    updated_data = {}
    if title:
        updated_data['title'] = title
    if body:
        updated_data['body'] = body

    if not updated_data:
        print("No se ingresaron datos para actualizar.")
        return

    url = f"{BASE_URL}/{post_id}"
    print(f"\n--- Realizando PATCH a: {url} ---")
    print("Actualizando con datos:", updated_data)
    try:
        response = requests.patch(url, json=updated_data)
        response.raise_for_status()
        print("PATCH exitoso. Código de estado:", response.status_code)
        print("Post actualizado:")
        print(json.dumps(response.json(), indent=2))
    except requests.exceptions.RequestException as e:
        print(f"Error durante la petición PATCH: {e}")

def delete_post():
    """Realiza una petición DELETE para eliminar un post."""
    post_id = input("Ingresa el ID del post a eliminar: ")
    url = f"{BASE_URL}/{post_id}"
    print(f"\n--- Realizando DELETE a: {url} ---")
    try:
        response = requests.delete(url)
        response.raise_for_status()
        print("DELETE exitoso. Código de estado:", response.status_code)
        print("Post eliminado correctamente.")
    except requests.exceptions.RequestException as e:
        print(f"Error durante la petición DELETE: {e}")

# --- Bucle principal del menú ---
def main_menu():
    while True:
        print("\n--- Menú de Peticiones API ---")
        print("1. Obtener estudiantes (GET)")
        print("2. Crear un nuevo estudiante (POST)")
        print("3. Actualizar un estudiante existente (PATCH)")
        print("4. Eliminar un estudiante (DELETE)")
        print("5. Salir")
        choice = input("Elige una opción (1-5): ")

        if choice == '1':
            get_posts()
        elif choice == '2':
            create_post()
        elif choice == '3':
            update_post()
        elif choice == '4':
            delete_post()
        elif choice == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")
        
        time.sleep(2)  # Pausa para que el usuario pueda leer la salida

if __name__ == "__main__":
    main_menu()