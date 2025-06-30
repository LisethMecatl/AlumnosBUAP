from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.database import get_db
from database.models import Color
from schemas.models import ColorCreate, ColorResponse
from utils.dependencies import get_current_active_user

router = APIRouter(
    prefix="/colores",
    tags=["colores"],
    dependencies=[Depends(get_current_active_user)]
)

@router.post("/", response_model=ColorResponse, status_code=status.HTTP_201_CREATED)
def create_color(color: ColorCreate, db: Session = Depends(get_db)):
    db_color = Color(**color.dict())
    db.add(db_color)
    db.commit()
    db.refresh(db_color)
    return db_color

@router.get("/", response_model=List[ColorResponse])
def read_colores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    colores = db.query(Color).offset(skip).limit(limit).all()
    return colores

@router.get("/{color_id}", response_model=ColorResponse)
def read_color(color_id: int, db: Session = Depends(get_db)):
    color = db.query(Color).filter(Color.id == color_id).first()
    if color is None:
        raise HTTPException(status_code=404, detail="Color no encontrado")
    return color

@router.put("/{color_id}", response_model=ColorResponse)
def update_color(
    color_id: int, 
    color: ColorCreate, 
    db: Session = Depends(get_db)
):
    db_color = db.query(Color).filter(Color.id == color_id).first()
    if db_color is None:
        raise HTTPException(status_code=404, detail="Color no encontrado")
    
    db_color.nombre = color.nombre
    db.commit()
    db.refresh(db_color)
    return db_color

@router.delete("/{color_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_color(color_id: int, db: Session = Depends(get_db)):
    color = db.query(Color).filter(Color.id == color_id).first()
    if color is None:
        raise HTTPException(status_code=404, detail="Color no encontrado")
    
    db.delete(color)
    db.commit()
    return None