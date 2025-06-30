from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.database import get_db
from database.models import Hobby
from schemas.models import HobbyCreate, HobbyResponse
from utils.dependencies import get_current_active_user

router = APIRouter(
    prefix="/hobbies",
    tags=["hobbies"],
    dependencies=[Depends(get_current_active_user)]
)

@router.post("/", response_model=HobbyResponse, status_code=status.HTTP_201_CREATED)
def create_hobby(hobby: HobbyCreate, db: Session = Depends(get_db)):
    db_hobby = Hobby(**hobby.dict())
    db.add(db_hobby)
    db.commit()
    db.refresh(db_hobby)
    return db_hobby

@router.get("/", response_model=List[HobbyResponse])
def read_hobbies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hobbies = db.query(Hobby).offset(skip).limit(limit).all()
    return hobbies

@router.get("/{hobby_id}", response_model=HobbyResponse)
def read_hobby(hobby_id: int, db: Session = Depends(get_db)):
    hobby = db.query(Hobby).filter(Hobby.id == hobby_id).first()
    if hobby is None:
        raise HTTPException(status_code=404, detail="Hobby no encontrado")
    return hobby

@router.put("/{hobby_id}", response_model=HobbyResponse)
def update_hobby(
    hobby_id: int, 
    hobby: HobbyCreate, 
    db: Session = Depends(get_db)
):
    db_hobby = db.query(Hobby).filter(Hobby.id == hobby_id).first()
    if db_hobby is None:
        raise HTTPException(status_code=404, detail="Hobby no encontrado")
    
    db_hobby.nombre = hobby.nombre
    db.commit()
    db.refresh(db_hobby)
    return db_hobby

@router.delete("/{hobby_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hobby(hobby_id: int, db: Session = Depends(get_db)):
    hobby = db.query(Hobby).filter(Hobby.id == hobby_id).first()
    if hobby is None:
        raise HTTPException(status_code=404, detail="Hobby no encontrado")
    
    db.delete(hobby)
    db.commit()
    return None