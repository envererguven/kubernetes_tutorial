# Module 5: Storage & Volumes

This module demonstrates how to preserve data beyond the lifecycle of a single container.

## 1. Volume Types
- **emptyDir**: A scratch volume that is deleted when the Pod is deleted. Used for sharing data between two containers in the same Pod.
- **hostPath**: Mounts a file or directory from the host node (your PC) into the Pod.
- **PersistentVolume (PV) / PVC**: The production way. Abstracted storage requested from the cluster.

## 2. Mounting a hostPath (Docker Desktop/WSL)
On Docker Desktop, the host machine is mapped inside the K8s VM. We use the path translation to map our project folder.

```yaml
volumes:
  - name: web-storage
    hostPath:
      path: /run/desktop/mnt/host/c/PROJECTS/docker_kubernetes/module5_storage_volumes/html
```

## 3. The Professional Way: PV & PVC (Declarative)
In real clusters, developers don't use `hostPath` directly. They request storage via a **PersistentVolumeClaim (PVC)**.

### Step 1: Create the PV and PVC
The Admin creates the PV (The actual disk) and the Developer creates the PVC (The request for disk).
```bash
# Apply the storage manifests
kubectl apply -f pvc-hostpath.yaml

# Check the status (Should be 'Bound')
kubectl get pv,pvc
```

### Step 2: Deploy the Persistent Go App
This app increments a counter stored on the PV. If you delete and recreate the pod, the counter will **NOT** reset.

```bash
# Apply the deployment using the PVC
kubectl apply -f go-persistent-deployment.yaml

# Watch the logs to see the counter incrementing
kubectl logs -l app=go-persistent -f
```

---

## 4. Useful Commands (Imperative vs. Declarative)

| Task | Imperative | Declarative |
|---|---|---|
| Create Volume | N/A (Requires YAML) | `kubectl apply -f pv.yaml` |
| View Usage | `kubectl describe pvc <name>` | `kubectl get pvc` |
| Delete Storage | `kubectl delete pvc <name>` | `kubectl delete -f pvc.yaml` |
