from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from uuid import UUID
from src.models.user import User
from src.services.user_service import get_user_service, UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: User, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

@router.get("/", response_model=List[User])
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_users()

@router.get("/{user_id}", response_model=User)
def get_user(user_id: UUID, service: UserService = Depends(get_user_service)):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
def update_user(user_id: UUID, updated_user: User, service: UserService = Depends(get_user_service)):
    user = service.update_user(user_id, updated_user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: UUID, service: UserService = Depends(get_user_service)):
    deleted = service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return None