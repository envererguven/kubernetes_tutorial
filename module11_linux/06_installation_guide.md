# Module 11.6: Advanced Ubuntu Setup: Networking & Orchestration

This guide provides step-by-step instructions for installing and managing powerful networking and orchestration tools on Ubuntu.

---

## 🛰️ 1. tcpdump (Packet Analysis)
`tcpdump` is a powerful command-line packet analyzer.

### Installation:
```bash
sudo apt update
sudo apt install tcpdump -y
```

### Running Examples:
- `sudo tcpdump -i eth0`: Capture packets on the `eth0` interface.
- `sudo tcpdump -i any port 80`: Capture all HTTP traffic across all interfaces.
- `sudo tcpdump -c 10 -n`: Capture only 10 packets and don't resolve hostnames (faster).
- `sudo tcpdump -i eth0 -w capture.pcap`: Save packets to a file for later analysis in Wireshark.

---

## 🧱 2. iptables (Traditional Firewall)
While `ufw` is easier, `iptables` is the standard low-level firewall tool.

### Installation:
```bash
sudo apt install iptables iptables-persistent -y
```

### Commands & Examples:
- **List Rules**: `sudo iptables -L -n -v` (Detailed list with line numbers).
- **Block an IP**: `sudo iptables -A INPUT -s 192.168.1.10 -j DROP`
- **Allow a Port**: `sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT`
- **Flush (Disable) All Rules**: `sudo iptables -F`
- **Save Rules (Persistent)**: `sudo netfilter-persistent save`

---

## 🐳 3. Docker Engine
The most popular container platform.

### Installation (Official Repo):
```bash
# 1. Add Docker's official GPG key
sudo apt update
sudo apt install ca-certificates curl gnupg -y
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# 2. Add the repository to Apt sources
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 3. Install Docker
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
```

### Running Examples:
- `sudo docker run hello-world`: Verify installation.
- `sudo docker ps -a`: View all containers.
- `sudo systemctl status docker`: Check if the service is running.

---

## ☸️ 4. Mini-Kubernetes (Minikube / MicroK8s)
For local development, `minikube` is the standard.

### Installation (Minikube):
```bash
# 1. Download the binary
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# 2. Start the cluster
minikube start --driver=docker
```

### Core Commands:
- `minikube status`: Check cluster health.
- `kubectl get nodes`: Verify the single-node setup.
- `minikube dashboard`: Open the web UI.
- `minikube stop`: Shutdown the local cluster.
