from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database.database import get_db
from database.models import Usuario
from schemas.models import UsuarioCreate, UsuarioResponse, UsuarioUpdate
from utils.dependencies import get_current_user, get_current_active_user

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    dependencies=[Depends(get_current_active_user)]
)


@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(
        Usuario.matricula == usuario.matricula).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="Matrícula ya registrada")

    # Hashear la contraseña
    hashed_password = get_password_hash(usuario.contrasena)

    nuevo_usuario = Usuario(
        nombre_completo=usuario.nombre_completo,
        matricula=usuario.matricula,
        edad=usuario.edad,
        carrera_id=usuario.carrera_id,
        genero_id=usuario.genero_id,
        contrasena=hashed_password,
        acceso_id=usuario.acceso_id,
        imagen=usuario.imagen
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario


@router.get("/", response_model=List[UsuarioResponse])
def read_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).offset(skip).limit(limit).all()
    return usuarios


@router.get("/{usuario_id}", response_model=UsuarioResponse)
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario


@router.put("/{usuario_id}", response_model=UsuarioResponse)
def update_usuario(
    usuario_id: int,
    usuario: UsuarioUpdate,
    db: Session = Depends(get_db)
):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    update_data = usuario.dict(exclude_unset=True)
    if "contrasena" in update_data:
        update_data["contrasena"] = get_password_hash(
            update_data["contrasena"])

    for field, value in update_data.items():
        setattr(db_usuario, field, value)

    db.commit()
    db.refresh(db_usuario)
    return db_usuario


@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(db_usuario)
    db.commit()
    return None


# En routers/usuarios.py (extensión)

@router.post("/{usuario_id}/deportes/{deporte_id}", status_code=status.HTTP_204_NO_CONTENT)
def add_deporte_to_usuario(
    usuario_id: int,
    deporte_id: int,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    deporte = db.query(Deporte).filter(Deporte.id == deporte_id).first()
    if not deporte:
        raise HTTPException(status_code=404, detail="Deporte no encontrado")

    if deporte in usuario.deportes:
        raise HTTPException(
            status_code=400, detail="El usuario ya tiene este deporte")

    usuario.deportes.append(deporte)
    db.commit()
    return None


@router.delete("/{usuario_id}/deportes/{deporte_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_deporte_from_usuario(
    usuario_id: int,
    deporte_id: int,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    deporte = db.query(Deporte).filter(Deporte.id == deporte_id).first()
    if not deporte:
        raise HTTPException(status_code=404, detail="Deporte no encontrado")

    if deporte not in usuario.deportes:
        raise HTTPException(
            status_code=400, detail="El usuario no tiene este deporte")

    usuario.deportes.remove(deporte)
    db.commit()
    return None


@router.get("/me", response_model=UsuarioResponse)
def read_current_user(
    current_user: Usuario = Depends(
        get_current_user),  # Usa get_current_user aquí
    db: Session = Depends(get_db)
):
    """Obtiene el usuario actualmente autenticado"""
    return current_user


@router.put("/me/password")
def update_password(
    current_password: str,
    new_password: str,
    current_user: Usuario = Depends(get_current_user),  # Y aquí
    db: Session = Depends(get_db)
):
    if not verify_password(current_password, current_user.contrasena):
        raise HTTPException(
            status_code=400, detail="Contraseña actual incorrecta")

    current_user.contrasena = get_password_hash(new_password)
    db.commit()
    return {"message": "Contraseña actualizada"}
