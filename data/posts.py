from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass(frozen=True)
class Post:
    id: int
    user_id: int
    title: str
    content: str
    created_at: datetime

posts: List[Post] = [
    Post(id=1, user_id=1, title="First Post", content="This is the first post.", created_at=datetime(2023, 6, 1, 10, 0, 0)),
    Post(id=2, user_id=2, title="Second Post", content="This is the second post.", created_at=datetime(2023, 6, 2, 15, 30, 0)),
    Post(id=3, user_id=1, title="Third Post", content="This is the third post.", created_at=datetime(2023, 6, 3, 9, 45, 0))
]