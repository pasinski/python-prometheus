FROM python:2.7.15-slim

# psutil requires gcc, so we'll install build-essential.
RUN apt-get update -y -q && \
    apt-get install --no-install-recommends -y -q \
        build-essential && \
    apt-get clean && \
    rm /var/lib/apt/lists/*_*

RUN pip install prometheus_client
RUN pip install psutil

WORKDIR /usr/src/app

ADD prometheus-exporter.py .

EXPOSE 8000

CMD [ "python", "prometheus-exporter.py" ]