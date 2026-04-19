# 🚀 Kubernetes Masterclass: Enterprise Training & Portal Hub

Welcome to the ultimate Kubernetes and Docker learning repository. This project contains a comprehensive curriculum from foundational containerization to multi-service enterprise architectures, all accessible via a dynamic **Learning Portal**.

---

## 🏛️ Project Architecture
- **Modules 0-9**: Core Kubernetes concepts (Docker, Networking, Deployments, Storage, Observability).
- **Module 10 (Enterprise)**: Five real-world projects covering **Banking, Telco, Fintech, Assurance, and Finance**.
- **The Learning Portal**: A professional-grade Python/Flask application that serves all internal markdown guides and source code as a dynamic web dashboard.

---

## 🌐 Quick Start: The Learning Portal

The easiest way to explore this repository is through the **Learning Portal**.

### 1. Build and Run (Standard Docker)
Run these commands in your WSL terminal to launch the Hub:

```bash
cd learning_portal
docker build -t learning-portal:v3 .
docker run -d --name learning-portal -p 8888:5000 -v "/mnt/c/PROJECTS/docker_kubernetes:/workspace" learning-portal:v3
```

### 2. Access the Portal
Visit: **[http://localhost:8888](http://localhost:8888)**

---

## 🏢 Module 10: Enterprise Projects
Each project demonstrates a full polyglot stack: **Proxy (Nginx) → Frontend → Backend → Database → Queue**.

- **[P1: Martian Bank](file:///c:/PROJECTS/docker_kubernetes/module10_projects/p1_banking)** (Java + Go + Postgres + Redis)
- **[P2: Telco Billing](file:///c:/PROJECTS/docker_kubernetes/module10_projects/p2_telco)** (Python + Go + MongoDB + Redis)
- **[P3: Fintech Wallet](file:///c:/PROJECTS/docker_kubernetes/module10_projects/p3_fintech)** (Node.js + Go + Postgres + Redis)
- **[P4: Assurance Claims](file:///c:/PROJECTS/docker_kubernetes/module10_projects/p4_assurance)** (Java + PHP + Postgres + Redis)
- **[P5: Portfolio Risk](file:///c:/PROJECTS/docker_kubernetes/module10_projects/p5_portfolio)** (Python + Go + TimescaleDB + Redis)

---

## ☸️ Kubernetes Deployment
If you prefer running the Portal inside your cluster:

```bash
cd learning_portal
kubectl apply -f k8s/portal-deployment.yaml
kubectl port-forward svc/learning-portal-svc 8888:5000
```
*Note: Ensure the `hostPath` in the manifest matches your local environment (see Troubleshooting section).*

---

## 🛠️ Troubleshooting
- **Empty Sidebar?** Ensure "File Sharing" is enabled in Docker Desktop for `C:\PROJECTS`.
- **404 Not Found?** Ensure you are using the `v3` image tag and have cleared old pods with `kubectl delete pod -l app=learning-portal`.
- **API Connection Failed?** Check the logs with `docker logs learning-portal`.

---

## 👤 Author
**Enver Erguven**  
GitHub: [https://github.com/envererguven](https://github.com/envererguven)  
Repo: [https://github.com/envererguven/kubernetes_tutorial](https://github.com/envererguven/kubernetes_tutorial)
