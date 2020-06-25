FROM python:3.7.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PORT 8888

WORKDIR /server
COPY . /server

RUN set -x \
    && pip install -r requirements.txt \
    && python setup.py develop 

CMD sh dev-server.sh
