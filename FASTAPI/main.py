
from fastapi import FastAPI, HTTPException
from typing import Optional, List
from modelsPydantic import modelUsuario

app= FastAPI(
    title='Mi primer API 196', 
    description= 'Angel Caleb Hinojosa Herrera',
    version='1.0.1'
)


usuarios = [
    {"id": 1, "nombre": "Caleb", "edad": 20, "correo": "Caleb@example.com"},
    {"id": 2, "nombre": "Panadero", "edad": 21, "correo": "Panadero@example.com"},
    {"id": 3, "nombre": "Richy", "edad": 21, "correo": "Richy@example.com"},
    {"id": 4, "nombre": "Semillo", "edad": 21, "correo": "Semillo@example.com"},
    {"id": 5, "nombre": "Emma", "edad": 20, "correo": "Emma@example.com"},
]


@app.get('/', tags=['Inicio'])
def main():
    return {'Hola FASTAPI!':'AngelCaleb'}

#Endpoint para consultar todos
@app.get('/usuarios', response_model=List[modelUsuario], tags=['Operaciones CRUD'])
def ConsultarTodos():
    return usuarios

#Endpoint para agregar usuarios
@app.post('/usuarios/', response_model=modelUsuario, tags=['Operaciones CRUD'])
def AgregarUsuario(usuarionuevo:modelUsuario):
    for usr in usuarios:
        if usr["id"] == usuarionuevo.id:
            raise HTTPException(status_code= 400, detail="El id usuario ya existe")

    usuarios.append(usuarionuevo)
    return usuarionuevo

#Endpoint para actualizar usuarios
@app.put('/usuarios/{usuario_id}', response_model=modelUsuario, tags=['Operaciones CRUD'])
def ActualizarUsuario(id:int, usuario_Actualizado:modelUsuario):
    for i, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[i]= usuario_Actualizado.model_dump()
            return usuarios[i]
    
    raise HTTPException(status_code=400, detail="Usuario no encontrado")


#Endpoint para borrar usuarios
@app.delete('/usuarios/{usuario_id}', tags=['Operaciones CRUD'])
def EliminarUsuario(usuario_id: int):
    for i, usr in enumerate(usuarios):
        if usr["id"] == usuario_id:
            usuarioelim = usuarios.pop(i)
            return {"mensaje": "Usuario eliminado correctamente", "usuario": usuarioelim}
    
    raise HTTPException(status_code=400, detail="Usuario no encontrado")

    

