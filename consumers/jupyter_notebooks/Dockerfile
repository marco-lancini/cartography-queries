FROM python:3.7-slim

LABEL org.opencontainers.image.source = "https://github.com/marco-lancini/cartography-queries"

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
