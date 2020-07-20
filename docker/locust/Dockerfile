FROM python:3.6-alpine

COPY . /app
WORKDIR /app

RUN apk --no-cache add g++ zeromq-dev libffi-dev file make gcc musl-dev
RUN which python && pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod +x load_test.sh

EXPOSE 8089 5557 5558

# turn off python output buffering
ENV PYTHONUNBUFFERED=1