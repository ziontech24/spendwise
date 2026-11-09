import os
from pathlib import Path

from dotenv import load_dotenv


# Locate the backend directory
BACKEND_DIR = Path(__file__).resolve().parents[2]

# Load environment variables from backend/.env
load_dotenv(BACKEND_DIR / ".env")


# JWT authentication settings
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
)


# Validate the JWT secret key
if not JWT_SECRET_KEY or len(JWT_SECRET_KEY) < 32:
    raise RuntimeError(
        "JWT_SECRET_KEY is missing or too short. "
        "Check your backend/.env file."
    )