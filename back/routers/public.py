from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import logging
from database.database import get_db
from database.models import Usuario

router = APIRouter(tags=["Public"])
logger = logging.getLogger(__name__)


@router.get("/usuarios/{matricula}/public", response_model=UsuarioPublicoResponse)
def get_public_user_profile(matricula: str, db: Session = Depends(get_db)):
    """
    Obtiene información pública de un usuario por su matrícula
    """
    try:
        logger.info(f"Buscando usuario con matrícula: {matricula}")

        usuario = db.query(Usuario).filter(
            Usuario.matricula == matricula).first()

        if not usuario:
            logger.warning(f"Usuario con matrícula {matricula} no encontrado")
            raise HTTPException(
                status_code=404,
                detail=f"Usuario con matrícula {matricula} no encontrado"
            )

        logger.info(f"Usuario encontrado: {usuario.nombre_completo}")

        return {
            "id": usuario.id,
            "nombre_completo": usuario.nombre_completo,
            "imagen": usuario.imagen,
            "carrera": usuario.carrera.nombre if usuario.carrera else None,
            "facultad": usuario.carrera.facultad.nombre if usuario.carrera and usuario.carrera.facultad else None,
            "deportes": [d.nombre for d in usuario.deportes],
            "peliculas": [p.titulo for p in usuario.peliculas]
        }

    except Exception as e:
        logger.error(f"Error al buscar usuario: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Error interno al procesar la solicitud"
        )
