FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install fastapi uvicorn

COPY . /app/

EXPOSE 8000

CMD ["uvicorn", "fastapi_app.main:app", "--host", "python", "manage.py", "runserver", "0.0.0.0:8000"]