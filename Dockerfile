FROM python:3.10.4-slim-bullseye

# Set environment to non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# Install only necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    ffmpeg \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip wheel \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose the port for Flask app
EXPOSE 8000

# Run both Flask and the Python script in parallel using bash
CMD bash -c "flask run --host=0.0.0.0 --port=8000 & python3 -m devgagan"
