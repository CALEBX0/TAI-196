from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel, Field

app = FastAPI(
    title='Examen 2do Parcial',
    description='Angel Caleb Hinojosa Herrera',
    version='1.0.1'
)

class modelEnvio(BaseModel):
    id: int = Field(..., gt=0, description="ID del usuario, solo números positivos")
    cp: str = Field(..., min_length=5, description="Código postal, mínimo 5 caracteres")
    destino: str = Field(..., min_length=6, description="Nombre del destino, mínimo 6 caracteres")
    peso: float = Field(..., gt=0, lt=500, description="Peso en gramos, mínimo 0 y máximo 500")

envios = [
    {"id": 1, "cp": "76123", "destino": "Peru", "peso": 100},
    {"id": 2, "cp": "76134", "destino": "Mexico", "peso": 150},
    {"id": 3, "cp": "76128", "destino": "España", "peso": 50},
]

# Inicio
@app.get('/', tags=['Inicio'])
def main():
    return {'message': 'Holaaaaaaaaaaa'}

# Endpoint para consultar 1 envío con el id
@app.get('/envios/{id}', tags=['Obtener envío'])
def obtener_envio(id: int):
    for envio in envios:
        if envio["id"] == id:
            return {"Tu envío es": envio}
    raise HTTPException(status_code=404, detail="Envío no encontrado")

# Endpoint para editar un envío
@app.put('/envios/{envio_id}', response_model=modelEnvio, tags=['Editar Envío'])
def actualizar_envio(envio_id: int, envio_actualizado: modelEnvio):
    for i, env in enumerate(envios):
        if env["id"] == envio_id:
            envios[i] = envio_actualizado.model_dump()
            return envios[i]

    raise HTTPException(status_code=404, detail="Envío no encontrado")
