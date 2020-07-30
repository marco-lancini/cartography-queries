#
# BUILD AND PUSH
# Version:
#   docker build -t cartography_queries:1.3 -f queries/Dockerfile .
#   docker tag cartography_queries:1.3 marcolancini/cartography_queries:1.3
#   docker push marcolancini/cartography_queries:1.3
# Latest:
#   docker tag cartography_queries:1.3 marcolancini/cartography_queries:latest
#   docker push marcolancini/cartography_queries:latest
#
FROM python:3.7-slim

RUN addgroup --gid 11111 app
RUN adduser --shell /bin/false --uid 11111 --ingroup app app

WORKDIR /app/
COPY queries/query_manager.py queries/queries.json /app/

RUN chmod +x query_manager.py
RUN chown -R app:app /app
USER app

ENTRYPOINT ["/app/query_manager.py"]
