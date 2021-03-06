FROM python:3.10

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install --upgrade pip -r requirements.txt

COPY . /app

EXPOSE 8001

CMD ["python", "app.py"]
