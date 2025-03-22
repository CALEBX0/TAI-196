
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from modelsPydantic import modelUsuario, modelAuth
from tokenGen import createToken
from middleware import BearerJWT
from DB.conexion import Session, engine, Base
from models.modelsDB import User


app= FastAPI(
    title='Mi primer API 196', 
    description= 'Angel Caleb Hinojosa Herrera',
    version='1.0.1'
)

#Levanta las tablas definidas en modelos
Base.metadata.create_all(bind=engine)

usuarios = [
    {"id": 1, "nombre": "Caleb", "edad": 20, "correo": "calebxo@hotmail.com"},
    {"id": 2, "nombre": "Panadero", "edad": 21, "correo": "Panadero@example.com"},
    {"id": 3, "nombre": "Richy", "edad": 21, "correo": "Richy@example.com"},
    {"id": 4, "nombre": "Semillo", "edad": 21, "correo": "Semillo@example.com"},
    {"id": 5, "nombre": "Emma", "edad": 20, "correo": "Emma@example.com"},
]


@app.get('/', tags=['Inicio'])
def main():
    return {'Hola FASTAPI!':'AngelCaleb'}

#Endpoint apra generar token
@app.post('/auth', tags=['Autentificación'])
def login(autorizado:modelAuth):
    if autorizado.email == 'calebxo@hotmail.com' and autorizado.passw == '123456789':
        token:str=createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content=token)
        return {"Aviso": "Token Generado"}
    else:
        return {"Aviso": "Usuario no autorizado"}


#Endpoint para consultar todos
@app.get('/usuarios', dependencies=[Depends(BearerJWT())], response_model=List[modelUsuario], tags=['Operaciones CRUD'])
def ConsultarTodos():
    return usuarios

#Endpoint para agregar usuarios
@app.post('/usuarios/', response_model=modelUsuario, tags=['Operaciones CRUD'])
def AgregarUsuario(usuarionuevo:modelUsuario):
    db=Session()
    try:
        db.add(User(**usuarionuevo.model_dump()))
        db.commit()
        return JSONResponse(status_code=201,
                            content={"mensaje":"Usuario Guardado", 
                                     "usuario":usuarionuevo.model_dump() })
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"mensaje":"No se guardó",
                                     "Excepcion": str(e) })

    finally:
        db.close()

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

    

