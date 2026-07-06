# =============================================================================
# Multi-stage Dockerfile — Cloud-Native Course Portal
# =============================================================================
# Stage 1: Build dependencies in a full Python image
# Stage 2: Copy only runtime artifacts into a slim, non-root final image
# =============================================================================

# ---------------------------------------------------------------------------
# Stage 1 — Builder
# ---------------------------------------------------------------------------
FROM python:3.11-slim AS builder

WORKDIR /build

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------------------------------------------------------------------------
# Stage 2 — Production Runtime
# ---------------------------------------------------------------------------
FROM python:3.11-slim AS production

LABEL maintainer="amrbassal98-ux" \
      description="Cloud-Native Course Portal — Production Image" \
      version="1.0.0"

RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq5 && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local

RUN groupadd -r appgroup && useradd -r -g appgroup -d /app -s /sbin/nologin appuser

WORKDIR /app

COPY manage.py .
COPY myproject/ myproject/
COPY onlinecourse/ onlinecourse/

RUN mkdir -p /app/static /app/logs && \
    chown -R appuser:appgroup /app

USER appuser

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
