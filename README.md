## Proyecto Final 47790
por: Carlos Tavares

## Modos de Ejecución Local:

Ubícate en la carpeta principal del proyecto y ejecuta el siguiente comando en tu entorno virtual de Python:

```python manage.py runserver ```

Si todo sale bien, podrás acceder al sitio en la siguiente dirección por defecto [http://127.0.0.1:8000/AppCoder/Inicio/](http://127.0.0.1:8000/AppCoder/Inicio/).

Desde aquí podrás acceder a todas las URLs funcionales a las que el diseñador o administrador quiere que accedas.

Pensé en agregar una pagina para la creación de Super Usuarios pero no me pareció lógico o realista.

Para agregar Super Usuarios dirijete a la terminal del entorno virtual de Python y ejecuta el siguiente código y rellena los cuestionamientos:

```python manage.py createsuperuser ```

## Requisitos de la entrega

Crear web similar a un blog

Contar con un admin en route donde se puedan manejar las apps y los datos en las apps.

Tener una app de mensajería para que los perfiles se puedan contactar entre sí.

Acceso visible a la vista Nosotros - /about.

Acceso visible a la vista de Blogs - /pages.

Acceder a una pantalla que contendrá las páginas. Al clickear en “Leer más”. /blog/{blog_id}

Si no existe ninguna página mostrar un "No hay páginas aún" - /404. 

Crear, editar o borrar las fotos y blogs al estar registrado como Administrador. Se agregó un /403 debido a que existe una página solo accesible por un admin o super usuario. Ambas poseen un hyper texto que redirige a /Inicio.

Cada blog, es decir cada model Blog debe tener como mínimo, un título, subtítulo, cuerpo, autor, fecha y una imagen.

Tener una app de registro donde se puedan registrar usuarios en el route accounts/signup, un usuario está compuesto por: email - contraseña - nombre de usuario.

Tener una app de login en el route accounts/login/ la cual permite loguearse con los datos de administrador o de usuario normal.

Tener una app de perfiles en el route accounts/profile/ la cual muestra la info de nuestro usuario y permite poder modificar y/o borrar: imagen - nombre - descripción -  un link a una página web - email y contraseña.

## Credenciales Usuarios Ficticios

Nombre: Laura
Apellido: Gómez
Username: lauragomez
Email: laura.gomez@example.com
Password: Lg123456!

Nombre: Carlos
Apellido: Martínez
Username: carlosmart
Email: carlos.martinez@example.com
Password: Cm789101!

Nombre: Ana
Apellido: Rodríguez
Username: anarodriguez
Email: ana.rodriguez@example.com
Password: Ar111213!

Nombre: Juan
Apellido: Pérez
Username: juanperez
Email: juan.perez@example.com
Password: Jp141516!

Nombre: María
Apellido: López
Username: marialopez
Email: maria.lopez@example.com
Password: Ml171819!

## CRUD

- NavBar
- Home
- About
- Pages
- Login
- Signup
- Messages
- Profile
- Logout
- Create page
- Update Page
- Delete page

## Video de Youtube:

Para visualizar el video de youtube con las funcionalidades de la página web click [aquí](https://youtu.be/rZA8JHC97d0?si=MQa4g0wO82qsgSu_). El video tiene sus marcadores de tiempo por si quieren ver una funcionalidad en específica.

Link: https://youtu.be/rZA8JHC97d0?si=MQa4g0wO82qsgSu_


## Queridos tutores y equipo de CoderHouse,

Quiero tomar un momento para expresar mi más sincero agradecimiento por la increíble experiencia de aprendizaje que he tenido durante este periodo de clases. Los conocimientos que he adquirido son invaluables y han enriquecido mi vida de muchas maneras.

Vuestra dedicación, paciencia y pasión por enseñar son evidentes en cada lección. Siempre estuvieron dispuestos a responder preguntas, aclarar conceptos y brindar orientación, lo cual hizo que el proceso de aprendizaje fuera más enriquecedor y accesible.

Los conocimientos que he obtenido me han empoderado en mi carrera y me han abierto nuevas oportunidades. Estoy emocionado/a por aplicar lo que he aprendido en el mundo real y continuar mi crecimiento profesional.

Agradezco profundamente a cada uno de ustedes por su compromiso con la educación de calidad y por haberme brindado la oportunidad de aprender y crecer. Estoy muy agradecido/a por todo lo que he adquirido durante este periodo de clases.

¡Gracias nuevamente por todo!
