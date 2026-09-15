from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from crud.producto_crud import (
    get_producto, get_productos, post_producto,
    update_producto, delete_producto
)
from schemas.producto_schema import ProductoCrear, ProductoRespuesta


router = APIRouter(prefix="/productos", tags=["productos"])


@router.get("/", status_code=200, response_model=list[ProductoRespuesta])
def route_get_productos(db: Session = Depends(get_db)):
    return get_productos(db)

@router.get("/{producto_id}", status_code=200, response_model=ProductoRespuesta)
def route_get_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = get_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/", status_code=201, response_model=ProductoRespuesta)
def route_post_producto(producto: ProductoCrear, db: Session = Depends(get_db)):
    return post_producto(db, producto)

@router.put("/{producto_id}", status_code=200, response_model=ProductoRespuesta)
def route_update_producto(producto_id: int, updated: ProductoCrear, db: Session = Depends(get_db)):
    producto = update_producto(db, producto_id, updated)
    if not producto:
        raise HTTPException(status_code=404, detail="No se encontró ningún producto con el ID indicado para actualizarlo")
    return producto

@router.delete("/{producto_id}", status_code=200, response_model=ProductoRespuesta)
def route_delete_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = delete_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="No se encontró ningún producto con el ID indicado para eliminarlo")
    return producto

