from typing import List, Optional, Union
from pydantic import BaseModel
from datetime import datetime

# Modelos base
class BaseSchema(BaseModel):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

# Facultades
class FacultadBase(BaseSchema):
    nombre: str

class FacultadCreate(FacultadBase):
    pass

class FacultadResponse(FacultadBase):
    id: int

# Carreras
class CarreraBase(BaseSchema):
    nombre: str
    facultad_id: int

class CarreraCreate(CarreraBase):
    pass

class CarreraResponse(CarreraBase):
    id: int
    facultad: FacultadResponse

# Géneros
class GeneroBase(BaseSchema):
    nombre: str

class GeneroCreate(GeneroBase):
    pass

class GeneroResponse(GeneroBase):
    id: int

# Niveles de Acceso
class AccesoBase(BaseSchema):
    nivel: str

class AccesoCreate(AccesoBase):
    pass

class AccesoResponse(AccesoBase):
    id: int

# Deportes
class DeporteBase(BaseSchema):
    nombre: str

class DeporteCreate(DeporteBase):
    pass

class DeporteResponse(DeporteBase):
    id: int

# Películas
class PeliculaBase(BaseSchema):
    titulo: str

class PeliculaCreate(PeliculaBase):
    pass

class PeliculaResponse(PeliculaBase):
    id: int

# Hobbies
class HobbyBase(BaseSchema):
    nombre: str

class HobbyCreate(HobbyBase):
    pass

class HobbyResponse(HobbyBase):
    id: int

# Colores
class ColorBase(BaseSchema):
    nombre: str

class ColorCreate(ColorBase):
    pass

class ColorResponse(ColorBase):
    id: int

# Géneros Musicales
class MusicaBase(BaseSchema):
    genero: str

class MusicaCreate(MusicaBase):
    pass

class MusicaResponse(MusicaBase):
    id: int

# Usuarios
class UsuarioBase(BaseSchema):
    nombre_completo: str
    matricula: str
    edad: Optional[int] = None
    imagen: Optional[str] = None

class UsuarioCreate(UsuarioBase):
    carrera_id: Optional[int] = None
    genero_id: Optional[int] = None
    acceso_id: int = 2  # Por defecto usuario normal
    contrasena: str
    deportes: Optional[List[int]] = []
    peliculas: Optional[List[int]] = []
    hobbies: Optional[List[int]] = []
    colores: Optional[List[int]] = []
    musicas: Optional[List[int]] = []

class UsuarioUpdate(BaseSchema):
    nombre_completo: Optional[str] = None
    matricula: Optional[str] = None
    edad: Optional[int] = None
    carrera_id: Optional[int] = None
    genero_id: Optional[int] = None
    acceso_id: Optional[int] = None
    contrasena: Optional[str] = None
    imagen: Optional[str] = None
    deportes: Optional[List[int]] = None
    peliculas: Optional[List[int]] = None
    hobbies: Optional[List[int]] = None
    colores: Optional[List[int]] = None
    musicas: Optional[List[int]] = None

class UsuarioResponse(UsuarioBase):
    id: int
    carrera: Optional[CarreraResponse] = None
    genero: Optional[GeneroResponse] = None
    acceso: Optional[AccesoResponse] = None
    deportes: Optional[List[DeporteResponse]] = []
    peliculas: Optional[List[PeliculaResponse]] = []
    hobbies: Optional[List[HobbyResponse]] = []
    colores: Optional[List[ColorResponse]] = []
    musicas: Optional[List[MusicaResponse]] = []

# Relaciones
class UsuarioDeporteBase(BaseSchema):
    usuario_id: int
    deporte_id: int

class UsuarioPeliculaBase(BaseSchema):
    usuario_id: int
    pelicula_id: int

class UsuarioHobbyBase(BaseSchema):
    usuario_id: int
    hobby_id: int

class UsuarioColorBase(BaseSchema):
    usuario_id: int
    color_id: int

class UsuarioMusicaBase(BaseSchema):
    usuario_id: int
    musica_id: int