# Kubernetes Basics - Official Training Reference

This file documents the core commands and concepts discovered during the training session.

## Environment & Context
Run these to verify your connection to the cluster.

| Command | Description |
|---------|-------------|
| `kubectl cluster-info` | Check if the control plane is reachable. |
| `kubectl get nodes` | List all nodes in the cluster. |
| `kubectl version --client` | Check your local `kubectl` version. |

## Module 1: Pods & Foundations

### The Atomic Unit: The Pod
A Pod is the smallest deployable object in Kubernetes. It represents a single instance of a running process in your cluster.

| Action | Command |
|--------|---------|
| Run a simple Pod | `kubectl run <name> --image=<image>` |
| List Pods | `kubectl get pods` |
| View Details | `kubectl describe pod <name>` |
| View Logs | `kubectl logs <name>` |
| Delete Pod | `kubectl delete pod <name>` |

## Module 2: Deployments & Scaling

### Declarative Configuration
Instead of `kubectl run`, we use YAML files to describe the *desired state*. Kubernetes then works to make the *actual state* match your description.

| Action | Command |
|--------|---------|
| Apply a manifest | `kubectl apply -f <filename>.yaml` |
| Get Deployments | `kubectl get deployments` |
| Scale Deployment | `kubectl scale deployment <name> --replicas=<num>` |
| Rollout Status | `kubectl rollout status deployment <name>` |
| Delete Deployment| `kubectl delete -f <filename>.yaml` |

If a Pod managed by a Deployment is deleted or crashes, the Deployment controller automatically detects the mismatch and recreates it.

## Module 3: Networking & Services

### Why Services?
Pods are ephemeral (they die and get replaced). Their IP addresses change. A **Service** provides a stable IP address and DNS name that stays the same for the lifetime of the application.

| Service Type | Visibility | Use Case |
|--------------|------------|----------|
| `ClusterIP` | Inside Cluster Only | Internal databases, microservices. |
| `NodePort` | Outside Cluster | Direct access via host IP + high port (30000+). |
| `LoadBalancer`| Outside Cluster | Standard way to expose apps (Docker Desktop creates a tunnel). |

| Action | Command |
|--------|---------|
| Create Service | `kubectl apply -f <service>.yaml` |
| Get Services | `kubectl get svc` |
| Get Endpoints | `kubectl get endpoints <service>` |
| Test Service (Internal)| `kubectl port-forward service/<name> 8080:80` |
