from fastapi import FastAPI
from database import Base, engine
from routers.producto_router import router as producto_router
from routers.venta_router import router as venta_router
from routers.carrito_router import router as carrito_router
from routers.carritoProducto_router import router as carritoProducto_router


Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(producto_router)
app.include_router(carrito_router)
app.include_router(carritoProducto_router)
app.include_router(venta_router)
