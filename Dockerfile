# Use the official Python slim image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the correct Cloud Run port
EXPOSE 8080

# Start the application using Gunicorn (Correct Path for `/src/`)
CMD ["gunicorn", "-b", "0.0.0.0:8080", "src.main:app"]