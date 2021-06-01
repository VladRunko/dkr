FROM python:3.8.1
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
COPY . /app/
COPY requirements.txt .
RUN ["pip", "install", "-r", "requirements.txt"]
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]