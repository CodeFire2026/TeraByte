# ¿Cómo creamos funciones en JavaScript de manera descriptiva?
```sh
Tenemos que tener presente que utilizamos el tipo de escritura Camel case y sus identificadores normalemente los vamos a encontrar en ingles, veamos varios ejemplos:
```

## Estas funciones tienen que ver con la manipulación de datos
```sh
calculateTotalPrice() — Calcular precio total :Sirve para calcular el monto final a pagar sumando subtotales, impuestos, descuentos o costos de envío (muy común en carritos de compras).
```
```sh
formatUserInput()— Formatear entrada del usuario: Sirve para limpiar o darle un formato estandarizado a lo que escribe el usuario (por ejemplo, sacarle los espacios de más al principio o al final, o poner la primera letra en mayúscula).
```
```sh
validateEmailAddress() — Validar dirección de correo: Sirve para comprobar que un texto ingresado tenga el formato real de un correo electrónico (que tenga un usuario, un @ y un dominio válido como .com).
```
```sh
convertToCamelCase() — Convertir a camelCase: Sirve para transformar una frase o texto separado por guiones o espacios al formato camelCase (juntando las palabras y poniendo en mayúscula la letra inicial de cada palabra a partir de la segunda, ej: miVariable).
```
```sh
filterActiveUsers() — Filtrar usuarios activos: Sirve para tomar una lista completa de usuarios y devolver una nueva lista que contenga únicamente a aquellos que están activos o habilitados.
```

## Eventos o Interacción
```sh
handleButtonClick() — Manejar clic en botón: Sirve para definir qué acción debe ocurrir (ej. mostrar un mensaje, enviar datos, abrir un menú) cuando el usuario hace clic en un botón específico.
```
```sh
onFormSubmit() — Al enviar formulario (o envío de formulario): Sirve para interceptar el momento en que se envía un formulario, generalmente para evitar que la página se recargue y validar los datos antes de mandarlos al servidor.
```
```sh
toggleDarkMode() — Alternar modo oscuro: Sirve para alternar el tema visual de una aplicación entre el modo claro y el modo oscuro (activa uno si está el otro, y viceversa).
```
```sh
updateProgressBar() — Actualizar barra de progreso: Sirve para modificar visualmente el porcentaje de avance de una barra de progreso (por ejemplo, cuando se está cargando un archivo o completando un formulario por pasos).
```
```sh
initializeApp() — Inicializar aplicación: Sirve para ejecutar todas las configuraciones iniciales cuando arranca la aplicación (conectar bases de datos, cargar datos esenciales, verificar si hay sesiones activas, etc.).
```

## Operaciones CRUD
```sh
createNewUser() — Crear nuevo usuario: Sirve para registrar un nuevo usuario en la base de datos o sistema.
```
```sh
fetchUserData() — Obtener/Consultar datos de usuario: Sirve para solicitar y traer los datos de un usuario específico desde el servidor o la base de datos para mostrarlos en pantalla.
```
```sh
updateUserProfile() — Actualizar perfil de usuario: Sirve para modificar los datos existentes de un usuario (como su nombre, foto de perfil o contraseña) y guardarlos.
```
```sh
deleteUserAccount() — Eliminar cuenta de usuario: Sirve para eliminar permanentemente o dar de baja la cuenta de un usuario del sistema.

```
## Utilidades
```sh
generateRandomId() — Generar ID aleatorio: Sirve para crear un identificador único y aleatorio (muy útil para asignar IDs temporales a elementos nuevos, como productos en un carrito).
```
```sh
formatCurrency() — Formatear moneda: Sirve para transformar un número plano (ej. 1500) en un formato de dinero legible con su moneda y separadores correspondientes (ej. $1.500,00).
```
```sh
debounceSearch() — Aplicar debounce (retardo) a la búsqueda: Sirve para retrasar la ejecución de una búsqueda mientras el usuario sigue escribiendo, evitando hacer una consulta al servidor por cada letra que tipea y ahorrando recursos.
```
```sh
sanitizeInput() — Sanitizar / Limpiar entrada de datos): Sirve para limpiar datos de entrada eliminando código malicioso (como etiquetas HTML o scripts) para evitar vulnerabilidades de seguridad (como ataques de tipo XSS).
```
```sh
checkPermissions() — Comprobar permisos: Sirve para verificar si el usuario actual tiene los permisos o roles necesarios (por ejemplo, si es "Administrador") para realizar una acción o ver cierta sección.
```

