# main.py
import sys
from pathlib import Path

# Add project root directory to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

import uvicorn
from fastapi import FastAPI
from routes.auth_routes import router as auth_router

app = FastAPI(
    title="FastAPI Authentication Service",
    description="API for User Signup, Login, and Reset Password",
    version="1.0.0"
)

# Include Authentication Routes
app.include_router(auth_router)

@app.get("/", tags=["Health Check"])
async def root():
    return {"status": "ok", "message": "FastAPI Authentication Service is running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
