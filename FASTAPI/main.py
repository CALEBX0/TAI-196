from fastapi import FastAPI, HTTPException
from typing import Optional

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


@app.get('/', tags=['Inicio'])
def main():
    return {'Hola FASTAPI!':'AngelCaleb - PROGRAMA 4'}




#ENDPOINT PARA OBTENER TODAS LAS TAREAS
@app.get('/tareas', tags=['Obtener tareas'])
def ObtenerTareas():
    return {"Tus tareas son: ": tareas}

#ENDPOINT PARA VER UNA TAREA EN ESPECÍFICO
@app.get('/tareas/{id}', tags=['Obtener Tarea'])
def ObtenerTarea(id: int):
    return {'Tu tarea es: ': id}




#ENDPOINT PARA AÑADIR UNA TAREA
@app.post('/tareas/', tags=['Añadir Tarea'])
def AñadirTarea(newtask:dict):
    for tarea in tareas:
        if tarea['id'] == newtask.get ("id"):
            
            raise HTTPException(status_code=400, detail="Tarea ya existente")

    tareas.append(newtask)
    return newtask





#ENDPOINT PARA ACTUALIZAR UNA TAREA
@app.put('/tareas/{tarea_id}', tags=['Actualizar Tarea'])
def ActualizarTarea(id:int, updatetask:dict):
    for l, tarea in enumerate (tareas):
        if tarea['id'] == id:
            tareas[l].update(updatetask)
            return {"mensaje": "Tarea correctamente", "tarea": updatetask}
    
    raise HTTPException(status_code=400, detail="Tarea no encontrada")
        


#ENDPOINT PARA BORRAR UNA TAREA
@app.delete('/tareas/{id}', tags=['Borrar Tarea'])
def BorrarTarea(id:int):
    for l, tarea in enumerate(tareas):
        if tarea['id'] == id:
            tareas.pop(l)
            return {"mensaje": "Tarea borrada exitosamente"}
    
    raise HTTPException(status_code=400, detail="Tarea no encontrada")