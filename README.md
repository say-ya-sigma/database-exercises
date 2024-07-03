## Database exercises

PostgreSQL で構築された DB 練習用のリポジトリです。

#### docker コンテナの起動

```bash
make up
```

#### DB への seed

```bash
make seed
```

シーディングされるデータは

- ユーザー 26 件
- ポスト 319 件
- ライク 531 県

#### DB への接続

- パラメータについては compose.yml 参照

```bash
export PGPASSWORD='password' && psql -U user -h 127.0.0.1 -p 5432 -d database_exercises
```
