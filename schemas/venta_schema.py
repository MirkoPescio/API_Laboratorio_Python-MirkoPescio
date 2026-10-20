from datetime import date, time
from pydantic import BaseModel

from schemas.carrito_schema import CarritoRespuestaDetallado

class VentaCrear(BaseModel):
    id_carrito: int
    fecha: date
    hora: time

class VentaRespuesta(BaseModel):
    id: int
    fecha: date
    hora: time
    id_carrito: int

# Otro schema que coincide con las salidas que pide el PDF

class VentaRespuestaDetallado(VentaRespuesta):
    # Se pasa por parámetro VentaRespuesta por que así
    # hereda todos los atributos de esa clase VentaRespuesta y así
    # sumo lo correspondiente al detalle de los productos del carrito
    carrito: CarritoRespuestaDetallado

