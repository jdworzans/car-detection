# syntax=docker/dockerfile:1
FROM python:3.10.4-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /web
COPY requirements.txt /web/
RUN pip install -r requirements.txt
COPY . /web/
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
