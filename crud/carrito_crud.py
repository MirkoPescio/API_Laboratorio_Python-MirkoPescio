from sqlalchemy.orm import Session

from models.carrito_model import Carrito
from models.venta_model import Venta
from schemas.carrito_schema import CarritoCrear


def get_carritos(db: Session):
    return db.query(Carrito).all()

def get_carrito(carrito_id: int, db: Session):
    return db.query(Carrito).filter(Carrito.id == carrito_id).first()

# Para crear un carrito:
def post_carrito(db: Session, carrito: CarritoCrear):
    nuevo_carrito = Carrito(
        fecha_creacion = carrito.fecha_creacion,
        estado = carrito.estado
    )
    db.add(nuevo_carrito)
    db.commit()
    db.refresh(nuevo_carrito)
    return nuevo_carrito

def update_carrito(carrito_id: int, updated: CarritoCrear, db: Session):
    carrito = get_carrito(carrito_id, db)

    if not carrito:
        return None

    # Para no modificar el carrito si se encuentra asociado a una venta:
    venta = db.query(Venta).filter(Venta.id_carrito == carrito_id).first()
    if venta:
        return "Carrito con venta"

    # No se puede reabrir un carrito cerrado
    if carrito.estado == "cerrado" and updated.estado == "abierto":
        return None

    # Estado inválido
    if updated.estado not in ["abierto", "cerrado"]:
        return None

    carrito.estado = updated.estado

    db.commit()
    db.refresh(carrito)
    return carrito

def delete_carrito(carrito_id: int, db: Session):
    carrito = get_carrito(carrito_id, db)

    if not carrito:
        return None

    # Para no modificar el carrito si se encuentra asociado a una venta:
    venta = db.query(Venta).filter(Venta.id_carrito == carrito_id).first()
    if venta:
        return "Carrito con venta"
    
    for cp in carrito.carritoProductos:
        db.delete(cp)

    db.delete(carrito)
    db.commit()
    return carrito



