from sqlalchemy import Column, Integer, Date, String
from sqlalchemy.orm import relationship
from database import Base

class Carrito(Base):
    __tablename__ = 'carritos'

    id = Column(
        Integer,
        primary_key = True,
        autoincrement = True,
        index = True
    )
    fecha_creacion = Column(Date, nullable = False)
    estado = Column(String, nullable = False)
    carritoProductos = relationship("CarritoProducto", back_populates="carrito")


