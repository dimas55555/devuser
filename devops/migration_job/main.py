from src.db.database import engine
from src.db.base import Base

from src.models.user_orm import UserORM

def run_migrations():
    print("Starting migrations...")

    Base.metadata.create_all(bind=engine)

    print("Migrations applied successfully!")

if __name__ == "__main__":
    run_migrations()
