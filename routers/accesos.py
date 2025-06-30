from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.database import get_db
from database.models import Acceso
from schemas.models import AccesoCreate, AccesoResponse
from utils.dependencies import get_current_active_user

router = APIRouter(
    prefix="/accesos",
    tags=["accesos"],
    dependencies=[Depends(get_current_active_user)]
)

@router.post("/", response_model=AccesoResponse, status_code=status.HTTP_201_CREATED)
def create_acceso(acceso: AccesoCreate, db: Session = Depends(get_db)):
    db_acceso = Acceso(**acceso.dict())
    db.add(db_acceso)
    db.commit()
    db.refresh(db_acceso)
    return db_acceso

@router.get("/", response_model=List[AccesoResponse])
def read_accesos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    accesos = db.query(Acceso).offset(skip).limit(limit).all()
    return accesos

@router.get("/{acceso_id}", response_model=AccesoResponse)
def read_acceso(acceso_id: int, db: Session = Depends(get_db)):
    acceso = db.query(Acceso).filter(Acceso.id == acceso_id).first()
    if acceso is None:
        raise HTTPException(status_code=404, detail="Nivel de acceso no encontrado")
    return acceso

@router.put("/{acceso_id}", response_model=AccesoResponse)
def update_acceso(
    acceso_id: int, 
    acceso: AccesoCreate, 
    db: Session = Depends(get_db)
):
    db_acceso = db.query(Acceso).filter(Acceso.id == acceso_id).first()
    if db_acceso is None:
        raise HTTPException(status_code=404, detail="Nivel de acceso no encontrado")
    
    db_acceso.nivel = acceso.nivel
    db.commit()
    db.refresh(db_acceso)
    return db_acceso

@router.delete("/{acceso_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_acceso(acceso_id: int, db: Session = Depends(get_db)):
    acceso = db.query(Acceso).filter(Acceso.id == acceso_id).first()
    if acceso is None:
        raise HTTPException(status_code=404, detail="Nivel de acceso no encontrado")
    
    db.delete(acceso)
    db.commit()
    return None