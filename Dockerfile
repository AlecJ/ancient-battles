FROM python:3.9-slim
WORKDIR /app

# Install Dependencies
COPY src/requirements.txt .
# Cython needed first
RUN pip install Cython==0.29.21
RUN pip install -r requirements.txt
# RUN apk del .build-deps

# Copy Application Files
COPY src/ .
COPY auto_app.py .
COPY .env .

# Set Entry/Command
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]