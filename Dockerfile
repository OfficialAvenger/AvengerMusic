FROM nikolaik/python-nodejs:python3.10-nodejs19

# Install FFmpeg (required for PyTgCalls)
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Show versions (for debugging)
RUN node -v && npm -v && python3 -V && pip3 -V

# Set working directory
WORKDIR /app

# Copy files to container
COPY . .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Set default command to run your bot
CMD ["bash", "start"]
