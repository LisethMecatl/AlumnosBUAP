from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database.database import Base

# Tablas de relación muchos a muchos
usuario_deporte = Table(
    'usuario_deporte', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarios.id'), primary_key=True),
    Column('deporte_id', Integer, ForeignKey('deportes.id'), primary_key=True)
)

usuario_pelicula = Table(
    'usuario_pelicula', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarios.id'), primary_key=True),
    Column('pelicula_id', Integer, ForeignKey('peliculas.id'), primary_key=True)
)

usuario_hobby = Table(
    'usuario_hobby', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarios.id'), primary_key=True),
    Column('hobby_id', Integer, ForeignKey('hobbies.id'), primary_key=True)
)

usuario_color = Table(
    'usuario_color', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarios.id'), primary_key=True),
    Column('color_id', Integer, ForeignKey('colores.id'), primary_key=True)
)

usuario_musica = Table(
    'usuario_musica', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarios.id'), primary_key=True),
    Column('musica_id', Integer, ForeignKey('musicas.id'), primary_key=True)
)

class Facultad(Base):
    __tablename__ = 'facultades'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    carreras = relationship("Carrera", back_populates="facultad")

class Carrera(Base):
    __tablename__ = 'carreras'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    facultad_id = Column(Integer, ForeignKey('facultades.id'))
    facultad = relationship("Facultad", back_populates="carreras")
    usuarios = relationship("Usuario", back_populates="carrera")

class Genero(Base):
    __tablename__ = 'generos'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    usuarios = relationship("Usuario", back_populates="genero")

class Acceso(Base):
    __tablename__ = 'accesos'
    id = Column(Integer, primary_key=True, index=True)
    nivel = Column(String(50), nullable=False)
    usuarios = relationship("Usuario", back_populates="acceso")

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String(100), nullable=False)
    matricula = Column(String(20))
    edad = Column(Integer)
    carrera_id = Column(Integer, ForeignKey('carreras.id'))
    genero_id = Column(Integer, ForeignKey('generos.id'))
    contrasena = Column(String(100))
    acceso_id = Column(Integer, ForeignKey('accesos.id'))
    imagen = Column(String(255))
    
    carrera = relationship("Carrera", back_populates="usuarios")
    genero = relationship("Genero", back_populates="usuarios")
    acceso = relationship("Acceso", back_populates="usuarios")
    
    deportes = relationship("Deporte", secondary=usuario_deporte, back_populates="usuarios")
    peliculas = relationship("Pelicula", secondary=usuario_pelicula, back_populates="usuarios")
    hobbies = relationship("Hobby", secondary=usuario_hobby, back_populates="usuarios")
    colores = relationship("Color", secondary=usuario_color, back_populates="usuarios")
    musicas = relationship("Musica", secondary=usuario_musica, back_populates="usuarios")

class Deporte(Base):
    __tablename__ = 'deportes'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    usuarios = relationship("Usuario", secondary=usuario_deporte, back_populates="deportes")

class Pelicula(Base):
    __tablename__ = 'peliculas'
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    usuarios = relationship("Usuario", secondary=usuario_pelicula, back_populates="peliculas")

class Hobby(Base):
    __tablename__ = 'hobbies'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    usuarios = relationship("Usuario", secondary=usuario_hobby, back_populates="hobbies")

class Color(Base):
    __tablename__ = 'colores'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    usuarios = relationship("Usuario", secondary=usuario_color, back_populates="colores")

class Musica(Base):
    __tablename__ = 'musicas'
    id = Column(Integer, primary_key=True, index=True)
    genero = Column(String(50), nullable=False)
    usuarios = relationship("Usuario", secondary=usuario_musica, back_populates="musicas")