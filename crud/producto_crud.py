from sqlalchemy.orm import Session
from models.producto_model import Producto
from schemas.producto_schema import ProductoCrear


def get_productos(db: Session):
    return db.query(Producto).all()

def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def post_producto(db: Session, producto: ProductoCrear):
    nuevo_producto = Producto(
        nombre = producto.nombre,
        precio = producto.precio
    )
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

def update_producto(db: Session, producto_id: int, updated: ProductoCrear):
    producto = get_producto(db, producto_id)
    if not producto:
        return None

    producto.nombre = updated.nombre
    producto.precio = updated.precio

    db.commit()
    db.refresh(producto)
    return producto

def delete_producto(db: Session, producto_id: int):
    producto = get_producto(db, producto_id)
    if not producto:
        return None

    db.delete(producto)
    db.commit()
    return producto

