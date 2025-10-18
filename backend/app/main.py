from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.objects import router as objects_router
from .routes.exports import router as exports_router

app = FastAPI(title="AI Travel Scout")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

app.include_router(objects_router)
app.include_router(exports_router)
