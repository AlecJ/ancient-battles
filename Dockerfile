FROM python:3.9-alpine
WORKDIR /app

# Install Dependencies
RUN apk update && \
    apk add --no-cache postgresql-dev gcc musl-dev \
    libressl-dev libffi-dev libxml2-dev libxslt-dev
COPY src/requirements.txt .
RUN pip install Cython==0.29.21
RUN pip install -r requirements.txt
# Because `pip install requirements` would be too simple

# Copy Application Files
COPY src/ .
COPY auto_app.py .
COPY .env .

# Set Entry/Command
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]