# Module 8: Centralized Logging (ELK)

This module moves from basic `kubectl logs` to a professional log aggregation system.

## 1. Why Centralized Logging?
In a cluster with 50+ pods, you cannot manually check logs for each one. 
- **Aggregation**: Bring all logs together in one database.
- **Persistence**: Logs stay even after pods are deleted.
- **Search**: Powerfully query and visualize patterns.

## 2. The Components (EFK Stack)
- **Elasticsearch**: The database and search engine for logs.
- **Filebeat**: The lightweight shipper that reads logs from every node.
- **Kibana**: The web-based visualization dashboard.

## 3. Step 8.1: Elasticsearch Setup
We use a single-node configuration with strict memory limits for local training.

```bash
# Apply the database
kubectl apply -f elasticsearch.yaml

# Check cluster health (Internal)
kubectl exec -it <elasticsearch-pod-name> -- curl http://localhost:9200/_cluster/health?pretty
```
