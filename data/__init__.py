from dataclasses import dataclass
from typing import List
from .users import User, users
from .posts import Post, posts
from .likes import Like, likes

@dataclass(frozen=True)
class Data:
    users: List[User]
    posts: List[Post]
    likes: List[Like]

data = Data(users=users(), posts=posts(), likes=likes())