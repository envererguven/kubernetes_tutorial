# Module 8 Recap: Centralized Logging (ELK)

We attempted to deploy the **ELK Stack** (Elasticsearch, Logstash/Filebeat, Kibana) in a local Kubernetes environment. Here is a summary of the architecture and the challenges faced.

## 1. The Architecture
In a professional production environment, logs follow this path:
- **Producer**: Your application (e.g., Python Flask) writes to `stdout`.
- **Shipper (Filebeat)**: A **DaemonSet** that runs on every node, reads logs from `/var/log/containers/`, and sends them to a buffer.
- **Buffer/Index (Elasticsearch)**: The high-performance search engine and database that stores and indexes the logs.
- **Visualizer (Kibana)**: The dashboard that allows developers to search, filter, and alert on logs.

## 2. Why it failed locally
- **Resource Intensity**: Elasticsearch is a JVM-based application. Even with optimized heap sizing (`-Xms512m -Xmx512m`), it is extremely heavy for a local Docker Desktop cluster.
- **Image Size & Registry Timeouts**: The full ELK images exceed 1GB uncompressed. In some network environments, the Kubernetes `kubelet` times out during the pull, resulting in `ErrImagePull` or `ImagePullBackOff`.

## 3. Production Best Practices
- **Managed Services**: Companies often use managed services like **Elastic Cloud**, **Datadog**, or **Splunk** to avoid managing the ELK infrastructure themselves.
- **Loki Stack**: A modern, lightweight alternative by Grafana Labs that is significantly more resource-efficient for Kubernetes.
- **Helm**: Always use Helm charts to deploy ELK in production to manage the complex configuration and resource requests/limits.

---
**Status**: This module has been deferred. We are moving to **Module 9** to learn **Helm**, which is the tool you *would* use to install ELK (or Loki) in a professional setting.
