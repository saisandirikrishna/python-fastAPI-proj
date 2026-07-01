from fastapi import FastAPI
from app.api.user_routes import router as user_router

app = FastAPI(
    title="FastAPI Demo Project",
    version="1.0.0"
)

app.include_router(user_router)


@app.get("/")
def home():
    print('home test1')
    return {
        "message": "FastAPI Application Running Successfully and deployed and testing"
    }