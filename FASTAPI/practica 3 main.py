
from fastapi import FastAPI, HTTPException
from typing import Optional

app= FastAPI(
    title='Mi primer API 196', 
    description= 'Angel Caleb Hinojosa Herrera',
    version='1.0.1'
)

usuarios=[
    {"id":1, "nombre":"Caleb", "edad":20},
    {"id":2, "nombre":"Panadero", "edad":21},
    {"id":3, "nombre":"Richy", "edad":21},
    {"id":4, "nombre":"Semillo", "edad":21},
    {"id":5, "nombre":"Emma", "edad":20}
]

@app.get('/', tags=['Inicio'])
def main():
    return {'Hola FASTAPI!':'AngelCaleb'}

#Endpoint para consultar todos
@app.get('/usuarios',tags=['Operaciones CRUD'])
def ConsultarTodos():
    return {"Usuarios Registrados: ": usuarios}

#Endpoint para agregar usuarios
@app.post('/usuarios/',tags=['Operaciones CRUD'])
def AgregarUsuario(usuarionuevo:dict):
    for usr in usuarios:
        if usr["id"] == usuarionuevo.get("id"):
            raise HTTPException(status_code= 400, details="El id usuario ya existe")

    usuarios.append(usuarionuevo)
    return usuarionuevo

#Endpoint para actualizar usuarios
@app.put('/usuarios/{usuario_id}', tags=['Operaciones CRUD'])
def ActualizarUsuario(id:int, usuarioActualizado: dict):
    for i, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[i].update(usuarioActualizado)
            return {"mensaje": "Usuario actualizado correctamente", "usuario": usuarioActualizado}
    
    raise HTTPException(status_code=400, detail="Usuario no encontrado")


#Endpoint para borrar usuarios
@app.delete('/usuarios/{usuario_id}', tags=['Operaciones CRUD'])
def EliminarUsuario(usuario_id: int):
    for i, usr in enumerate(usuarios):
        if usr["id"] == usuario_id:
            usuarioelim = usuarios.pop(i)
            return {"mensaje": "Usuario eliminado correctamente", "usuario": usuarioelim}
    
    raise HTTPException(status_code=400, detail="Usuario no encontrado")

    

