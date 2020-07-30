FROM python:3.7-slim

WORKDIR /app/
COPY consumers .
COPY queries/queries.json jupyter_notebooks/
COPY requirements.txt .

RUN groupadd -g 1001 app && useradd -ms /bin/bash -u 1001 -g app app && \
    python3 -m pip install -r requirements.txt && \
    chown -R app:app /app

USER app

CMD ["sh","-c","jupyter lab --ip=0.0.0.0 --port=8080"]

