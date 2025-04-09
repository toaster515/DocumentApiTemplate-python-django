# File Storage API Template (Django)

A containerized Django API template for uploading files to multiple cloud storage providers (AWS S3, Azure Blob), while recording metadata in Postgres. Supports background processing via Celery + Redis.

---

## Features

- Clean, modular architecture (Domain → Application → Infrastructure)
- S3 and Azure Blob Storage integrations
- Background metadata writing with Celery
- Postgres for metadata persistence
- OpenAPI docs via `drf-spectacular` (Swagger UI)
- Fully Dockerized for local dev
- Pluggable architecture for adding new storage providers
- Auto migration + healthcheck endpoint

---

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/your-org/file-storage-api-python.git
cd file-storage-api-python/docker
```
### 2. Start
```bash
docker-compose up --build
```

Visit:
- API Docs: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- Healthcheck: http://localhost:8000/api/health/

### 3. Config
See `.env.example` for example local setup


---
## Architecture
```bash
docker/
├── docker-compose.yml 
src/
├── api/                # Django project config
├── application/        # Business logic (use cases)
├── infrastructure/
│   ├── documents/      # Models, serializers, views
│   └── storage/        # S3 and Azure implementations
├── .env
├── Dockerfile
├── requirements.txt
```
Uses interface-based abstraction for storage providers to keep logic clean and modular.
