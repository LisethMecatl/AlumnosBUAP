from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.database import get_db
from database.models import Deporte
from schemas.models import DeporteCreate, DeporteResponse
from utils.dependencies import get_current_active_user

router = APIRouter(
    prefix="/deportes",
    tags=["deportes"],
    dependencies=[Depends(get_current_active_user)]
)

@router.post("/", response_model=DeporteResponse, status_code=status.HTTP_201_CREATED)
def create_deporte(deporte: DeporteCreate, db: Session = Depends(get_db)):
    db_deporte = Deporte(**deporte.dict())
    db.add(db_deporte)
    db.commit()
    db.refresh(db_deporte)
    return db_deporte

@router.get("/", response_model=List[DeporteResponse])
def read_deportes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    deportes = db.query(Deporte).offset(skip).limit(limit).all()
    return deportes

@router.get("/{deporte_id}", response_model=DeporteResponse)
def read_deporte(deporte_id: int, db: Session = Depends(get_db)):
    deporte = db.query(Deporte).filter(Deporte.id == deporte_id).first()
    if deporte is None:
        raise HTTPException(status_code=404, detail="Deporte no encontrado")
    return deporte

@router.put("/{deporte_id}", response_model=DeporteResponse)
def update_deporte(
    deporte_id: int, 
    deporte: DeporteCreate, 
    db: Session = Depends(get_db)
):
    db_deporte = db.query(Deporte).filter(Deporte.id == deporte_id).first()
    if db_deporte is None:
        raise HTTPException(status_code=404, detail="Deporte no encontrado")
    
    db_deporte.nombre = deporte.nombre
    db.commit()
    db.refresh(db_deporte)
    return db_deporte

@router.delete("/{deporte_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_deporte(deporte_id: int, db: Session = Depends(get_db)):
    deporte = db.query(Deporte).filter(Deporte.id == deporte_id).first()
    if deporte is None:
        raise HTTPException(status_code=404, detail="Deporte no encontrado")
    
    db.delete(deporte)
    db.commit()
    return None