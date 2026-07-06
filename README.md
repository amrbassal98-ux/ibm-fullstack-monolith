# IBM Full-Stack & DevOps Engineering Monolith

Cloud-Native Full-Stack & DevOps Engineering Architecture - IBM Professional Certificate Portfolio

---

## Core Showcase: Car Dealership Review System

The flagship full-stack capstone application demonstrating end-to-end cloud-native development with container orchestration, microservices decomposition, and CI/CD automation.

### Architecture Overview

| Layer | Technology | Port | Isolation |
|:---|:---|:---|:---|
| **Frontend / Proxy** | Python 3.12 (Django 3.2 + Gunicorn) | 8000 | Kubernetes Pod |
| **React SPA** | React 18.2 / React Router 6.19 | 3000 | Static build served by Django |
| **Backend API** | Node.js 18 / Express 4.18 | 3030 | Docker Compose |
| **Database** | MongoDB (Docker) | 27017 | Named volume (`mongo_data`) |
| **Sentiment Analyzer** | Python 3.9 / Flask / NLTK VADER | 5050 | Docker Compose |
| **Orchestration** | Minikube v1.38.1 / Kubernetes v1.35.1 | - | Docker driver, single-node |

### Engine Layer Split

- **JavaScript Engine** (`server/database/`) - Express REST API for MongoDB CRUD operations on dealership and review records. Models: `dealership.js`, `review.js`, `inventory.js`. Seed data via `data/*.json`.
- **Python Engine** (`server/djangoproj/`, `server/djangoapp/`) - Django application serving React SPA, proxying REST requests to the Node.js backend, and managing user authentication.
- **Background Review Router** (`server/djangoapp/microservices/`) - Flask-based NLP sentiment scoring microservice using NLTK VADER for compound-score classification of user review text.

### CI/CD Linting Actions

GitHub Actions workflow (`.github/workflows/main.yml`) runs on push/PR to `main` and `master`:
- **Python Linter** - `flake8` on all `.py` files
- **JavaScript Linter** - `JSHint` on all `.js` files under `server/database/`

---

## Technical Directory Matrix

| Directory | Classification | Description |
|:---|:---|:---|
| `01-capstone-showcase/car-dealership-review-system/` | **Showcase** | Full-stack capstone - Django/React/Node.js/MongoDB with Kubernetes orchestration and CI/CD |
| `02-standalone-services/backend-api-modules/tfjzl-final-cloud-app-with-database/` | **Production Component Module** | Django cloud application with database integration (IBM Skills Network course final) |
| `02-standalone-services/backend-api-modules/django_project/` | Production Component Module | Customer360 Django CRUD application |
| `02-standalone-services/backend-api-modules/final_project/` | Production Component Module | Final project Django backend |
| `02-standalone-services/backend-api-modules/hjbsk-build_deploy_app_flask/` | Production Component Module | Flask build & deploy application |
| `02-standalone-services/backend-api-modules/my_django_project/` | Production Component Module | Custom Django project |
| `02-standalone-services/backend-api-modules/servers/` | Production Component Module | Standalone server configurations |
| `02-standalone-services/frontend-ui-components/react/` | Production Component Module | React frontend component library |
| `03-cloud-and-devops-infra/autoscaler/` | Cloud Infrastructure | Kubernetes autoscaler (cluster, vertical pod, addon-resizer) |
| `03-cloud-and-devops-infra/kubernetes/` | Cloud Infrastructure | Kubernetes CC201 lab configurations |
| `03-cloud-and-devops-infra/containers-project/` | Cloud Infrastructure | Container deployment manifests |
| `03-cloud-and-devops-infra/k8-scaling-and-secrets-mgmt/` | Cloud Infrastructure | K8s scaling and secrets management |
| `03-cloud-and-devops-infra/swagger/` | Cloud Infrastructure | Microservices API specifications |
| `04-foundational-architecture-labs/` | Foundational Labs | Python, Flask, React, and Sentiment Analysis practice labs |

---

## Repository Purpose

Consolidates all IBM Full-Stack Cloud Developer Professional Certificate coursework into a single monorepo for portfolio presentation. Each directory maps to a discrete course module, lab exercise, or capstone deliverable.
