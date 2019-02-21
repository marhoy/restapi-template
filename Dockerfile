FROM python:3.6-slim

RUN adduser -D flask

WORKDIR /home/flask

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY myapp myapp
COPY runserver.py ./

RUN chown -R flask:flask ./
USER flask

EXPOSE 5000
ENTRYPOINT ["python", "runserver.py"]
