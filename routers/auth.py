from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from database.database import get_db
from schemas.auth import Token, UsuarioLogin
from utils.security import (
    create_access_token, 
    verify_password,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from database.models import Usuario

router = APIRouter(tags=["auth"])

def authenticate_user(db: Session, matricula: str, contrasena: str):
    usuario = db.query(Usuario).filter(Usuario.matricula == matricula).first()
    if not usuario:
        return False
    
    # Si la contraseña está en texto plano (para migración)
    if usuario.contrasena == contrasena:
        # Actualiza a hash bcrypt
        usuario.contrasena = get_password_hash(contrasena)
        db.commit()
        return usuario
    
    # Verificación normal con bcrypt
    if not verify_password(contrasena, usuario.contrasena):
        return False
    return usuario

@router.post("/login", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    usuario = authenticate_user(db, form_data.username, form_data.password)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Matrícula o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": usuario.matricula}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}