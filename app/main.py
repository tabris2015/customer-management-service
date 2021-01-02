import os                           # para obtener variables de entorno
import uvicorn                      # servidor ASGI para correr fastapi
from fastapi import FastAPI         # modulo principal para el servicio web
import app.settings as settings
from .routers import todo, transaction, client           # rutas

app = FastAPI(title=f'To-do app: {settings.TITLE}', version=settings.VERSION)

# routers
app.include_router(todo.router, tags=['To-do'], prefix='/todos')
app.include_router(transaction.router, tags=['Transactions'], prefix='/transactions')
app.include_router(client.router, tags=['Clients'], prefix='/clients')


# healthcheck
@app.get('/')
def index():
    return {'status': 'OK'}


if __name__ == '__main__':
    uvicorn.run('app.main:app', host='0.0.0.0', port=8000, reload=True)
