from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Secure AI Voice Communication",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "Backend running"}
