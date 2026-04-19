# Module 0: Docker Fundamentals

Docker is the foundation of Kubernetes. While K8s manages clusters, Docker manages the individual containers within those clusters. This module covers everything you need to build, run, and network containers.

## 1. The Core Workflow
The Docker workflow consists of three main steps: **Build**, **Ship**, and **Run**.

| Command | Type | Description |
|---------|------|-------------|
| `docker build` | Declarative (Dockerfile) | Creates an Image from a Dockerfile. |
| `docker tag/push` | Imperative | Labels and uploads images to a registry. |
| `docker run` | Imperative | Starts a container from an image. |

---

## 2. Dockerfile Deep Dive
A `Dockerfile` is a text document that contains all the commands a user could call on the command line to assemble an image.

### Language Examples (In the `src/` directory)

#### Go (Compiled, Multi-stage)
Multi-stage builds allow us to compile code in one container and only keep the resulting binary in the final image, drastically reducing size.
```dockerfile
# Build Stage
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY main.go .
RUN go build -o go-cli main.go

# Final Stage (Production)
FROM alpine:latest
COPY --from=builder /app/go-cli .
ENTRYPOINT ["./go-cli"]
```

#### Java (Fat Jar / Compiled)
```dockerfile
FROM openjdk:17-slim
WORKDIR /app
COPY App.java .
RUN javac App.java
CMD ["java", "App"]
```

#### PHP (Interpreted)
```dockerfile
FROM php:8.2-cli-alpine
COPY index.php .
CMD ["php", "index.php"]
```

---

## 3. Essential CLI Commands
Mastering these commands is key to debugging and managing containers.

### Build & Manage Images
```bash
# Build an image with a tag
docker build -t my-app:v1 .

# List all local images
docker images

# Remove an image
docker rmi my-app:v1
```

### Running & Debugging Containers
```bash
# Run a container in the background (detached)
docker run -d --name my-running-app my-app:v1

# Check container logs
docker logs my-running-app

# Execute a command inside a running container (shell access)
docker exec -it my-running-app /bin/sh

# Stop and remove a container
docker stop my-running-app
docker rm my-running-app
```

---

## 4. Networking & Port Exposure
Kubernetes networking relies on understanding how Docker maps ports.

### Mapping Ports
```bash
# Map Host Port 8080 to Container Port 80
docker run -p 8080:80 nginx
```

### Testing Connectivity (Curl)
```bash
# Verify the service is responding
curl -v http://localhost:8080
```

---

## 5. Persistent Storage (Volumes)
Containers are ephemeral (they die and lose data). Volumes keep data alive.

```bash
# Bind Mount (Maps a local folder to a container folder)
docker run -v C:\my-data:/app/data my-app

# Managed Volume (Docker handles the storage location)
docker run -v my-vol:/app/data my-app
```

---

## 6. Docker Compose (Declarative Multi-Container)
Docker Compose is like "Kubernetes Junior". It uses a YAML file to manage multiple services together.

**Example `docker-compose.yaml`**:
```yaml
version: '3.8'
services:
  web:
    build: ./src/go
    ports:
      - "8080:80"
  worker:
    build: ./src/php
    environment:
      - APP_ENV=production
```

Run with: `docker-compose up -d`
