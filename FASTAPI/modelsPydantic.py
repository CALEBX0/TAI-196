from pydantic import BaseModel, Field, EmailStr

#Modelo  para validación de datos
class modelUsuario(BaseModel):
    id: int = Field(...,gt=0, description="Id único y números positivos")
    nombre: str = Field(...,min_length=3 , max_length=15, description="Nombre, debe contenar solo letras y espacios")
    edad:int = Field(...,gt=0, lt=130, description="Edad, debe de ser un número positivo")
    correo: EmailStr | None = Field(default=None, description="Correo, el correo debe de contener un @. Ejemplo: example@soyuncorreo.com")
