# PRE-ENTREGA 4
# Sistema de blog modular y validado


# DATOS DEL AUTOR

perfil_autor = {
    "nombre": "José Mercado",
    "bio": "Estudiante de desarrollo web y creador de contenido sobre programación.",
    "especialidad": "Desarrollo Web",
    "redes_sociales": ["@jose_dev", "@jose_web"]
}


# ESTADOS POSIBLES

estados_post = (
    "borrador",
    "publicado",
    "archivado"
)


# ETIQUETAS DEL BLOG

etiquetas_blog = {
    "Python",
    "Desarrollo Web",
    "HTML",
    "CSS"
}


# LISTA DE POSTS

posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Aprendiendo desarrollo web",
        "contenido": "En este post veremos conceptos básicos del desarrollo web.",
        "autor": perfil_autor,
        "tags": ["HTML", "CSS", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Estructuras de datos en Python",
        "contenido": "",
        "autor": perfil_autor,
        "tags": ["Python", "Diccionarios"],
        "estado": "archivado"
    }
]


# FUNCIÓN DEL MENÚ

def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    try:
        opcion = int(input("Elegí una opción: "))
        return opcion

    except ValueError:
        print("Error: debes ingresar un número.")
        return None


# FUNCIÓN PARA LISTAR POSTS

def listar_posts(lista):
    print("\nPosts disponibles:")

    for post in lista:
        titulo = post.get("titulo", "Sin título")

        autor = post.get("autor", {})

        if isinstance(autor, dict):
            nombre_autor = autor.get("nombre", "Autor desconocido")
        else:
            nombre_autor = "Autor desconocido"

        print("-", titulo, "| Autor:", nombre_autor)


# FUNCIÓN PARA BUSCAR POR TÍTULO

def buscar_por_titulo(lista, termino):

    if termino == "":
        print("La búsqueda no puede estar vacía.")
        return

    encontrado = False

    for post in lista:
        titulo = post.get("titulo", "")

        if termino.lower() in titulo.lower():
            print("-", titulo)
            encontrado = True

    if encontrado == False:
        print("No se encontraron posts con ese titulo.")


# FUNCIÓN PARA FILTRAR POR TAG

def filtrar_por_tag(lista, tag_buscado):

    if tag_buscado == "":
        print("El tag no puede estar vacío.")
        return

    encontrado = False

    for post in lista:

        tags = post.get("tags", [])

        if isinstance(tags, list):

            for tag in tags:

                if tag_buscado.lower() == tag.lower():
                    print("-", post.get("titulo", "Sin título"))
                    encontrado = True
                    break

    if encontrado == False:
        print("No se encontraron posts con ese tag.")


# FUNCIÓN PARA VALIDAR POSTS

def validar_post(post):

    if not isinstance(post, dict):
        return False, "el post no es un diccionario"

    claves_obligatorias = [
        "id",
        "titulo",
        "contenido",
        "autor",
        "tags",
        "estado"
    ]

    for clave in claves_obligatorias:
        if clave not in post:
            return False, "falta la clave " + clave

    if post.get("titulo") == "":
        return False, "el título está vacío"

    if post.get("contenido") == "":
        return False, "el contenido está vacío"

    if not isinstance(post.get("autor"), dict):
        return False, "el autor no es un diccionario"

    if "nombre" not in post["autor"]:
        return False, "el autor no tiene nombre"

    if not isinstance(post.get("tags"), list):
        return False, "tags debe ser una lista"

    if post.get("estado") not in estados_post:
        return False, "el estado no es válido"

    return True, "válido"


# PROGRAMA PRINCIPAL

if __name__ == "__main__":

    while True:

        opcion = mostrar_menu()

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = input("Buscar por titulo: ").strip()
            buscar_por_titulo(posts, termino)

        elif opcion == 3:
            tag = input("Escribí un tag: ").strip()
            filtrar_por_tag(posts, tag)

        elif opcion == 4:

            print("\nValidación de posts:")

            for post in posts:

                valido, mensaje = validar_post(post)

                if valido:
                    print(
                        "Post",
                        post.get("id", "Sin ID"),
                        ": válido"
                    )

                else:
                    print(
                        "Post",
                        post.get("id", "Sin ID"),
                        ": error -",
                        mensaje
                    )

        elif opcion == 5:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        elif opcion is not None:
            print("Opción inválida, intenta de nuevo")