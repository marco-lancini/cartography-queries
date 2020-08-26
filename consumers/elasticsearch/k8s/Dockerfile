#
# BUILD AND PUSH
# Version:
#   docker build -t cartography_elastic_ingestor:1.0 -f consumers/elasticsearch/k8s/Dockerfile .
#   docker tag cartography_elastic_ingestor:1.0 marcolancini/cartography_elastic_ingestor:1.0
#   docker push marcolancini/cartography_elastic_ingestor:1.0
# Latest:
#   docker tag cartography_elastic_ingestor:1.0 marcolancini/cartography_elastic_ingestor:latest
#   docker push marcolancini/cartography_elastic_ingestor:latest
#
FROM python:3.7-slim

RUN addgroup --gid 11111 app
RUN adduser --shell /bin/false --uid 11111 --ingroup app app

COPY consumers/elasticsearch/py/requirements.txt /tmp/
RUN python3 -m pip install -r /tmp/requirements.txt

WORKDIR /app/
COPY consumers/neo4j_connector.py .
COPY consumers/elasticsearch/py/ .
COPY queries/queries.json .

RUN chown -R app:app /app
USER app

CMD ["python3", "/app/ingestor.py"]
