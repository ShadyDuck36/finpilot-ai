
from fastapi import FastAPI

app = FastAPI(
    title="FinPilot AI",
    description="Enterprise Invoice Processing Platform",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to FinPilot AI",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
