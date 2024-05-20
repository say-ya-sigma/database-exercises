from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class User:
    id: int
    name: str
    email: str

users: List[User] = [
    User(id=1,name="Alice", email="alice@example.com"),
    User(id=2, name="Bob", email="bob@example.com")
]
