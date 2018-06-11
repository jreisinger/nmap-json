FROM python:alpine

RUN apk add --no-cache nmap

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY nmap-json.py run.sh ./

ENTRYPOINT ["./run.sh"]
