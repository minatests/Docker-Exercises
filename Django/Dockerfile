FROM python:3.9-alpine3.13

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apk update && \
    apk add postgresql-dev gcc musl-dev jpeg-dev zlib-dev libffi-dev
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
