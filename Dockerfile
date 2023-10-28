# syntax=docker/dockerfile:1.2
# Use a multi-architecture base image
FROM --platform=$BUILDPLATFORM python:3.9-slim-buster AS base

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY ./src/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY ./src/ .

# Run the command to start the application
CMD [ "python", "scrape.py" ]