from fastapi.responses import JSONResponse
from modelsPydantic import modelAuth
from tokenGen import createToken
from fastapi import APIRouter

routerAuth=APIRouter()

#Endpoint para generar token
@routerAuth.post('/auth', tags=['Autentificación'])
def login(autorizado:modelAuth):
    if autorizado.email == 'calebxo@hotmail.com' and autorizado.passw == '123456789':
        token:str=createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content=token)
        return {"Aviso": "Token Generado"}
    else:
        return {"Aviso": "Usuario no autorizado"}