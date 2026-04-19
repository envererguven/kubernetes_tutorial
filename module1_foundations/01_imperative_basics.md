# Module 1: Kubernetes Foundations (Imperative)

This module covers the basic "imperative" commands used to interact with the cluster and run individual Pods, while introducing the shift toward declarative management.

## 0. The Kubernetes Philosophy: Imperative vs. Declarative
Understanding the difference between **telling K8s what to do** vs **telling K8s what the world should look like**.

| | Imperative | Declarative |
|---|---|---|
| **Analogy** | Following a recipe step-by-step. | Ordering from a menu (the chef handles how). |
| **Command** | `kubectl run`, `kubectl create`, `kubectl scale` | `kubectl apply -f file.yaml` |
| **Best For** | Ad-hoc testing, debugging, one-off fixes. | Production setups, CI/CD, Version Control. |
| **Pros** | Fast, no files needed. | History tracking, self-healing, reproducible. |

---

## 1. Cluster Verification
Commands to ensure your environment (Docker Desktop + WSL) is working correctly.

```bash
# Check kubectl client version
kubectl version --client

# Verify cluster connectivity
kubectl cluster-info

# List nodes (in Docker Desktop, you should see 'desktop-control-plane')
kubectl get nodes
```

## 2. Running your first Pod (Imperative)
Using `kubectl run` to quickly spin up a container.

```bash
# Run a simple Nginx pod
kubectl run hello-k8s --image=nginx

# List pods to see status (Pending -> ContainerCreating -> Running)
kubectl get pods

# Get detailed information about the pod (IP, events, etc.)
kubectl describe pod hello-k8s

# Export pod configuration to YAML (Great for creating templates)
kubectl get pod hello-k8s -o yaml > pod-template.yaml

# List pods with more detail (Node name, IP)
kubectl get pods -o wide
```

## 3. Modifying Running Resources (Imperative)
Sometimes you need to make quick changes WITHOUT a YAML file.

```bash
# Add a label to a pod
kubectl label pod hello-k8s tier=frontend

# Update a label (overwrite)
kubectl label pod hello-k8s tier=api --overwrite

# Edit a resource live (Opens your default terminal editor)
# kubectl edit pod hello-k8s
```

## 4. Running from a File (Declarative)
The professional way to manage Kubernetes is using manifest files.

```bash
# Create the pod from a file
kubectl apply -f basic-go-pod.yaml

# Check the Status
kubectl get pods --show-labels
```

## 5. Debugging & Networking
Accessing the pod and checking logs.

```bash
# View container logs
kubectl logs hello-k8s

# Port Forwarding: Access the pod from your Windows browser at http://localhost:8080
kubectl port-forward hello-k8s 8080:80

# Delete the pod (Manual cleanup)
kubectl delete pod hello-k8s
```
