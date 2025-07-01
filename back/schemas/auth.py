#autenticacion jwt
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    matricula: str | None = None

class UsuarioLogin(BaseModel):
    matricula: str
    contrasena: str