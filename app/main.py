import os                           # para obtener variables de entorno
import uvicorn                      # servidor ASGI para correr fastapi
from fastapi import FastAPI         # modulo principal para el servicio web
from .routers import todo           # rutas

os.environ['TZ'] = 'UTC'            # zona horaria UTC

title_detail = os.getenv('K_SERVICE', 'Local')     # obtener id del proyecto en produccion
version = os.getenv('K_REVISION', 'local')           # obtener version del deployment en prod
app = FastAPI(title=f'To-do app: {title_detail}', version=version)

# routers
app.include_router(todo.router, tags=['To-do'], prefix='/todos')


# healthcheck
@app.get('/')
def index():
    return {'status': 'OK'}


if __name__ == '__main__':
    uvicorn.run('app.main:app', host='0.0.0.0', port=8000, reload=True)
