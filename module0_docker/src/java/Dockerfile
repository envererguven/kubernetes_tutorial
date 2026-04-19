# Build Stage
FROM openjdk:17-slim AS builder

WORKDIR /app

# Copy source
COPY App.java .

# Compile
RUN javac App.java

# Final Stage
FROM openjdk:17-slim

WORKDIR /app

# Copy compiled class from builder
COPY --from=builder /app/App.class .

# Run
CMD ["java", "App"]
