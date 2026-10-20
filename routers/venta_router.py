from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.carrito_model import Carrito
from models.carritoProducto_model import CarritoProducto
from models.producto_model import Producto
from crud.venta_crud import (
    get_ventas, get_venta, post_venta, delete_venta
)
from schemas.venta_schema import VentaCrear, VentaRespuesta, VentaRespuestaDetallado


router = APIRouter(prefix="/ventas", tags=["ventas"])


@router.get("/", status_code=200, response_model=list[VentaRespuesta])
def route_get_ventas(db: Session = Depends(get_db)):
    return get_ventas(db)

@router.get("/{venta_id}")
def route_get_venta(venta_id: int, db: Session = Depends(get_db)):
    venta = get_venta(venta_id, db)
    if not venta:
        raise HTTPException(404, "Venta no encontrada")

    # Obtener carrito
    carrito = db.query(Carrito).filter(Carrito.id == venta.id_carrito).first()

    # Obtener productos del carrito
    productos_carrito = db.query(CarritoProducto).filter(
        CarritoProducto.id_carrito == carrito.id
    ).all()

    # Calcular precio_total
    precio_total = 0
    productos_detalle = []

    for item in productos_carrito:
        producto = db.query(Producto).filter(Producto.id == item.id_producto).first()
        precio_total += producto.precio * item.cantidad

        productos_detalle.append({
            "id": item.id,
            "producto": {
                "id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio
            },
            "cantidad": item.cantidad
        })

    # Armar respuesta detallada
    return {
        "id": venta.id,
        "fecha": venta.fecha,
        "hora": venta.hora,
        "precio_total": precio_total,
        "carrito": {
            "id": carrito.id,
            "fecha_creacion": carrito.fecha_creacion,
            "estado": carrito.estado,
            "productos": productos_detalle
        }
    }


@router.post("/", status_code=201, response_model=VentaRespuesta)
def route_post_venta(venta: VentaCrear, db: Session = Depends(get_db)):
    return post_venta(db, venta)

@router.delete("/{venta_id}", status_code=200, response_model=VentaRespuesta)
def route_delete_venta(venta_id: int, db: Session = Depends(get_db)):
    venta = delete_venta(venta_id, db)
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada para eliminar")
    return venta
