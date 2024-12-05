from fastapi import FastAPI
from app.routes import tea_routes, order_routes, user_routes, review_routes, auth_routes
from app.db.database import engine
from app.db.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tea Shop API")

app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(tea_routes.router, prefix="/teas", tags=["Teas"])
app.include_router(order_routes.router, prefix="/orders", tags=["Orders"])
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(review_routes.router, prefix="/reviews", tags=["Reviews"])

@app.get("/")
def root():
    return {"message": "Welcome to the Tea Shop API!"}
