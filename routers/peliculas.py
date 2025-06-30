from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.database import get_db
from database.models import Pelicula
from schemas.models import PeliculaCreate, PeliculaResponse
from utils.dependencies import get_current_active_user

router = APIRouter(
    prefix="/peliculas",
    tags=["peliculas"],
    dependencies=[Depends(get_current_active_user)]
)

@router.post("/", response_model=PeliculaResponse, status_code=status.HTTP_201_CREATED)
def create_pelicula(pelicula: PeliculaCreate, db: Session = Depends(get_db)):
    db_pelicula = Pelicula(**pelicula.dict())
    db.add(db_pelicula)
    db.commit()
    db.refresh(db_pelicula)
    return db_pelicula

@router.get("/", response_model=List[PeliculaResponse])
def read_peliculas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    peliculas = db.query(Pelicula).offset(skip).limit(limit).all()
    return peliculas

@router.get("/{pelicula_id}", response_model=PeliculaResponse)
def read_pelicula(pelicula_id: int, db: Session = Depends(get_db)):
    pelicula = db.query(Pelicula).filter(Pelicula.id == pelicula_id).first()
    if pelicula is None:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    return pelicula

@router.put("/{pelicula_id}", response_model=PeliculaResponse)
def update_pelicula(
    pelicula_id: int, 
    pelicula: PeliculaCreate, 
    db: Session = Depends(get_db)
):
    db_pelicula = db.query(Pelicula).filter(Pelicula.id == pelicula_id).first()
    if db_pelicula is None:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    
    db_pelicula.titulo = pelicula.titulo
    db.commit()
    db.refresh(db_pelicula)
    return db_pelicula

@router.delete("/{pelicula_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pelicula(pelicula_id: int, db: Session = Depends(get_db)):
    pelicula = db.query(Pelicula).filter(Pelicula.id == pelicula_id).first()
    if pelicula is None:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    
    db.delete(pelicula)
    db.commit()
    return None