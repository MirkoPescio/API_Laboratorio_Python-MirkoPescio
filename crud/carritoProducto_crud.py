from sqlalchemy.orm import Session

from models.carrito_model import Carrito
from models.producto_model import Producto
from models.carritoProducto_model import CarritoProducto
from models.venta_model import Venta
from schemas.carritoProducto_schema import CarritoProductoCrear


def get_carritoProducto_por_carrito(id_carrito: int, db: Session):
    return db.query(CarritoProducto).filter(
            CarritoProducto.id_carrito == id_carrito
        ).all()

# Para obtener un registro específico (carrito + producto)
def get_carritoProducto(id_carrito: int, id_producto: int, db: Session):
    return db.query(CarritoProducto).filter(
        CarritoProducto.id_carrito == id_carrito,
        CarritoProducto.id_producto == id_producto
    ).first()

# Agregar un producto a un carrito:
def post_carritoProducto(id_carrito: int, id_producto: int, carritoProducto: CarritoProductoCrear, db: Session):

    carrito = db.query(Carrito).filter(Carrito.id == id_carrito).first()

    if not carrito:
        return None

    producto = db.query(Producto).filter(Producto.id == id_producto).first()

    if not producto:
        return "Producto inexistente"

    if carrito.estado == "cerrado":
        return None

    if carritoProducto.cantidad <= 0:
        return "Cantidad inválida"

    # Para no modificar el carrito si se encuentra asociado a una venta:
    venta = db.query(Venta).filter(Venta.id_carrito == id_carrito).first()
    if venta:
        return "Carrito con venta"

    carritoProducto_existente = get_carritoProducto(id_carrito, id_producto, db)

    if carritoProducto_existente:
        # Si ya existe el producto solamente actualizo la cantidad:
        carritoProducto_existente.cantidad += carritoProducto.cantidad
        db.commit()
        db.refresh(carritoProducto_existente)
        return carritoProducto_existente
    else:
        # Si no existe el producto, lo creo
        nuevo_carritoProducto = CarritoProducto(
            id_carrito = id_carrito,
            id_producto = id_producto,
            cantidad = carritoProducto.cantidad
        )
        
        db.add(nuevo_carritoProducto)
        db.commit()
        db.refresh(nuevo_carritoProducto)
        return nuevo_carritoProducto



# Eliminar un producto de un carrito:
def delete_carritoProducto(id_carrito: int, id_producto: int, db: Session):
    # Funcion delete
    carrito = db.query(Carrito).filter(Carrito.id == id_carrito).first()

    if not carrito:
        return None

    if carrito.estado == "cerrado":
        return None

    # Para no modificar el carrito si se encuentra asociado a una venta:
    venta = db.query(Venta).filter(Venta.id_carrito == id_carrito).first()
    if venta:
        return "carrito con venta"

    carritoProducto = get_carritoProducto(id_carrito, id_producto, db)

    if not carritoProducto:
        return "Producto no encontrado en el carrito"

    db.delete(carritoProducto)
    db.commit()
    return carritoProducto

