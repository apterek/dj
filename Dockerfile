FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app

RUN addgroup django --system && adduser -aG django django

WORKDIR /app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends vim

COPY requirements.txt /tmp/requirements.txt
RUN pip install --trusted-host pypi.org --no-cache-dir --upgrade pip && \
    pip install --trusted-host pypi.org --no-cache-dir -r /tmp/requirements.txt

RUN apt-get autoremove -y --purge && \
    apt-get clean -y \

$ chmod +x app/entrypoint.sh \

RUN chown -R django:django /app

USER django

ENTRYPOINT ["/app/entrypoint.sh"]
