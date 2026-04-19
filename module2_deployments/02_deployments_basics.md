# Module 2: Deployments & Scaling (Declarative)

This module shifts from manual Pod management to the "Desired State" architecture using Deployments.

## 1. Creating a Deployment
Instead of `kubectl run`, we use a YAML file to define the management rules.

```bash
# Apply the deployment manifest
kubectl apply -f nginx-deployment.yaml

# List all pods with their labels
kubectl get pods --show-labels
```

# 2. Scaling (The "Fleet" Concept)
Making your application bigger or smaller takes a single command (Imperative) or a automatic rule (Declarative).

### Imperative Scaling (Manual)
```bash
# Scaling up to 10 replicas immediately
kubectl scale deployment nginx-deployment --replicas=10
```

### Declarative Scaling (Automatic)
Using a **Horizontal Pod Autoscaler (HPA)**, Kubernetes can automatically scale your deployment based on actual CPU/Memory usage.

```bash
# Apply the HPA manifest
kubectl apply -f hpa-example.yaml

# Check HPA status
kubectl get hpa
```

## 3. Self-Healing
If you delete a pod managed by this deployment, Kubernetes will automatically create a new one to maintain the replica count.

```bash
# Delete a specific pod
kubectl delete pod <pod-name>

# Immediately check pods to see a new 'ContainerCreating' pod
kubectl get pods
```

---

## 4. Beyond Web Apps: Workers & CLI Tools
Kubernetes isn't just for Nginx. It's used for background processing and CLI tasks.

### Running a Background Worker (Imperative)
Using the Go-CLI image we built in Module 0.
```bash
# Run a one-off job to test our CLI tool
kubectl run go-worker --image=my-go-cli:v1 --restart=OnFailure

# View the output!
kubectl logs go-worker
```

### Scheduled Tasks (CronJobs)
Use CronJobs for tasks that need to run at specific intervals (e.g., database backups, log cleanup).

```bash
# Apply the cronjob manifest
kubectl apply -f cronjob-example.yaml

# List cronjobs
kubectl get cronjobs

# View the status of the jobs spawned by the cronjob
kubectl get jobs
```

---

## 5. Verification with Curl
Even for internal apps, we often use `curl` to verify internal connectivity.

```bash
# Create a temporary 'tester' pod to curl another pod internally
kubectl run tester --image=curlimages/curl -it --rm -- /bin/sh

# Inside the tester pod, try to reach the nginx-deployment service
# curl http://nginx-service:80
```
