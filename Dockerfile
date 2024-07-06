FROM python:3.8-slim-buster
WORKDIR /app
COPY  . /app

RUN pip install -r requirements.txt
RUN apt update -y && apt install awscli -y

CMD ["python3", "application.py"]