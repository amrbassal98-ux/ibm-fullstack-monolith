# Cloud-Native Full-Stack & DevOps Engineering Architecture

> A centralized monorepo containing production-grade full-stack applications, microservices infrastructure, and architectural milestones developed during IBM Professional Tracks.

---

## Overview

This repository serves as a comprehensive portfolio of cloud-native engineering competencies, demonstrating proficiency across the full development lifecycle—from foundational programming patterns to enterprise-grade deployment architectures. Each directory represents a distinct engineering discipline, organized to showcase progressive technical mastery.

---

## Core Showcase

### `01-capstone-showcase/tfjzl-final-cloud-app-with-database`

The primary capstone project demonstrating end-to-end cloud-native application development with database integration and production deployment capabilities.

| Component | Technology |
|-----------|------------|
| **Backend Runtime** | Python (Django/Flask) |
| **Database Integration** | SQLite / Cloud Database |
| **Cloud Deployment** | IBM Cloud Foundry (manifest.yml, Procfile) |
| **API Architecture** | RESTful endpoints with ORM models |
| **Static Assets** | Frontend templates and static files |

**Key Features:**
- Multi-model database schema with migrations
- Cloud-native deployment configuration
- Production-ready application structure
- Environment-based configuration management

---

## Technical Directory Matrix

| Directory | Classification | Description |
|-----------|---------------|-------------|
| `02-standalone-services` | **Production Component Modules** | Modular microservices and web applications including Django backends, Flask APIs, Express.js servers, and React frontend components |
| `03-cloud-and-devops-infra` | **Infrastructure Engineering** | Docker containerization, Kubernetes orchestration, horizontal autoscaling configurations, and API specification management |
| `04-foundational-architecture-labs` | **Foundational Architecture Milestones** | Core algorithmic and structural framework labs demonstrating fundamental programming patterns and architectural principles |

---

## Repository Structure

```
ibm-fullstack-monolith/
├── 01-capstone-showcase/           # Primary portfolio projects
│   └── tfjzl-final-cloud-app-with-database/
├── 02-standalone-services/         # Production component modules
│   ├── backend-api-modules/        # Django, Flask, Express backends
│   └── frontend-ui-components/     # React applications
├── 03-cloud-and-devops-infra/      # Infrastructure engineering
│   ├── autoscaler/                 # Kubernetes autoscaling
│   ├── containers-project/         # Docker configurations
│   ├── k8-scaling-and-secrets-mgmt/
│   ├── kubernetes/                 # K8s orchestration
│   └── swagger/                    # API specifications
└── 04-foundational-architecture-labs/ # Core framework labs
    ├── CC201/                      # Cloud computing labs
    ├── lab3_template/              # Django project template
    ├── mymath/                     # Mathematical functions
    ├── online-plant-shopping/      # Full-stack e-commerce
    ├── practice/                   # Flask practice servers
    └── practice_project/           # Sentiment analysis
```

---

## Engineering Disciplines Demonstrated

### Backend Development
- **Python Frameworks**: Django ORM, Flask routing, Express.js APIs
- **Database Design**: Schema migrations, model relationships, data validation
- **API Architecture**: RESTful endpoints, middleware integration

### Frontend Engineering
- **React Ecosystem**: Component architecture, state management, hooks
- **Build Systems**: Vite, Webpack configurations
- **Responsive Design**: Component-based UI patterns

### Cloud & DevOps
- **Containerization**: Dockerfile best practices, multi-stage builds
- **Orchestration**: Kubernetes deployments, services, secrets management
- **Auto-scaling**: Horizontal pod autoscaler configurations
- **CI/CD**: Cloud Foundry deployment manifests

### Infrastructure as Code
- **Terraform**: Cloud resource provisioning
- **Kubernetes YAML**: Deployment, Service, ConfigMap definitions
- **Docker Compose**: Local development environments

---

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- Docker Desktop
- Kubernetes cluster (minikube or cloud provider)
- IBM Cloud CLI (for Cloud Foundry projects)

### Local Development
```bash
# Clone the repository
git clone <repository-url>
cd ibm-fullstack-monolith

# Navigate to specific project
cd 02-standalone-services/backend-api-modules/django_project

# Install Python dependencies
pip install -r requirements.txt

# Run Django development server
python manage.py runserver
```

### Docker Deployment
```bash
# Build container image
docker build -t my-app .

# Run container
docker run -p 8000:8000 my-app
```

### Kubernetes Deployment
```bash
# Apply Kubernetes configurations
kubectl apply -f k8-scaling-and-secrets-mgmt/

# Check deployment status
kubectl get pods
kubectl get services
```

---

## Portfolio Highlights

| Project | Complexity | Technologies |
|---------|------------|--------------|
| tfjzl-final-cloud-app-with-database | High | Python, Django, Cloud Foundry |
| online-plant-shopping | High | Node.js, React, Express, MongoDB |
| autoscaler | Medium | Kubernetes, Go, YAML |
| containers-project | Medium | Docker, Node.js |
| final_project | Medium | Python, Flask, Watson AI |

---

## Author

**Amr Bassal** - Cloud-Native Full-Stack & DevOps Engineer

---

## License

This repository is maintained as a professional portfolio demonstrating engineering competencies developed through IBM Professional Certificate programs.
