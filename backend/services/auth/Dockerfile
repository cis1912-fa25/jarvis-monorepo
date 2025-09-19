FROM python:3.10-slim

WORKDIR /service/app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY services/auth/. .

COPY utilities /utilities

RUN uv sync --no-cache --link-mode=copy

CMD ["uv", "run", "fastapi", "dev", "main.py", "--port", "8000", "--host", "0.0.0.0"]