// Ejercicio 1: Función que valide una contraseña (mínimo 8 caracteres, 1 número, 1 mayúscula)
function validatePassword(password) {
    let tieneNumero = false;
    let tieneMayuscula = false;

    if (password.length < 8) {
        return false;
    }

    for (let i = 0; i < password.length; i++) {

        if (password[i] >= "0" && password[i] <= "9") {
            tieneNumero = true;
        }

        if (password[i] >= "A" && password[i] <= "Z") {
            tieneMayuscula = true;
        }
    }

    if (tieneNumero && tieneMayuscula) {
        return true;
    } else {
        return false;
    }
}

console.log(validatePassword("Abc12345"));
console.log(validatePassword("weak"));


// Ejercicio 2: Crear un sistema simple de gestión de tareas
function createTaskManager() {

    let tasks = [];

    return {

        addTask: function(task) {
            tasks.push(task);
        },

        completeTask: function(taskId) {
            tasks[taskId] = tasks[taskId] + " (Completada)";
        },

        listTasks: function() {
            for (let i = 0; i < tasks.length; i++) {
                console.log(i + ": " + tasks[i]);
            }
        }

    };
}


// Uso:

const myTasks = createTaskManager();

myTasks.addTask("Aprender JavaScript");
myTasks.addTask("Hacer ejercicio");

myTasks.listTasks();

myTasks.completeTask(0);

console.log("-------------");

myTasks.listTasks();
