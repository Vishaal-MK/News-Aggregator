# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       libpq-dev \
    && apt-get clean \

# Install pip
RUN pip install --upgrade pip
# Copy the requirements file into the image
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the image
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Run the application
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]