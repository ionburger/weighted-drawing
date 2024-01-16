FROM python:3.12
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]