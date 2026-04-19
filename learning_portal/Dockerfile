FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install flask flask-cors markdown

# Copy backend source
COPY backend/app.py .

# Copy frontend source into static folder
COPY frontend/index.html static/index.html

# Map the workspace volume
VOLUME /workspace

EXPOSE 5000

CMD ["python", "app.py"]
