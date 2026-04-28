from src.cache.user_cache import cache

class UserServiceCache:

    def create_user(self, data):
        return cache.create(data)

    def get_users(self):
        return cache.get_all()

    def get_user(self, user_id):
        return cache.get(user_id)

    def delete_user(self, user_id):
        return cache.delete(user_id)

def get_user_service_cache():
    return UserServiceCache()