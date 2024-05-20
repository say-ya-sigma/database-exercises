from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass(frozen=True)
class Like:
    id: int
    user_id: int
    post_id: int
    created_at: datetime

likes: List[Like] = [
    Like(id=1, user_id=2, post_id=1, created_at=datetime(2023, 6, 1, 11, 0, 0)),
    Like(id=2, user_id=1, post_id=2, created_at=datetime(2023, 6, 2, 16, 0, 0)),
    Like(id=3, user_id=2, post_id=3, created_at=datetime(2023, 6, 3, 10, 0, 0)),
    Like(id=4, user_id=1, post_id=1, created_at=datetime(2023, 6, 3, 12, 30, 0))
]
