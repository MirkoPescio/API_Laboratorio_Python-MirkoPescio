from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from crud.carrito_crud import (
    get_carritos,
    get_carrito,
    post_carrito,
    update_carrito,
    delete_carrito
)
from schemas.carrito_schema import CarritoCrear, CarritoRespuesta, CarritoRespuestaDetallado


router = APIRouter(prefix = "/carritos", tags = ["Carritos"])


@router.get("/", response_model=list[CarritoRespuesta])
def route_get_carritos(db: Session = Depends(get_db)):
    return get_carritos(db)

@router.get("/{carrito_id}", response_model = CarritoRespuestaDetallado)
def route_get_carrito(carrito_id: int, db: Session = Depends(get_db)):
    carrito = get_carrito(carrito_id, db)
    if not carrito:
        raise HTTPException(status_code = 404, detail = "Carrito no encontrado")
    return carrito

@router.post("/", response_model = CarritoRespuesta)
def route_post_carrito(carrito: CarritoCrear, db: Session = Depends(get_db)):
    return post_carrito(db, carrito)

@router.put("/{carrito_id}", response_model=CarritoRespuesta)
def route_update_carrito(carrito_id: int, updated: CarritoCrear, db: Session = Depends(get_db)):
    carrito = update_carrito(carrito_id, updated, db)
    if not carrito:
        raise HTTPException(status_code = 404, detail = "Carrito no encontrado para actualizarse")
    return carrito

@router.delete("/{carrito_id}", response_model = CarritoRespuesta)
def route_delete_carrito(carrito_id: int, db: Session = Depends(get_db)):
    carrito = delete_carrito(carrito_id, db)
    if not carrito:
        raise HTTPException(status_code = 404, detail = "No se encontró ningún carrito para eliminar")
    return carrito

