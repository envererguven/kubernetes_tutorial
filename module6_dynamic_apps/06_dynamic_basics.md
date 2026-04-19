# Module 6: Dynamic Apps & Configuration

This module covers building custom images and managing configuration via ConfigMaps and Secrets.

## 1. Local Build Loop (Docker Desktop)
You don't need a registry. Build locally and use `imagePullPolicy: Never`.

```bash
# Build the image
docker build -t my-flask-app:v1 .

# Check if image exists
docker images | grep my-flask-app
```

## 2. ConfigMaps vs Secrets
- **ConfigMap**: For non-sensitive settings (URLs, greetings, feature flags).
- **Secrets**: For sensitive data (Passwords, API keys, SSH keys). Store as Base64.

```bash
# How to encode a secret in terminal:
echo -n "my-password" | base64
```

# How to encode a secret in terminal:
echo -n "my-password" | base64
```

### Imperative Creation (Fastest)
Sometimes you don't want to write a YAML file just for a simple key.
```bash
# Create a Secret from literal values
kubectl create secret generic mysql-pass --from-literal=password='admin123'

# Create a ConfigMap from a file
kubectl create configmap app-theme --from-file=config.txt

# List them
kubectl get secrets,cm
```

---

## 3. Real Example: Java Config Reader
This example shows a Java app reading from the `java-config` ConfigMap.

### Step 1: Apply Config
```bash
kubectl apply -f configmap-java.yaml
```

### Step 2: Deploy App
(This would use a deployment linking the ConfigMap to environment variables or volume mounts).
```bash
# Example snippet of the deployment:
# env:
#   - name: DB_HOST
#     valueFrom:
#       configMapKeyRef:
#         name: java-config
#         key: db-host
```

## 4. Troubleshooting: ErrImageNeverPull
This is a frequent issue in Docker Desktop where the Kubernetes engine cannot find the locally built image.

### The "Double Cache" Problem
Modern Docker Desktop has two image stores: **Moby** (standard Docker) and **containerd** (Kubernetes). Sometimes they don't sync properly.

### Option A: The Settings Fix (Permanent)
1. Go to **Docker Desktop Settings**.
2. Uncheck **"Use containerd for pulling and storing images"**.
3. Apply & Restart. This forces both Docker and K8s to use the same image store.

### Option B: The Volume Mount Workaround
If you cannot rebuild images, you can use a base image (like `python:3.9-slim`) and mount your application folder into the container using **Volumes** (as seen in Module 5).

### Common Mistake: imagePullPolicy
If your image is only local, you MUST use:
- `imagePullPolicy: IfNotPresent` (Tries local first)
- *Avoid* `imagePullPolicy: Always` (Will always fail for local-only images).
