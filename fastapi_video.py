from fastapi import FastAPI

app = FastAPI()

@app.get("/") # raiz donde se esta ejecutando el programa
async def root():
    return "Hola FastAPI!"

#click derecho sobre el archivo quue contiene la app fastapi open in integrated terminal
# hacer un uvicorn nombre del documento que contiene fastapi:app --reload

@app.get("/url") # raiz donde se esta ejecutando el programa
async def url():
    return {"url_curso":"https://mouredev.com/python"}

# para ver la documentacion -> http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc

#POST:para crear datos.
#GET:leer datos.
#PUT:para actualizar datos.
#DELETE:borrar datos.

