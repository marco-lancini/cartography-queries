FROM python:3.9-slim

RUN addgroup --gid 11111 app
RUN adduser --shell /bin/false --uid 11111 --ingroup app app

COPY consumers/elasticsearch/deployment/py/requirements.txt /tmp/
RUN python3 -m pip install -r /tmp/requirements.txt

WORKDIR /app/
COPY consumers/neo4j_connector.py .
COPY consumers/elasticsearch/deployment/py/ .
COPY queries/queries.json .

RUN chown -R app:app /app
USER app

CMD ["python3", "/app/ingestor.py"]
