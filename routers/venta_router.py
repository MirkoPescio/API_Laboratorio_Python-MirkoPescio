from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from crud.venta_crud import (
    get_ventas, get_venta, post_venta, delete_venta
)
from schemas.venta_schema import VentaCrear, VentaRespuesta, VentaRespuestaDetallado


router = APIRouter(prefix="/ventas", tags=["ventas"])


@router.get("/", status_code=200, response_model=list[VentaRespuesta])
def route_get_ventas(db: Session = Depends(get_db)):
    return get_ventas(db)

@router.get("/{venta_id}", status_code=200, response_model=VentaRespuestaDetallado)
def route_get_venta(venta_id: int, db: Session = Depends(get_db)):
    venta = get_venta(venta_id, db)
    if not venta:
        raise HTTPException(status_code = 404, detail="Venta no encontrada")
    return venta

@router.post("/", status_code=201, response_model=VentaRespuesta)
def route_post_venta(venta: VentaCrear, db: Session = Depends(get_db)):
    return post_venta(db, venta)

@router.delete("/{venta_id}", status_code=200, response_model=VentaRespuesta)
def route_delete_venta(venta_id: int, db: Session = Depends(get_db)):
    venta = delete_venta(db, venta_id)
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada para eliminar")
    return venta
