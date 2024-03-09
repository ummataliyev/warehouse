psql.up:
	docker run -d --name warehouse \
		-p 5430:5432 \
		-e POSTGRES_PASSWORD=$$DB_PASSWORD \
		-e POSTGRES_USER=$$DB_NAME \
		-e POSTGRES_DB=$$DB_USER \
		postgres:latest
