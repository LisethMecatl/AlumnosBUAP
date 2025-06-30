from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database.database import get_db
from database.models import Facultad
from schemas.models import FacultadCreate, FacultadResponse
from utils.dependencies import get_current_active_user

router = APIRouter(
    prefix="/facultades",
    tags=["facultades"],
    dependencies=[Depends(get_current_active_user)]
)

@router.post("/", response_model=FacultadResponse)
def create_facultad(facultad: FacultadCreate, db: Session = Depends(get_db)):
    db_facultad = Facultad(nombre=facultad.nombre)
    db.add(db_facultad)
    db.commit()
    db.refresh(db_facultad)
    return db_facultad

@router.get("/", response_model=List[FacultadResponse])
def read_facultades(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    facultades = db.query(Facultad).offset(skip).limit(limit).all()
    return facultades

@router.get("/{facultad_id}", response_model=FacultadResponse)
def read_facultad(facultad_id: int, db: Session = Depends(get_db)):
    facultad = db.query(Facultad).filter(Facultad.id == facultad_id).first()
    if facultad is None:
        raise HTTPException(status_code=404, detail="Facultad no encontrada")
    return facultad

@router.put("/{facultad_id}", response_model=FacultadResponse)
def update_facultad(
    facultad_id: int, 
    facultad: FacultadCreate, 
    db: Session = Depends(get_db)
):
    db_facultad = db.query(Facultad).filter(Facultad.id == facultad_id).first()
    if db_facultad is None:
        raise HTTPException(status_code=404, detail="Facultad no encontrada")
    
    db_facultad.nombre = facultad.nombre
    db.commit()
    db.refresh(db_facultad)
    return db_facultad

@router.delete("/{facultad_id}")
def delete_facultad(facultad_id: int, db: Session = Depends(get_db)):
    facultad = db.query(Facultad).filter(Facultad.id == facultad_id).first()
    if facultad is None:
        raise HTTPException(status_code=404, detail="Facultad no encontrada")
    
    db.delete(facultad)
    db.commit()
    return {"message": "Facultad eliminada correctamente"}