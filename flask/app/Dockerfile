FROM python:3.8
WORKDIR /app
ADD app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python3","./app.py"]
