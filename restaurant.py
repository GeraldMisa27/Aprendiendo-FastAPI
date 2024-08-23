from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
app = FastAPI()


#entidad platillos
class Plato(BaseModel):
    id: int
    nombre: str
    detalles: str
    precio: float

platillos = [Plato(id=1, nombre="arroz blanco", detalles="el arroz es un cereal rico en carbohidratos y no contiene colesterol", precio=125.00),
             Plato(id=2, nombre="arroz blanco", detalles="el arroz es un cereal rico en carbohidratos", precio=140.00)]

@app.get("/Restaurante/") # raiz donde se esta ejecutando el programa
async def restaurant():
    return platillos


# para llamar a un parametro por path
#http://127.0.0.1:8000/Restaurante/1
@app.get("/Restaurante/{id}")
async def restaurant(id: int):
    plato_encontrado = next((Plato for Plato in platillos if Plato.id == id), None)
    if plato_encontrado: # si plato encontrado no es none
        return plato_encontrado.id
    else:
        return {"error": "Plato no encontrado"}
    

# llamar por query
#http://127.0.0.1:8000/Restaurante/?id=1
#para juntar parametros http://127.0.0.1:8000/Restaurantelambda/?id=1&nombre=arroz blanco

@app.get("/Restaurante/")
async def restaurant(id: int):
    return search_plato(id)

    #Post,Put y delete 

@app.post("/Restaurante/")
async def add_plato(plato: Plato):
    if type(search_plato(plato.id)) == Plato:
        return {"error": "el Plato ya existe"}
    else:    
        platillos.append(plato)
        return {"plato": plato, "error": "el Plato fue añadido exitosamente"}

@app.put("/Restaurante/")
async def update_plato(plato_actualizado: Plato):
    found = False
    for index, saved_plato in enumerate(platillos):
        if saved_plato.id == plato_actualizado.id:
            platillos[index] = plato_actualizado
            found = True
    if not found:
        return  {"error":"Plato no actualizado"}
    else:
        return {"plato": plato_actualizado ,"message": "Plato actualizado exitosamente"}

@app.delete("/Restaurante/{id}")
async def delete_plato(id: int):
    found = False
    for index, saved_plato in enumerate(platillos):
        if saved_plato.id == id:
            del platillos[index]
            found = True
    if not found:
        return  {"error":"Plato no existe"}
    else:
        return {"message": "Plato eliminado exitosamente"}

def search_plato(id: int):
    plato_encontrado = filter(lambda plato: plato.id == id, platillos)
    try:
        return list(plato_encontrado)[0]
    except:
        return{"error": "Plato no encontrado"}