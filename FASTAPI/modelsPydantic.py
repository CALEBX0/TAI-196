from pydantic import BaseModel, Field, EmailStr

#Modelo  para validación de datos
class modelUsuario(BaseModel):
    name: str = Field(...,min_length=3 , max_length=15, description="Nombre, debe contenar solo letras y espacios")
    age:int = Field(...,gt=0, lt=130, description="Edad, debe de ser un número positivo")
    #correo: EmailStr | None = Field(default=None, description="Correo, el correo debe de contener un @. Ejemplo: example@soyuncorreo.com")
    email:str

class modelAuth(BaseModel):
    email: EmailStr
    passw:str =Field(..., min_length=8, strip_whitespace=True, description="Contraseña, mínimo 8 carácteres")