from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import engine, Base
from routers import (
    auth, usuarios, facultades, carreras, generos, accesos,
    deportes, peliculas, hobbies, colores, musicas
)

app = FastAPI(title="API Alumnos BUAP", version="1.0.0")

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear tablas en la base de datos (en producción usar migraciones)
Base.metadata.create_all(bind=engine)

# Incluir routers
app.include_router(auth.router)
app.include_router(usuarios.router)
app.include_router(facultades.router)
app.include_router(carreras.router)
app.include_router(generos.router)
app.include_router(accesos.router)
app.include_router(deportes.router)
app.include_router(peliculas.router)
app.include_router(hobbies.router)
app.include_router(colores.router)
app.include_router(musicas.router)


@app.get("/")
def read_root():
    return {"message": "API Alumnos BUAP - Bienvenido"}
