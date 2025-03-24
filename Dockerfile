
# Build stage
FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y python3-pip

COPY ./pyproject.toml ./pyproject.toml
COPY ./uv.lock ./uv.lock

# Install dependencies
RUN pip install uv
RUN uv venv .venv --python=3.11
RUN . .venv/bin/activate
RUN uv pip install -e .

COPY ./bookroom_agents ./bookroom_agents
COPY ./docker/entrypoint.sh /entrypoint.sh

# Expose the default port
EXPOSE 15230

# Set entrypoint
ENTRYPOINT [ "/bin/bash","/entrypoint.sh" ]