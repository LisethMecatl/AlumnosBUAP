from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.database import get_db
from database.models import Carrera
from schemas.models import CarreraCreate, CarreraResponse
from utils.dependencies import get_current_active_user

router = APIRouter(
    prefix="/carreras",
    tags=["carreras"],
    dependencies=[Depends(get_current_active_user)]
)

@router.post("/", response_model=CarreraResponse, status_code=status.HTTP_201_CREATED)
def create_carrera(carrera: CarreraCreate, db: Session = Depends(get_db)):
    db_carrera = Carrera(**carrera.dict())
    db.add(db_carrera)
    db.commit()
    db.refresh(db_carrera)
    return db_carrera

@router.get("/", response_model=List[CarreraResponse])
def read_carreras(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    carreras = db.query(Carrera).offset(skip).limit(limit).all()
    return carreras

@router.get("/{carrera_id}", response_model=CarreraResponse)
def read_carrera(carrera_id: int, db: Session = Depends(get_db)):
    carrera = db.query(Carrera).filter(Carrera.id == carrera_id).first()
    if carrera is None:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")
    return carrera

@router.put("/{carrera_id}", response_model=CarreraResponse)
def update_carrera(
    carrera_id: int, 
    carrera: CarreraCreate, 
    db: Session = Depends(get_db)
):
    db_carrera = db.query(Carrera).filter(Carrera.id == carrera_id).first()
    if db_carrera is None:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")
    
    for field, value in carrera.dict().items():
        setattr(db_carrera, field, value)
    
    db.commit()
    db.refresh(db_carrera)
    return db_carrera

@router.delete("/{carrera_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_carrera(carrera_id: int, db: Session = Depends(get_db)):
    carrera = db.query(Carrera).filter(Carrera.id == carrera_id).first()
    if carrera is None:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")
    
    db.delete(carrera)
    db.commit()
    return None