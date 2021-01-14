import os                           # para obtener variables de entorno
import uvicorn                      # servidor ASGI para correr fastapi
from fastapi import FastAPI         # modulo principal para el servicio web
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin
import app.settings as settings
from .routers import todo, transaction, client, account           # rutas

firebase_admin.initialize_app()

app = FastAPI(title=f'To-do app: {settings.TITLE}', version=settings.VERSION)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
    )
# routers
app.include_router(todo.router, tags=['To-do'])
app.include_router(transaction.router, tags=['Transactions'])
app.include_router(client.router, tags=['Clients'])
app.include_router(account.router, tags=['Accounts'])


# healthcheck
@app.get('/')
def index():
    return {'status': 'Todo blue'}


if __name__ == '__main__':
    uvicorn.run('app.main:app', host='0.0.0.0', port=8000, reload=True)
