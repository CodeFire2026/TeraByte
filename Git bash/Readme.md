# CLASE 01 MIÉRCOLES 12 DE AGOSTO DEL 2026 - Portafolio 1

## USO DE GITHUB

GitHub es una plataforma que nos permite guardar repositorios de Git que podemos usar como servidores remotos y ejecutar algunos comandos de forma visual e interactiva (sin necesidad de la consola de comandos).

Luego de crear nuestra cuenta, podemos crear o importar repositorios, crear organizaciones y proyectos de trabajo, descubrir repositorios de otras personas, contribuir a esos proyectos, dar estrellas y muchas otras cosas.

### COMANDOS

#Import repository, New repository, New organization: significa que es como tu empresa, New project: significa es como un grupo de repositorios que puedes tener dentro de una empresa, New gist: es un pedasito de código que puedes compartir

New repository #Ponemos el nombre: Prueba-Inicio.Repo, descripción: Así armamos un repositorio. Hay muchas licencias para publicar el código: NO lo hacemos ahora.


Create repository #Lo ponemos en privado o en Publico.

El README.md es el archivo que veremos por defecto al entrar a un repositorio. Es una muy buena práctica configurarlo para describir el proyecto, los requerimientos y las instrucciones que debemos seguir para contribuir correctamente.

Para clonar un repositorio desde GitHub (o cualquier otro servidor remoto) debemos copiar la URL (por ahora, usando ssh) y ejecutar el comando git clone + la URL que acabamos de copiar. Esto descargará la versión de nuestro proyecto que se encuentra en GitHub.

ATENCIÓN: ¿Por qué? Porque a través de https nos pedirá usuario(nombre perfil) y contraseña. Igual esto ya no funciona de una manera fácil.

Sin embargo, esto solo funciona para las personas que quieren empezar a contribuir en el proyecto.

Cómo conectar un repositorio de GitHub a nuestro documento local, Si queremos conectar el repositorio de GitHub con nuestro repositorio local, aconsejo que al trabajar desde GitHub no utilizemos localmente el comando git init, si debemos ejecutar las siguientes instrucciones:

Teclear aquí para VER el video 1

En el video esta todo lo que se debe hacer...


PORTAFOLIO


Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Auxiliar:
Dante Nicolás Martinez
* IntroYpractica
* Practicas
* PDF


Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Auxiliar Nico, lo que sea tarea o investigación.

Profesor Ariel Betancud

# CLASE 02 MIÉRCOLES 19 DE AGOSTO DEL 2026 - Portafolio 2

## Vamos a cargar la llave SSH publica en GitHub -> SI YA HAZ HECHO ESTE TRABAJO, NO SE DEBE REPETIR EL SSH

Para copiar la llave publica debes ir al archivo .ssh y allí encontrarás el archivo .pub lo podes abrir con el txt, luego copiar el contenido que esta dentro.

copiar la llave publica #Ir a GitHub, vamos a setting, vamos a SSH and GPG keys

crear una nueva #New SSH key poner nombre y pegar la ssh publica, con esto esta listo.

Aconsejo que la ssh tenga el nombre del ordenador en el que estas trabajando. Esto se debe hacer con cada pc nueva o dispositivo nuevo que tengamos para acceder a nuestra cuenta de GitHub.

git branch #Vemos en que rama estamos

git checkout master #Ponernos en la rama master

git branch -M main #Cambiamos el nombre a la rama master

git remote add origin git@github.com:nombreUsuario/class-git.git #Agregamos el repositorio remoto, este es un ejemplo

git remote -v #Vemos si ya esta conectado

git merge segunda #Mergeamos lo que tenemos en la rama segunda en main

git commit -am "Uso de GitHub parte 20" #Hacemos el commit de hoy

git push origin main #Pasamos todo lo hecho a GitHub, revisar en el repositorio en GitHub.

Frente al cambio de nombre de rama master a main, suele suceder que en el repo de GitHub se hayan creado dos ramas, la rama master y la rama main, se debe ir al repo, settings y ahí se puede cambiar la rama principal, en vez de que siga siendo master, que sea la rama main, luego de eso ya podemos borrar la rama master.

PORTAFOLIO


Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Auxiliar:

Dante Nicolás Martinez

* Introducción
* Practica
* PDF

Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Auxiliar Nico, lo que sea tarea o investigación.

Profesor Ariel Betancud

