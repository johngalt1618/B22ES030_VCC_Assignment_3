FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r monitoring/requirements.txt
CMD ["python", "monitoring/alerting.py"]
