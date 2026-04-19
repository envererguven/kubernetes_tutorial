# Module 9: Advanced Tools (Helm & Dashboard)

This module introduces **Helm**, the package manager for Kubernetes, and the official **Kubernetes Dashboard**.

## 1. What is Helm?
Helm is like `apt` or `npm` but for Kubernetes. It allows you to:
- **Reuse**: Use "Charts" (pre-made manifests) created by the community.
- **Configure**: Use `values.yaml` to change settings without editing complex templates.
- **Rollback**: Easily undo a deployment with `helm rollback`.

## 2. Helm Cheat Sheet
```bash
# Add a repository (App Store)
helm repo add <name> <url>

# Search for apps
helm search repo <keyword>

# Install an app
helm install <release-name> <chart-name>

# List installed apps
helm list
```

## 3. The Kubernetes Dashboard
The Dashboard provides a web-based UI to manage your cluster. 

### Why use a Dashboard?
- **Visualization**: See your pods, services, and nodes in a graph.
- **Editing**: Change scaling or config on the fly via the browser.
- **Logs/Exec**: Access logs and shells without typing long commands.

---
**Next Step**: Once installed, we will generate a **Bearer Token** to log in securely.
