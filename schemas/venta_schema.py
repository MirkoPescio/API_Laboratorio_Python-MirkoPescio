from datetime import date, time
from pydantic import BaseModel

from schemas.producto_schema import ProductoRespuesta

class VentaCrear(BaseModel):
    id_producto: int
    cantidad: int


class VentaRespuesta(BaseModel):
    id: int
    fecha: date
    hora: time
    id_producto: int
    cantidad: int
    precio_total: float

# Otro schema que coincide con las salidas que pide el PDF

class VentaRespuestaDetallado(BaseModel):
    id: int
    fecha: date
    hora: time
    producto: ProductoRespuesta
    cantidad: int
    precio_total: float

