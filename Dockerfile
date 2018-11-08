FROM registry.access.redhat.com/rhscl/python-36-rhel7

MAINTAINER Michal Pasinski <michal.pasinski-extern@deutschebahn.com>

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r ./requirements.txt

ADD prometheus-exporter.py .

EXPOSE 8000

CMD [ "python", "prometheus-exporter.py" ]