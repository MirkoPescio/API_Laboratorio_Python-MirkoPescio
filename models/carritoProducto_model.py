from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class CarritoProducto(Base):
    __tablename__ = "carritoProductos"

    id = Column(Integer, primary_key=True)
    id_carrito = Column(Integer, ForeignKey("carritos.id"), nullable = False)
    id_producto = Column(Integer, ForeignKey("productos.id"), nullable = False)
    cantidad = Column(Integer, nullable = False)

    carrito = relationship("Carrito", back_populates="carritoProductos")
    producto = relationship("Producto")
    """
    Esta última línea de código es:
    Porque cuando devuelvas un CarritoProductoRespuestaDetallado, vas a querer incluir:
        * nombre del producto
        * precio
        * etc.
    """
