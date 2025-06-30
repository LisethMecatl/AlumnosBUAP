# Importaciones necesarias
from utils.security import get_password_hash
from database.database import SessionLocal
from database.models import Usuario  # ¡Esta es la línea que faltaba!

def hash_passwords():
    db = SessionLocal()
    try:
        usuarios = db.query(Usuario).all()
        
        for usuario in usuarios:
            if usuario.contrasena and not usuario.contrasena.startswith("$2b$"):
                print(f"Hasheando contraseña para usuario: {usuario.nombre_completo}")
                usuario.contrasena = get_password_hash(usuario.contrasena)
                db.commit()
        
        print("¡Proceso completado! Todas las contraseñas han sido hasheadas.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    hash_passwords()