.DEFAULT_GOAL := help

run:
	poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload --env-file .local.env

migrate-create:
	alembic revision --autogenerate -m $(MIGRATION)


migrate-apply:
	alembic upgrade head