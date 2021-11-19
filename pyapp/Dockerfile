FROM python:slim-buster
# FROM python:3.9
ARG PORT=8000
ENV PORT=$PORT

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt
COPY ./app /code/app

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]



