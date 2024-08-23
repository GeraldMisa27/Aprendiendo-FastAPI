from pydantic import BaseModel

class plato(BaseModel):
    id: int
    nombre: str
    detalles_plato: str
    precio: float

class entradas(plato):
    pass

class plato_principal(plato):
    pass

class postre(plato):
    pass

class bebidas(plato):
    pass

