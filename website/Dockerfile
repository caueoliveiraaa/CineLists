FROM python:3.12.1-slim-bullseye

WORKDIR /app

COPY ./website /app

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

ENTRYPOINT [ "python",  "main.py"]
