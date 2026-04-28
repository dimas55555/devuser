from uuid import UUID, uuid4

class UserCache:
    def __init__(self):
        self.users = {}

    def create(self, data):
        user_id = str(uuid4())
        user = {
            "id": user_id,
            **data
        }
        self.users[user_id] = user
        return user

    def get_all(self):
        return list(self.users.values())

    def get(self, user_id):
        return self.users.get(user_id)

    def delete(self, user_id):
        return self.users.pop(user_id, None)

cache = UserCache()