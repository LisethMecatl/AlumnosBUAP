from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.database import get_db
from database.models import Musica
from schemas.models import MusicaCreate, MusicaResponse
from utils.dependencies import get_current_active_user

router = APIRouter(
    prefix="/musicas",
    tags=["musicas"],
    dependencies=[Depends(get_current_active_user)]
)

@router.post("/", response_model=MusicaResponse, status_code=status.HTTP_201_CREATED)
def create_musica(musica: MusicaCreate, db: Session = Depends(get_db)):
    db_musica = Musica(**musica.dict())
    db.add(db_musica)
    db.commit()
    db.refresh(db_musica)
    return db_musica

@router.get("/", response_model=List[MusicaResponse])
def read_musicas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    musicas = db.query(Musica).offset(skip).limit(limit).all()
    return musicas

@router.get("/{musica_id}", response_model=MusicaResponse)
def read_musica(musica_id: int, db: Session = Depends(get_db)):
    musica = db.query(Musica).filter(Musica.id == musica_id).first()
    if musica is None:
        raise HTTPException(status_code=404, detail="Género musical no encontrado")
    return musica

@router.put("/{musica_id}", response_model=MusicaResponse)
def update_musica(
    musica_id: int, 
    musica: MusicaCreate, 
    db: Session = Depends(get_db)
):
    db_musica = db.query(Musica).filter(Musica.id == musica_id).first()
    if db_musica is None:
        raise HTTPException(status_code=404, detail="Género musical no encontrado")
    
    db_musica.genero = musica.genero
    db.commit()
    db.refresh(db_musica)
    return db_musica

@router.delete("/{musica_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_musica(musica_id: int, db: Session = Depends(get_db)):
    musica = db.query(Musica).filter(Musica.id == musica_id).first()
    if musica is None:
        raise HTTPException(status_code=404, detail="Género musical no encontrado")
    
    db.delete(musica)
    db.commit()
    return None