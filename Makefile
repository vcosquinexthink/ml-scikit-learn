# Define variables for the Docker image name and container name
IMAGE_NAME = flask-jupyter-app
CONTAINER_NAME = flask-jupyter-container

# Docker build command
build:
	docker build -t $(IMAGE_NAME) .

# Docker run command
run:
	docker run --rm -p 5000:5000 -p 8888:8888 --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Docker stop command
stop:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

# Run tests (optional, you can use curl or other testing tools to verify the app is running)
test:
	@echo "Testing Flask app on http://localhost:5000"
	@curl -s -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'

