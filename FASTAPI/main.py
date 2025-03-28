
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
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


@app.get('/', tags=['Inicio'])
def main():
    return {'Hola FASTAPI!':'AngelCaleb'}

#dependencies=[Depends(BearerJWT())]
#Endpoint para consultar todos
@app.get('/usuarios', tags=['Operaciones CRUD'])
def ConsultarTodos():
    db=Session()
    try:
        consulta=db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    
    except Exception as x:
        return JSONResponse(status_code=500,
                            content={"mensaje":"No se guardó",
                                     "Excepcion": str(x) })
    finally:
        db.close()



#Endpoint para consultar por ID
@app.get('/usuarios/{id}', tags=['Operaciones CRUD'])
def ConsultarId(id:int):
    db=Session()
    try:
        consulta=db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404, content={"Mensaje":"Usuario no encontrado"})
        return JSONResponse(content=jsonable_encoder(consulta))
    
    except Exception as x:
        return JSONResponse(status_code=500,
                            content={"mensaje":"No se guardó",
                                     "Excepcion": str(x) })
    finally:
        db.close()


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

#Endpoint para Actualizar usuario
@app.put('/usuarios/{id}', response_model=modelUsuario, tags=['Operaciones CRUD'])
def ActualizarUsuario(id: int, usuario_Actualizado: modelUsuario):
    db = Session()
    try:
        usuario = db.query(User).filter(User.id == id).first() #Servirá para buscar desde la base de datos
        
        if usuario is None: #Si no encuentra el usuario, ps marca error de que no lo encuentra
            return JSONResponse(status_code=404,
                                 content={"mensaje": "Usuario no encontrado"})
        
        # Esta parte de acá nos servirá para actualizar nuestros datos
        for key, value in usuario_Actualizado.dict().items():
            setattr(usuario, key, value)
        
        db.commit()
        return JSONResponse(status_code=200,
                             content={"mensaje": "Usuario actualizado", 
                                      "usuario": usuario_Actualizado.model_dump()})
    
    except Exception as z: #Por algún error, ponemos este except para que veamos que es un error xd
        db.rollback()
        return JSONResponse(status_code=500,
                             content={"mensaje": "No se guardó",
                                      "Excepcion": str(z)})

    finally: #Cerramos la BD por seguridad
        db.close()


@app.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def EliminarUsuario(id: int):
    db = Session()
    try:
        usuario = db.query(User).filter(User.id == id).first() #Servirá para buscar desde la base de datos
        
        if usuario is None:
            return JSONResponse(status_code=404, content={"Mensaje": "Usuario no encontrado"})
        
        # Nos servirá para eliminar al usuario
        db.delete(usuario)
        db.commit()
        return JSONResponse(status_code=200, content={"mensaje": "Usuario borrado", "usuario": {"id": id}})

    except Exception as q:
        db.rollback()  # En caso de error, se revertirán los cambios
        return JSONResponse(status_code=500, content={"mensaje": "No se eliminó", "Excepcion": str(q)})

    finally:
        db.close() 

#Endpoint para actualizar usuarios
""" @app.put('/usuarios/{usuario_id}', response_model=modelUsuario, tags=['Operaciones CRUD'])
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
    
    raise HTTPException(status_code=400, detail="Usuario no encontrado") """


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

    

