FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app



RUN apt-get update && pip install -r requirements.txt
#This allows Render to detect the port
EXPOSE 8000  

CMD ["python3", "app.py"]