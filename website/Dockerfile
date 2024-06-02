FROM python:3.12.1-slim-bullseye

WORKDIR /app

COPY ./website /app

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run", "main.py" , "--server.port=8501", "--server.address=0.0.0.0"]
