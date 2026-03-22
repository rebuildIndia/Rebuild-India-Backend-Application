from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.api_v1.endpoints.user import router as user_router

app = FastAPI(title="Rebuild India Backend Application",description="Backend logic for Rebuild India")

Base.metadata.create_all(bind=engine)

app.include_router(user_router, prefix="/users", tags=["Users"])