# Use a Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install necessary dependencies including git
RUN apt-get update && apt-get install -y git && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the contents of the project to the /app directory
COPY . .

# Ensure the entrypoint script exists and is executable
RUN chmod +x /app/.github/scripts/entrypoint.sh

# Set the entrypoint to the entrypoint script
ENTRYPOINT ["/bin/bash", "/app/.github/scripts/entrypoint.sh"]
