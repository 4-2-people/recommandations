from fastapi.security import HTTPBasic
from passlib.context import CryptContext

DATABASE_URL = 'postgresql+asyncpg://user:password@0.0.0.0:8001/database'

security = HTTPBasic()

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
