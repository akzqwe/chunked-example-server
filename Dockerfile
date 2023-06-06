FROM python:3.9
COPY . /app
WORKDIR /app
EXPOSE 8080
CMD ["python", "server.py"]
