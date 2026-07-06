# Cloud-Native Course Portal & Learning Management Service

A production-grade Django REST and template-driven Learning Management System (LMS) designed for enterprise-scale course delivery, learner enrollment management, and automated assessment grading. Built on Django's MTV architecture with a PostgreSQL-ready database layer, static asset pipeline, and containerized deployment primitives.

## Architecture Overview

### Django MTV / REST Layer
The application follows Django's Model-Template-View (MTV) pattern, extended with class-based generic views for RESTful resource exposure:

- **Models** (`onlinecourse/models.py`): Defines the core domain schema — `Instructor`, `Learner`, `Course`, `Lesson`, `Enrollment`, `Question`, `Choice`, and `Submission`. Relationships enforce referential integrity via cascade deletions and many-to-many through-tables.
- **Templates** (`onlinecourse/templates/`): Bootstrap-rendered HTML templates for course listings, detail views, exam forms, authentication flows, and result displays.
- **Views** (`onlinecourse/views.py`): Class-based `ListView`/`DetailView` for course browsing, function-based views for enrollment, exam submission, grading, login/logout, and registration workflows.

### Database Schema
| Entity | Description |
|---|---|
| `Instructor` | FK to `AUTH_USER_MODEL`, tracks employment status and learner count |
| `Learner` | FK to `AUTH_USER_MODEL`, occupation enum, social profile URL |
| `Course` | Core entity with image, description, publication date, M2M instructors and users via `Enrollment` |
| `Lesson` | FK to `Course`, ordered content blocks |
| `Enrollment` | Through-table linking Users to Courses with mode (audit/honor) and rating |
| `Question` | FK to `Course`, grade-weighted assessment items |
| `Choice` | FK to `Question`, boolean correctness flag |
| `Submission` | FK to `Enrollment`, M2M to `Choice` for exam attempt tracking |

### Static Asset Handling
Static files (CSS, JavaScript, admin assets) are served via Django's `STATICFILES_DIRS` and collected to `STATIC_ROOT` via `collectstatic`. Media uploads (course images) are routed through `MEDIA_ROOT`/`MEDIA_URL` with development-mode static serving via `+ static()` URL patterns.

## Setup Guide

### Prerequisites
- Python 3.11+
- pip (bundled with Python)
- Git

### Local Development Installation

```bash
# 1. Clone the repository
git clone https://github.com/amrbassal98-ux/cloud-native-course-portal.git
cd cloud-native-course-portal

# 2. Create and activate an isolated Python virtual environment
python3 -m venv python3-venv
source python3-venv/bin/activate

# 3. Install dependencies in the isolated environment
pip install --upgrade pip
pip install -r requirements.txt

# 4. Initialize environment configuration
cp .env.example .env
# Edit .env with your local SECRET_KEY and DEBUG settings

# 5. Apply database migrations
python manage.py migrate

# 6. Create an administrative superuser
python manage.py createsuperuser

# 7. Collect static assets
python manage.py collectstatic --noinput

# 8. Launch the development server
python manage.py runserver
```

### Production Deployment (Docker)

```bash
# Build the multi-stage container image
docker build -t cloud-native-course-portal .

# Run with environment file injection
docker run -d \
  --name course-portal \
  -p 8000:8000 \
  --env-file .env \
  cloud-native-course-portal
```

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `SECRET_KEY` | Yes | Django cryptographic secret key |
| `DEBUG` | No | Enable debug mode (default: `False`) |
| `ALLOWED_HOSTS` | Yes | Comma-separated allowed hostnames |
| `DATABASE_ENGINE` | No | Database backend (default: `sqlite3`) |
| `DATABASE_NAME` | No | Database name (default: `db.sqlite3`) |
| `DATABASE_USER` | No | Database username |
| `DATABASE_PASSWORD` | No | Database password |
| `DATABASE_HOST` | No | Database host |
| `DATABASE_PORT` | No | Database port |

## Project Structure

```
cloud-native-course-portal/
├── myproject/          # Django project configuration
│   ├── settings.py     # Centralized settings with env validation
│   ├── urls.py         # Root URL routing
│   ├── wsgi.py         # WSGI application entry point
│   └── asgi.py         # ASGI application entry point
├── onlinecourse/       # Core learning management app
│   ├── models.py       # Domain model definitions
│   ├── views.py        # Request handlers and business logic
│   ├── urls.py         # App-level URL routing
│   ├── admin.py        # Django admin configuration
│   ├── templates/      # Bootstrap-rendered HTML templates
│   └── migrations/     # Database migration files
├── static/             # Collected static assets
├── manage.py           # Django management CLI
├── requirements.txt    # Python dependency manifest
├── Dockerfile          # Multi-stage production container
├── .dockerignore       # Container build exclusions
├── .env.example        # Environment variable template
├── Procfile            # Cloud Foundry process definition
└── manifest.yml        # Cloud Foundry deployment manifest
```

## 🚀 Architectural Modernization Roadmap

1. **Decoupled PostgreSQL Engine Instance** — Migrate from the default SQLite3 backend to a managed PostgreSQL service (e.g., IBM Cloud Databases for PostgreSQL or AWS RDS). This enables connection pooling via `pgbouncer`, concurrent write support, and horizontal read replicas for high-availability production workloads. The `django-environ` integration already supports `DATABASE_URL` injection for zero-code database switching.

2. **Comprehensive Unit & Integration Test Coverage** — Implement a layered testing strategy using `pytest-django` with factory-based model fixtures (`factory_boy`), achieving >90% code coverage across models, views, and business logic. Add `pytest-cov` for coverage reporting, `responses` for external HTTP mocking, and CI-integrated test gates via GitHub Actions to enforce quality on every pull request.

3. **Redis Data Caching & Session Backend** — Deploy a Redis instance as a caching layer for frequently queried course catalog data and enrollment counts, reducing database read amplification. Migrate Django's session storage to `django-redis` for distributed session management across multiple application containers, enabling stateless horizontal scaling behind a load balancer.
