from typing import List, Optional
from uuid import UUID, uuid4
from src.models.user import User

# Singleton UserService
class UserService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserService, cls).__new__(cls)
            cls._instance.users = []  # In-memory storage
        return cls._instance

    def create_user(self, name: str, email: str) -> User:
        user = User(id=uuid4(), name=name, email=email)
        self.users.append(user)
        return user

    def get_users(self) -> List[User]:
        return self.users

    def get_user(self, user_id: UUID) -> Optional[User]:
        return next((user for user in self.users if user.id == user_id), None)

    def update_user(self, user_id: UUID, name: str, email: str) -> Optional[User]:
        for idx, user in enumerate(self.users):
            if user.id == user_id:
                self.users[idx].name = name
                self.users[idx].email = email
                return self.users[idx]
        return None

    def delete_user(self, user_id: UUID) -> bool:
        for idx, user in enumerate(self.users):
            if user.id == user_id:
                del self.users[idx]
                return True
        return False

# Dependency injection
def get_user_service() -> UserService:
    return UserService()