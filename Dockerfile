FROM python:3.7-slim

RUN addgroup --gid 11111 app
RUN adduser --shell /bin/false --uid 11111 --ingroup app app

WORKDIR /app/
COPY query_manager.py .
COPY queries.json .

RUN chmod +x query_manager.py
RUN chown -R app:app /app
USER app

ENTRYPOINT ["/app/query_manager.py"]