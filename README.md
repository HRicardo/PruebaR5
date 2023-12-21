se accede al crud para realizar consultas, agregar, eliminar y editar desde la pagina web y se liberan los siguientes servicios para consultar desde un postman 

/getBookspost/ - Consultar libros tanto de la BD como desde google books y Open Library Search
/createBookspost/ - se crean libros para poder modificar desde la interfaz grafica
/deleteBookspost/<id>/ - se eliminan registros de la base de datos

el content type para los servicios es application/x-www-form-urlencoded y se debe setear la cookie:

csrftoken=RlubHWr8qo42gtf5uOeTgebqFoegGu40mcFTVUlYkQaimFBBGVIUfoFjocrwN5OW; Path=/; Expires=Thu, 19 Dec 2024 23:17:55 GMT;

para que django acepte la consulta

se utilizaron los siguientes plataformas:

lenguaje: python 3
framework: django 3.1.3
base de datos: mysql
carpeta raiz: htdocs (dentro de la carpeta del env)
