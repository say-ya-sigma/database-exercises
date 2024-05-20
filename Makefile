up:
	@docker compose up -d

build:
	@docker compose build

down:
	@docker compose down

bash:
	@docker compose exec worker bash

seed:
	@docker compose exec worker poetry run python worker.py