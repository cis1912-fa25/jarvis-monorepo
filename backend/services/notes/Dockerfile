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
COPY services/notes/pyproject.toml ./
COPY services/notes/uv.lock ./

# Install dependencies
RUN uv sync --no-cache --link-mode=copy

# Copy service code
COPY services/notes/. .

CMD ["uv", "run", "fastapi", "dev", "main.py", "--port", "8001", "--host", "0.0.0.0"]
