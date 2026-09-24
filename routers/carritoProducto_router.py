from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from crud.carritoProducto_crud import (
    post_carritoProducto,
    delete_carritoProducto
)
from schemas.carritoProducto_schema import (
    CarritoProductoCrear,
    CarritoProductoRespuesta
)


router = APIRouter(prefix = "/carritos", tags=["CarritoProductos"])


@router.post("/{id_carrito}/productos/{id_producto}", response_model = CarritoProductoRespuesta)
def route_post_carritoProducto(id_carrito: int, id_producto: int,
    producto: CarritoProductoCrear, db: Session = Depends(get_db)):
        productoCarrito = post_carritoProducto(id_carrito, id_producto,
                producto, db)
        if not productoCarrito:
            raise HTTPException(status_code = 400, detail = "No se pudo agregar el producto al carrito")
        return productoCarrito


@router.delete("/{id_carrito}/productos/{id_producto}", response_model = CarritoProductoRespuesta)
def route_delete_carritoProducto(id_carrito: int, id_producto: int,
        db: Session = Depends(get_db)):
            productoCarrito = delete_carritoProducto(id_carrito,
                id_producto, db)
            if not productoCarrito:
                raise HTTPException(status_code = 404,
                    detail = f"Producto no encontrado para eliminar en el carrito de ID: {id_carrito}")
            return productoCarrito


