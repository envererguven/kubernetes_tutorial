# Module 4: Networking Deep Dive (Internal DNS)

This module explores how Pods communicate with each other using the built-in Kubernetes DNS.

## 1. Service Discovery
You never need to hardcode Pod IPs. Instead, you use the Service Name.
- Service Name: `nginx-service`
- Full DNS Name: `nginx-service.default.svc.cluster.local`

---

## 2. Advanced DNS Networking (Verification)
We use a dedicated "dnsutils" pod for deep network exploration.

```bash
# Run a pod with nslookup and dig
kubectl run dns-tool --image=tutum/dnsutils -it --rm -- sh

# Inside the pod:
# nslookup nginx-service
# dig nginx-service.default.svc.cluster.local
```

### Key Concept: CoreDNS
Every request to a service name is intercepted by **CoreDNS** (a system pod in the `kube-system` namespace) which returns the **ClusterIP** of the service.

---

## 3. Ingress: Advanced HTTP Routing (Declarative)
While Service types like NodePort and LoadBalancer work at Layer 4 (IP/TCP), **Ingress** works at Layer 7 (HTTP/HTTPS). It allows you to route traffic based on hostnames or URL paths.

```bash
# Apply the Ingress manifest
kubectl apply -f ingress-example.yaml

# List Ingresses
kubectl get ingress
```

**Benefits of Ingress**:
- **Host-based routing**: `api.example.com` -> `api-service`, `blog.example.com` -> `blog-service`.
- **Path-based routing**: `/app1` -> `service1`, `/app2` -> `service2`.
- **SSL/TLS Termination**: Manage certificates in one place.

---

## 4. Why this matters
In a real application (e.g., Python app + Redis database):
1. You create a Service for Redis named `redis-service`.
2. Your Python code just connects to `host="redis-service"`.
3. Kubernetes handles all the IP changes and load balancing automatically.
