from fastapi import FastAPI, HTTPException

app= FastAPI(
    title="Angel Caleb Hinojosa Herrera",
    description="Práctica 4",
    version="1.1.0"
)

tareas=[
    {"id": 1, "titulo": "Estudiar para el Examen", "descripcion": "Repasar los apuntes de TAI", "vencimiento": "14-02-24", "Estado": "Completada"},
    {"id": 2, "titulo": "Hacer ejercicio", "descripcion": "Correr 30 minutos en el parque", "vencimiento": "15-02-24", "Estado": "Pendiente"},
    {"id": 3, "titulo": "Terminar proyecto", "descripcion": "Finalizar el código del sistema de convocatorias", "vencimiento": "18-02-24", "Estado": "En progreso"},
    {"id": 4, "titulo": "Llamar a mis padres", "descripcion": "Preguntarles cómo están y ponerse al día", "vencimiento": "16-02-24", "Estado": "Pendiente"},
    {"id": 5, "titulo": "Actualizar la laptop", "descripcion": "Instalar el nuevo SSD y clonar el sistema", "vencimiento": "20-02-24", "Estado": "Pendiente"}
]


@app.get("/", tags=["Inicio"])
def main():
    return{"Hola, Bienvenido"}

#ENDPOINT PARA OBTENER TODAS LAS TAREAS
@app.get("/tareas", tags=["Obtener tareas"])
def ObtenerTareas():
    return {"Tus tareas son: " tareas}
