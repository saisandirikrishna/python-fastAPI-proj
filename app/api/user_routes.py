from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.services.user_service import (
    create_user,
    delete_user,
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

@router.delete("/delete/:id")
def add_user(id: int):
    print(id)
    return delete_user(id)