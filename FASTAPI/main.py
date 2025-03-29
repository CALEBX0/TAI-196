
from fastapi import FastAPI
from DB.conexion import engine, Base
from routers.usuarios import routerUsuario
from routers.auth import routerAuth


app= FastAPI(
    title='Mi primer API 196', 
    description= 'Angel Caleb Hinojosa Herrera',
    version='1.0.1'
)

#Levanta las tablas definidas en modelos
Base.metadata.create_all(bind=engine)

app.include_router(routerUsuario)
app.include_router(routerAuth)



@app.get('/', tags=['Inicio'])
def main():
    return {'Hola FASTAPI!':'AngelCaleb'}

#dependencies=[Depends(BearerJWT())]




    

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
