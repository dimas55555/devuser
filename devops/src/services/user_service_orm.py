from sqlalchemy.orm import Session
from src.models.user_orm import UserORM


class UserServiceORM:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, data):
        user = UserORM(**data)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_users(self):
        return self.db.query(UserORM).all()

    def get_user(self, user_id):
        return self.db.query(UserORM).filter(UserORM.id == user_id).first()

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
        return user


def get_user_service_orm(db: Session):
    return UserServiceORM(db)