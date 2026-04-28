from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.deps import get_db
from src.services.user_service_orm import get_user_service_orm

router = APIRouter(prefix="/orm/users", tags=["Users ORM"])


def get_service(db: Session = Depends(get_db)):
    return get_user_service_orm(db)


@router.post("/")
def create_user(data: dict, service=Depends(get_service)):
    return service.create_user(data)


@router.get("/")
def get_users(service=Depends(get_service)):
    return service.get_users()


@router.get("/{user_id}")
def get_user(user_id: str, service=Depends(get_service)):
    return service.get_user(user_id)


@router.delete("/{user_id}")
def delete_user(user_id: str, service=Depends(get_service)):
    return service.delete_user(user_id)