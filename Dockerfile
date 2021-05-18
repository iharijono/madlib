FROM python:3.7.0-alpine3.8

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY api.py .
COPY main.py .
EXPOSE 9000

CMD python main.py