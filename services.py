from models import User
from typing import List

class UserService:
    def __init__(self):
        self.users = [
            User(id=1, username="user1", email="user1@example.com"),
            User(id=2, username="user2", email="user2@example.com")
        ]

    def get_users(self) -> List[User]:
        return self.users
    
    def get_user(self, user_id: int) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        return None
