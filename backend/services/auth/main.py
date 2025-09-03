from fastapi import FastAPI
from app.routers import auth
from app.models.db import create_tables


app = FastAPI(
    title="jarvis-auth",
    debug=True,
    ignore_trailing_slash=True,
    root_path="/auth",
)

@app.on_event("startup")
async def startup_event():
    """Create database tables on startup"""
    create_tables()

# Include routers
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"service": "jarvis-auth"}
