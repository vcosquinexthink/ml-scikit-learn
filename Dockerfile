# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask default port 5000 and Jupyter Lab port 8888 to the outside world
EXPOSE 5000
EXPOSE 8888

# Install supervisor to manage multiple processes
RUN apt-get update && apt-get install -y supervisor

# Copy the supervisor configuration file to the container
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Start supervisor to run both Jupyter Lab and Flask
CMD ["/usr/bin/supervisord"]

