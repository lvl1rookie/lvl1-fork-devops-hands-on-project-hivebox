FROM python:3.12.3

ADD app.py .

CMD ["python", "./app.py" ]