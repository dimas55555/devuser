import os

class Settings:
    TEST_MODE = os.getenv("TEST_MODE", "db")

settings = Settings()
