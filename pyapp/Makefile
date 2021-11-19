APP_DIR             ?= app
HOST				?= 0.0.0.0
PORT				?= 8888

# Run App
.PHONY: runapp start stop build
runapp:
	uvicorn ${APP_DIR}.main:app --reload --host ${HOST} --port ${PORT}

build:
	docker build -t pyapp-heroku:latest .
start:
	docker run -d --name pyapp-heroku -p 8888:8000 pyapp-heroku

stop:
	docker stop pyapp-heroku && docker rm pyapp-heroku

# heroku container:push web --app pyapp-cont
# heroku container:release web --app pyapp-cont

# heroku apps:destroy -a pyapp-cont --confirm pyapp-cont