#
# BUILD AND PUSH
# Version:
#   docker build -t cartography_jupyter:1.0 -f consumers/jupyter_notebooks/Dockerfile .
#   docker tag cartography_jupyter:1.0 marcolancini/cartography_jupyter:1.0
#   docker push marcolancini/cartography_jupyter:1.0
# Latest:
#   docker tag cartography_jupyter:1.0 marcolancini/cartography_jupyter:latest
#   docker push marcolancini/cartography_jupyter:latest
#
FROM python:3.7-slim

RUN addgroup --gid 11111 app
RUN adduser --shell /bin/false --uid 11111 --ingroup app app

COPY consumers/jupyter_notebooks/requirements.txt /tmp/
RUN python3 -m pip install -r /tmp/requirements.txt

WORKDIR /app/
COPY consumers/jupyter_notebooks/notebooks/ .
COPY queries/queries.json .

RUN chown -R app:app /app
USER app

CMD ["sh", "-c", "jupyter lab --ip=0.0.0.0 --port=8080"]
