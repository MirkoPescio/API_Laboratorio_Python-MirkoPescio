from pydantic import BaseModel
from schemas.producto_schema import ProductoRespuesta


class CarritoProductoCrear(BaseModel):
    id_producto: int
    cantidad: int


class CarritoProductoRespuesta(BaseModel):
    id: int
    producto: ProductoRespuesta
    cantidad: int

    class Config:
        orm_mode = True


