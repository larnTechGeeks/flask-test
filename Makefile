build:
	docker-compose build

build-app:
	docker image build -t techapp .

run-app:
	docker run -p 8001:8001 -d techapp

up:
	docker-compose up

ps:
	docker-compose ps

logs:
	docker-compose logs -f

rm: stop
	docker-compose rm

stop:
	docker-compose stop

down:
	docker-compose down --remove-orphans

test:
	cd src; python -m pytest

server:
	cd src; python3 app.py

server-1:
	docker run -p 5000:5000 -d app
