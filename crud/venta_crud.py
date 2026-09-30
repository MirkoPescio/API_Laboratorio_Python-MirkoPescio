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
        return None
    
    productos = db.query(CarritoProducto).filter(CarritoProducto.id_carrito == carrito.id).all()
    
    total = 0
    for producto in productos:
        productoCarrito = db.query(Producto).filter(Producto.id == producto.id_producto).first()
        total += productoCarrito.precio * producto.cantidad

    nueva_venta = Venta(
        fecha = venta.fecha,
        hora = venta.hora,
        id_carrito = carrito.id,
        monto_total = total
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

