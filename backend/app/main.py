from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.routes.users import router as users_router
from app.routes.auth import router as auth_router
from app.database.connection import get_db


# Create the FastAPI application
app = FastAPI(
    title="SpendWise API",
    description="Backend API for the SpendWise personal finance application.",
    version="1.0.0"
)
# Register API routers
app.include_router(users_router)
app.include_router(auth_router)


# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "SpendWise API is running successfully."
    }


# Database connection test endpoint
@app.get("/health/database")
def database_health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
            "message": "SpendWise database connection is working."
        }

    except Exception:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "message": "Could not connect to the SpendWise database."
        }