from fastapi.security import HTTPBasic
from passlib.context import CryptContext

DATABASE_URL = 'postgresql+asyncpg://user:password@database:5432/database'

security = HTTPBasic()

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
