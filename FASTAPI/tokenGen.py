import jwt

def createToken(datos:dict):
    token:str = jwt.encode(payload=datos, key='Miku', algorithm= 'HS256')
    return token