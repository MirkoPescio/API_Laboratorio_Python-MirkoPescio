from fastapi import FastAPI
from database import Base, engine
from routers.producto_router import router as producto_router


Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(producto_router)
