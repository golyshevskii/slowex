format-dev:
	poetry run black --config pyproject.toml slowex_test/
	poetry run isort --settings-path pyproject.toml slowex_test/
	poetry run flake8 --config .flake8 slowex_test/

# Docker
prune-a:
	docker system prune -a

up:
	docker-compose up

up-b:
	docker-compose up --build

down:
	docker-compose down
