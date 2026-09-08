from pydantic import BaseModel

# Clase para crear cada producto (POST)
class ProductoCrear(BaseModel):
    nombre: str
    precio: float

class ProductoRespuesta(ProductoCrear):
    id: int
    
