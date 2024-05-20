import os
import psycopg2
from table_definition import table_definitions
from data import data

# 環境変数からデータベースのURLを取得
database_url = os.environ.get('DATABASE_URL')

conn = psycopg2.connect(database_url)

cur = conn.cursor()

# 以前のデータベースを削除
cur.execute("DROP SCHEMA public CASCADE")
cur.execute("CREATE SCHEMA public")

# テーブルを作成する
for table_definition in table_definitions:
    table_name = table_definition.table_name
    columns = [f"{column.name} {column.data_type}" for column in table_definition.columns]
    create_table_query = f"CREATE TABLE {table_name} ({', '.join(columns)})"
    cur.execute(create_table_query)

# データを順次処理してデータベースに投入する
for table_definition in table_definitions:
    table_name = table_definition.table_name
    table_data = getattr(data, table_name)
    for item in table_data:
        columns = [column.name for column in table_definition.columns]
        values = [getattr(item, column) for column in columns]
        insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"
        cur.execute(insert_query, values)

conn.commit()
cur.close()
conn.close()