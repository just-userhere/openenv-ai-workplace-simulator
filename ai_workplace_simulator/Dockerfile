# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set Python path so the env module can be found
ENV PYTHONPATH=/app

# Command to run the inference script
CMD ["python", "scripts/run_inference.py"]
