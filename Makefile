run: stop
	docker compose build
	docker compose up -d
	docker compose ps
logs:
	docker compose logs website
stop:
	docker compose down -t 0
