# Module 7: Observability & Management

This module focuses on how to monitor, debug, and manage running applications in the cluster.

## 1. Logs (Viewing Stdout)
Kubernetes captures everything your application prints to the console.

```bash
# View current logs
kubectl logs -l app=flask-app

# Stream logs (Real-time)
kubectl logs -l app=flask-app -f --tail=10

# Multi-container logs (If your pod has more than one container)
kubectl logs <pod-name> -c <container-name>
```

---

## 2. Health Checks: Probes (Declarative)
Kubernetes needs to know if your app is alive and ready to handle traffic.

- **Liveness Probe**: Restarts the container if it fails (e.g., deadlock).
- **Readiness Probe**: Stops sending traffic to the pod if it's "busy" (e.g., loading cache).
- **Startup Probe**: Protects slow-starting apps.

```yaml
# Example from java-worker-deployment.yaml
livenessProbe:
  exec:
    command: ["cat", "/app/WorkerApp.class"]
  initialDelaySeconds: 15
  periodSeconds: 20
```

---

## 3. Exec (The "SSH" of K8s)
Sometimes you need to get inside a container to check the filesystem or network.

```bash
# Open an interactive shell inside a pod
# Note: Use one of your pod names from 'kubectl get pods'
kubectl exec -it <pod-name> -- sh

# Inside the pod, check environment variables:
printenv | grep APP
exit
```

## 3. Top (Resource Monitoring)
Note: This requires the Metrics Server. In Docker Desktop, this might not be enabled by default.

```bash
# View CPU and Memory usage for nodes
kubectl top nodes

# View CPU and Memory usage for pods
kubectl top pods
```

---
**Lab Exercise**:
1. Stream logs: `kubectl logs -l app=flask-app -f`.
2. Refresh your browser at `http://localhost`.
3. Watch the logs update in your terminal as Flask handles the requests!
