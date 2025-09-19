FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set work directory
WORKDIR /service/app

# Copy shared library
COPY utilities /utilities

# Copy dependency files first for better Docker layer caching
COPY services/auth/pyproject.toml ./
COPY services/auth/uv.lock ./

# Install dependencies
RUN uv sync --no-cache --link-mode=copy

# Copy service code
COPY services/auth/. .

CMD ["uv", "run", "fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]
