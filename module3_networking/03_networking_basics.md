# Module 3: Networking & Services (Load Balancing)

This module explains how to provide a stable network interface for a group of dynamic Pods.

## 1. The Core Problem
Pods IPs are not stable. They change whenever a pod is recreated. 
A **Service** acts as a fixed entry point (Stable IP + DNS name) that stays the same for the lifetime of the application.

## 2. Service Selection
A Service uses a **Selector** to find which pods to send traffic to. In our example, it looks for any pod with the label `app: nginx`.

```yaml
spec:
  selector:
    app: nginx  # Must match the labels in your Deployment.yaml
```

## 3. Service Types (Exposure Levels)

| Type | Access Scope | Best For... |
|---|---|---|
| **ClusterIP** | Internal | DBs, internal APIs. |
| **NodePort** | External (via Node IP) | Simple testing, direct access. |
| **LoadBalancer** | External (Global) | Production apps, Public APIs. |

---

## 4. NodePort: Exposing on Every Node
A NodePort service builds on ClusterIP by opening a specific port on every Node in the cluster. This allows external traffic to reach the service via `<NodeIP>:<NodePort>`.

```bash
# Imperative creation of a NodePort service
kubectl expose deployment nginx-deployment --type=NodePort --name=nginx-nodeport --port=80

# Find the assigned NodePort (usually 30000-32767)
kubectl get svc nginx-nodeport
```

**Verification (Curl)**:
```bash
# In Docker Desktop, you can access via localhost:<NodePort>
curl -v http://localhost:<NODE_PORT>
```

---

## 5. LoadBalancer: The "Gold Standard"
In a cloud environment (AWS, GCP, Azure), a LoadBalancer service automatically provisions a Cloud Load Balancer. In Docker Desktop, it maps to `localhost`.

```bash
# Apply the LoadBalancer manifest
kubectl apply -f nginx-lb.yaml

# Check for the External-IP
kubectl get svc nginx-lb --watch
```

**Testing External Access**:
```bash
curl -v http://localhost:80
```

---

## 6. Summary of Port Exposure Mapping
Understanding the "Port Chain" is critical:

1. **Port (Service)**: The port the service listens on.
2. **TargetPort (Pod)**: The port the application inside the pod is listening on.
3. **NodePort (External)**: The high-range port on the Node that routes to the service.

---

## 7. Exposing Multiple Ports
Sometimes an app needs multiple ports (e.g., HTTP on 80 and HTTPS on 443). You can define them in a single service using **Named Ports**.

```bash
# Apply the multi-port service
kubectl apply -f multi-port-service.yaml

# Check the service to see both ports mapped
kubectl describe svc multi-port-svc
```
