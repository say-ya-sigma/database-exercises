from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict
from .users import User, users
from .posts import Post, posts

@dataclass(frozen=True)
class Like:
    id: int
    user_id: int
    post_id: int
    created_at: datetime

# 選択するポストのインデックスを指定
selected_post_indices: List[int] = [2, 5, 7, 12, 15, 18, 20, 23, 26, 29, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58,
                                    61, 64, 67, 70, 73, 76, 79, 82, 85, 88]

# 各選択されたポストに対するいいねの数を指定
post_like_counts: Dict[int, int] = {
    2: 15, 5: 20, 7: 12, 12: 18, 15: 22, 18: 13, 20: 25, 23: 16, 26: 11, 29: 19,
    31: 24, 34: 10, 37: 17, 40: 21, 43: 14, 46: 26, 49: 23, 52: 13, 55: 19, 58: 16,
    61: 22, 64: 12, 67: 18, 70: 25, 73: 15, 76: 20, 79: 11, 82: 17, 85: 23, 88: 14
}

def likes():
    target_users: List[User] = users()  
    target_posts: List[Post] = posts()
    likes: List[Like] = []

    like_id = 1
    for post_index in selected_post_indices:
        post = target_posts[post_index]
        num_likes = post_like_counts[post_index]
        for user_index in range(num_likes):
            user = target_users[user_index % len(target_users)]
            
            # いいねの日時を設定（ポストの作成日時から30日以内）
            created_at = post.created_at + timedelta(days=(like_id % 31))
            
            like = Like(id=like_id, user_id=user.id, post_id=post.id, created_at=created_at)
            likes.append(like)
            like_id += 1

    return likes
