# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Expose a port if necessary (optional, can be used if your app uses networking)
EXPOSE 80

# Run the Python script when the container starts
CMD ["python", "run.py"]
