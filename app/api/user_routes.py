from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.services.user_service import (
    create_user,
    get_users
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
def fetch_users():
    return get_users()


@router.post("/")
def add_user(user: UserCreate):
    return create_user(user)