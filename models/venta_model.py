from sqlalchemy import Column, Integer, Float, Date, Time, ForeignKey
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
    id_carrito = Column(Integer, ForeignKey("carritos.id"), nullable = False)

    carrito = relationship("Carrito")
    
