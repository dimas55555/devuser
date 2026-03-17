from fastapi import APIRouter, Depends
from uuid import UUID
from src.services.user_service import UserService, get_user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(name: str, email: str, service: UserService = Depends(get_user_service)):
    return service.create_user(name, email)


@router.get("/")
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_users()


@router.get("/{user_id}")
def get_user(user_id: UUID, service: UserService = Depends(get_user_service)):
    return service.get_user(user_id)


@router.delete("/{user_id}")
def delete_user(user_id: UUID, service: UserService = Depends(get_user_service)):
    return service.delete_user(user_id)