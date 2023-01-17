import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from prometheus_fastapi_instrumentator import Instrumentator

from api import router
from database import get_session, engine

# Create an application instance and connect endpoints
app = FastAPI(title='recommandations')
app.include_router(router)


@app.on_event('startup')
async def startup():
    # Check database connection
    get_session()

    # Configure prometheus /metrics
    Instrumentator().instrument(app).expose(app)


@app.on_event('shutdown')
async def shutdown():
    await engine.dispose()


@app.exception_handler(Exception)
async def exception_handler(request: Request, exception: Exception):
    return JSONResponse(status_code=400, content={'detail': str(exception)})


if __name__ == '__main__':
    uvicorn.run('app:app', port=8000, host='0.0.0.0', reload=True)
