# Build Stage
FROM golang:1.21-alpine AS builder

WORKDIR /app

# Copy source code
COPY main.go .

# Build the binary
RUN go build -o go-cli main.go

# Final Stage
FROM alpine:latest

WORKDIR /root/

# Copy the binary from the builder stage
COPY --from=builder /app/go-cli .

# Run the binary
ENTRYPOINT ["./go-cli"]
