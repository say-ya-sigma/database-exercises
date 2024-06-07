from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class User:
    id: int
    name: str
    email: str

def users():
    users: List[User] = [
        User(id=1, name="Alice", email="alice@example.com"),
        User(id=2, name="Bob", email="bob@example.com"),
        User(id=3, name="Carol", email="carol@example.com"),
        User(id=4, name="David", email="david@example.com"),
        User(id=5, name="Eve", email="eve@example.com"),
        User(id=6, name="Frank", email="frank@example.com"),
        User(id=7, name="Grace", email="grace@example.com"),
        User(id=8, name="Henry", email="henry@example.com"),
        User(id=9, name="Ivy", email="ivy@example.com"),
        User(id=10, name="Jack", email="jack@example.com"),
        User(id=11, name="Kate", email="kate@example.com"),
        User(id=12, name="Liam", email="liam@example.com"),
        User(id=13, name="Mia", email="mia@example.com"),
        User(id=14, name="Noah", email="noah@example.com"),
        User(id=15, name="Olivia", email="olivia@example.com"),
        User(id=16, name="Paul", email="paul@example.com"),
        User(id=17, name="Quinn", email="quinn@example.com"),
        User(id=18, name="Ryan", email="ryan@example.com"),
        User(id=19, name="Sarah", email="sarah@example.com"),
        User(id=20, name="Tom", email="tom@example.com"),
        User(id=21, name="Uma", email="uma@example.com"),
        User(id=22, name="Victor", email="victor@example.com"),
        User(id=23, name="Wendy", email="wendy@example.com"),
        User(id=24, name="Xavier", email="xavier@example.com"),
        User(id=25, name="Yara", email="yara@example.com"),
        User(id=26, name="Zoe", email="zoe@example.com"),
    ]
    return users
