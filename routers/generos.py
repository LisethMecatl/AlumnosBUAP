from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.database import get_db
from database.models import Genero
from schemas.models import GeneroCreate, GeneroResponse
from utils.dependencies import get_current_active_user

router = APIRouter(
    prefix="/generos",
    tags=["generos"],
    dependencies=[Depends(get_current_active_user)]
)

@router.post("/", response_model=GeneroResponse, status_code=status.HTTP_201_CREATED)
def create_genero(genero: GeneroCreate, db: Session = Depends(get_db)):
    db_genero = Genero(**genero.dict())
    db.add(db_genero)
    db.commit()
    db.refresh(db_genero)
    return db_genero

@router.get("/", response_model=List[GeneroResponse])
def read_generos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    generos = db.query(Genero).offset(skip).limit(limit).all()
    return generos

@router.get("/{genero_id}", response_model=GeneroResponse)
def read_genero(genero_id: int, db: Session = Depends(get_db)):
    genero = db.query(Genero).filter(Genero.id == genero_id).first()
    if genero is None:
        raise HTTPException(status_code=404, detail="Género no encontrado")
    return genero

@router.put("/{genero_id}", response_model=GeneroResponse)
def update_genero(
    genero_id: int, 
    genero: GeneroCreate, 
    db: Session = Depends(get_db)
):
    db_genero = db.query(Genero).filter(Genero.id == genero_id).first()
    if db_genero is None:
        raise HTTPException(status_code=404, detail="Género no encontrado")
    
    db_genero.nombre = genero.nombre
    db.commit()
    db.refresh(db_genero)
    return db_genero

@router.delete("/{genero_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_genero(genero_id: int, db: Session = Depends(get_db)):
    genero = db.query(Genero).filter(Genero.id == genero_id).first()
    if genero is None:
        raise HTTPException(status_code=404, detail="Género no encontrado")
    
    db.delete(genero)
    db.commit()
    return None