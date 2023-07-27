# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# first we COPY only requirements. txt to ensure that later builds
# with changes to your sc code will be faster due to caching of this layer
COPY requirements.txt .

# Install the required packages using pip
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory to the working directory in the container
COPY . .

# EXPOSE 8000 
# specify Lambda handler that will be invoked on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

