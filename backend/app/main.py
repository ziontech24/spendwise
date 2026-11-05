from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI(
    title="SpendWise API",
    description="Backend API for the SpendWise personal finance application.",
    version="1.0.0"
)


# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "SpendWise API is running successfully."
    }