from typing import List, Optional
from uuid import UUID
from src.models.user import User

class UserService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserService, cls).__new__(cls)
            cls._instance.users: List[User] = []
        return cls._instance

    def create_user(self, user: User) -> User:
        self.users.append(user)
        return user

    def get_users(self) -> List[User]:
        return self.users

    def get_user(self, user_id: UUID) -> Optional[User]:
        return next((u for u in self.users if u.id == user_id), None)

    def update_user(self, user_id: UUID, updated_user: User) -> Optional[User]:
        for idx, u in enumerate(self.users):
            if u.id == user_id:
                self.users[idx] = updated_user
                return updated_user
        return None

    def delete_user(self, user_id: UUID) -> bool:
        for idx, u in enumerate(self.users):
            if u.id == user_id:
                del self.users[idx]
                return True
        return False

def get_user_service() -> UserService:
    return UserService()