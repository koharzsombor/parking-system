from fastapi import FastAPI
from app.infrastructure.database.base import Base
from app.infrastructure.database.session import engine
from app.api.routes.reservations import router as reservation_router
from app.api.routes.parking_spot import router as spot_router
from app.api.routes.users import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Parking System")

@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok"}

app.include_router(reservation_router)
app.include_router(spot_router)
app.include_router(user_router)
