import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from api import router
from database import get_session

# Create an application instance and connect endpoints
app = FastAPI(title='recommandations')
app.include_router(router)


@app.on_event('startup')
async def startup():
    get_session()


@app.exception_handler(Exception)
async def exception_handler(request: Request, exception: Exception):
    return JSONResponse(status_code=400, content={'detail': str(exception)})


if __name__ == '__main__':
    uvicorn.run('app:app', port=8000, host='0.0.0.0', reload=True)
