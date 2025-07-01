from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import Usuario
from utils.security import SECRET_KEY, ALGORITHM
from schemas.auth import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        matricula: str = payload.get("sub")
        if matricula is None:
            raise credentials_exception
        token_data = TokenData(matricula=matricula)
    except JWTError:
        raise credentials_exception

    usuario = db.query(Usuario).filter(
        Usuario.matricula == token_data.matricula).first()
    if usuario is None:
        raise credentials_exception
    return usuario


def get_current_active_user(current_user: Usuario = Depends(get_current_user)):
    if current_user.acceso_id != 1:  # 1 es admin
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    return current_user
