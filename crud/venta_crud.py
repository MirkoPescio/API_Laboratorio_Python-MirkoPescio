from sqlalchemy.orm import Session
from datetime import datetime

from models.venta_model import Venta
from models.carrito_model import Carrito
from models.producto_model import Producto
from models.carritoProducto_model import CarritoProducto

from schemas.venta_schema import VentaCrear


def get_ventas(db: Session):
    return db.query(Venta).all()

def get_venta(venta_id: int, db: Session):
    return db.query(Venta).filter(Venta.id == venta_id).first()

def post_venta(db: Session, venta: VentaCrear):
    carrito = db.query(Carrito).filter(Carrito.id == venta.id_carrito).first()
    
    if not carrito:
        return None
    
    if carrito.estado != "cerrado":
        return "Carrito abierto"
    
    venta_existente = db.query(Venta).filter(Venta.id_carrito == venta.id_carrito).first()
    
    if venta_existente:
        return "Carrito con venta ya registrada"
    
    nueva_venta = Venta(
        fecha = venta.fecha,
        hora = venta.hora,
        id_carrito = carrito.id,
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

