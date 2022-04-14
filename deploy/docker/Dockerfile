FROM python:3.9-slim
LABEL maintainer "Alec Jordan <alecbjordan@gmail.com>"
WORKDIR /app

# Install Dependencies
RUN apt-get update
COPY src/requirements.txt .
# Cython needed first
RUN pip install Cython==0.29.21
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn[gevent]

# Copy Application Files
COPY src/ ./src
COPY auto_app.py .
COPY migrations/ ./migrations
COPY .env.SAMPLE .env

# Set Entry/Command
EXPOSE 5000
CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
