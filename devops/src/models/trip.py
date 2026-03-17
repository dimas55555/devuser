class Trip:
    def __init__(self, id: int, title: str, user_id: int, description: str):
        self.id = id
        self.title = title
        self.user_id = user_id
        self.description = description

    def __repr__(self):
        return f"Trip(id={self.id}, title='{self.title}', user_id={self.user_id})"