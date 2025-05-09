from fastapi import FastAPI
from routes import user, building, energy, feedback
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user.router, prefix="/auth", tags=["Auth"])
app.include_router(building.router, prefix="/buildings", tags=["Buildings"])
app.include_router(energy.router, prefix="/energy", tags=["Energy"])
app.include_router(feedback.router, prefix="/feedback", tags=["Feedback"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)