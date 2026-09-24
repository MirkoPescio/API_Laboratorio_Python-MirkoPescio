from datetime import date
from pydantic import BaseModel
from schemas.carritoProducto_schema import CarritoProductoRespuesta

class CarritoCrear(BaseModel):
    fecha_creacion: date
    estado: str


class CarritoRespuesta(BaseModel):
    id: int
    fecha_creacion: date
    estado: str

    class Config:
        orm_mode = True


class CarritoRespuestaDetallado(CarritoRespuesta):
    carritoProductos: list[CarritoProductoRespuesta]


