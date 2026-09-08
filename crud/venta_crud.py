from sqlalchemy.orm import Session
from datetime import datetime

from models.venta_model import Venta
from models.producto_model import Producto
from schemas.venta_schema import VentaCrear


def get_ventas(db: Session):
    return db.query(Venta).all()

def get_venta(venta_id: int, db: Session):
    return db.query(Venta).filter(Venta.id == venta_id).first()

def post_venta(db: Session, venta: VentaCrear):
    producto = db.query(Producto).filter(Producto.id == venta.id_producto).first()
    if not producto:
        return None

    total = producto.precio * venta.cantidad

    nueva_venta = Venta(
        fecha = datetime.now().date(),
        hora = datetime.now().time(),
        id_producto = venta.id_producto,
        cantidad = venta.cantidad,
        precio_total = total
    )
    db.add(nueva_venta)
    db.commit()
    db.refresh(nueva_venta)
    return nueva_venta

def delete_venta(venta_id: int, db: Session):
    venta = get_venta(venta_id, db)
    if not venta:
        return None

    db.delete(venta)
    db.commit()
    return venta

