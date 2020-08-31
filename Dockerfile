FROM alpine:3.10

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrate pip3

WORKDIR /code

COPY . /code

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "App.py"]