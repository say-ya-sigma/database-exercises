from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict
from .users import users

@dataclass(frozen=True)
class Post:
    id: int
    user_id: int
    title: str
    content: str
    created_at: datetime

user_post_counts: Dict[int, int] = {
    1: 10,
    2: 12,
    3: 15,
    4: 11,
    5: 13,
    6: 14,
    7: 10,
    8: 12,
    9: 11,
    10: 13,
    11: 15,
    12: 10,
    13: 12,
    14: 14,
    15: 11,
    16: 13,
    17: 10,
    18: 12,
    19: 15,
    20: 11,
    21: 14,
    22: 13,
    23: 10,
    24: 12,
    25: 11,
    26: 15,
    27: 14
}

def posts():
    posts: List[Post] = []
    target_users = users()

    # 各ユーザーに10件から15件のポストを作成
    post_id = 1
    for user in target_users:
        num_posts = user_post_counts[user.id]
        for _ in range(num_posts):
            title = f"{user.name}'s Post {post_id}"
            content = f"This is {user.name}'s post #{post_id}."
            created_at = datetime(2023, 6, 1) + timedelta(days=post_id)
            post = Post(id=post_id, user_id=user.id, title=title, content=content, created_at=created_at)
            posts.append(post)
            post_id += 1

    return posts
