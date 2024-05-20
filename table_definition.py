from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Column:
    name: str
    data_type: str

@dataclass(frozen=True)
class TableDefinition:
    table_name: str
    columns: List[Column]

table_definitions: List[TableDefinition] = [
    TableDefinition(
        table_name="users",
        columns=[
            Column(name="id", data_type="SERIAL PRIMARY KEY"),
            Column(name="name", data_type="VARCHAR(255)"),
            Column(name="email", data_type="VARCHAR(255)"),
        ]
    ),
    TableDefinition(
        table_name="posts",
        columns=[
            Column(name="id", data_type="SERIAL PRIMARY KEY"),
            Column(name="user_id", data_type="INTEGER REFERENCES users(id)"),
            Column(name="content", data_type="TEXT"),
            Column(name="created_at", data_type="TIMESTAMP DEFAULT CURRENT_TIMESTAMP"),
        ]
    ),
    TableDefinition(
        table_name="likes",
        columns=[
            Column(name="id", data_type="SERIAL PRIMARY KEY"),
            Column(name="user_id", data_type="INTEGER REFERENCES users(id)"),
            Column(name="post_id", data_type="INTEGER REFERENCES posts(id)"),
            Column(name="created_at", data_type="TIMESTAMP DEFAULT CURRENT_TIMESTAMP"),
        ]
    ),
]
