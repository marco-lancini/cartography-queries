FROM python:3.9.7-slim

LABEL org.opencontainers.image.source = "https://github.com/marco-lancini/cartography-queries"

RUN addgroup --gid 11111 app
RUN adduser --shell /bin/false --uid 11111 --ingroup app app

WORKDIR /app/
COPY queries/query_manager.py queries/queries.json /app/

RUN chmod +x query_manager.py
RUN chown -R app:app /app
USER app

ENTRYPOINT ["/app/query_manager.py"]
