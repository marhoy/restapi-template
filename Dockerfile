FROM python:3.6-slim

RUN useradd flask

WORKDIR /home/flask

COPY requirements.txt requirements.txt
COPY gunicorn_config.py gunicorn_config.py
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY restapi restapi

RUN chown -R flask:flask ./
USER flask

EXPOSE 5000
ENTRYPOINT ["./venv/bin/gunicorn", "-c", "gunicorn_config.py", "restapi:app"]
