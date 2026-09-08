from sqlalchemy import Column, Integer, String, Float, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models.producto_model import Producto

class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, 
        primary_key = True,
        index = True,
        autoincrement = True,
        nullable = False
    )
    fecha = Column(Date, nullable = False)
    hora = Column(Time, nullable = False)
    id_producto = Column(Integer, ForeignKey("productos.id"), nullable = False)
    cantidad = Column(Integer, nullable = False)
    precio_total = Column(Float, nullable = False)

    producto = relationship("Producto")
