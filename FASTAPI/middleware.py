from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from tokenGen import validateToken

class BearerJWT(HTTPBearer):
    async def __call__(self, request:Request):
        auth= await super().__call__(request)
        data=validateToken(auth.credentials)

        if not isinstance(data, dict): 
            raise HTTPException(status_code=401, details='Formato de token no válido')
        
        if data.get('correo')!= 'calebxo@hotmail.com':
            HTTPException(status_code=403, detail= 'Credenciales No Válidas')
            