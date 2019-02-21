FROM python:3.6-slim

RUN useradd flask

WORKDIR /home/flask

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY myapp myapp
COPY runserver.py ./

RUN chown -R flask:flask ./
USER flask

EXPOSE 5000
ENTRYPOINT ["./venv/bin/gunicorn", "-w", "4", "-b", ":5000", "myapp:app"]
