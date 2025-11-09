# Use Python 3.11 slim image for smaller size
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set Python path to include src directory
ENV PYTHONPATH="/app:/app/src"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and README first for better caching
COPY pyproject.toml README.md ./

# Install Python dependencies directly
RUN pip install --no-cache-dir google-generativeai>=0.3.0 jinja2>=3.1.0 typing-extensions>=4.0.0

# Copy application code
COPY src/ ./src/
COPY data/ ./data/
COPY *.py ./
COPY README.md ./

# Create necessary directories
RUN mkdir -p outputs logs

# Set default environment variables
ENV GEMINI_API_KEY="" \
    ENVIRONMENT=production \
    DEBUG=false

# Expose port (if needed for future web interface)
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "from src.ocs import OCS; ocs = OCS(); print('Health check OK')" || exit 1

# Default command
CMD ["python", "-m", "src.ocs.main"]