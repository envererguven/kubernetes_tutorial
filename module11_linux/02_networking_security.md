# Module 11.2: Networking & Security

## 🌐 1. Linux Networking
Networking is the heart of any server.

### Interface & IP Management:
- `ip addr show`: View all network interfaces and IP addresses (Modern `ifconfig`).
- `ip route show`: View the default gateway and routing table.
- `ping -c 4 google.com`: Test connectivity.
- `curl -I http://google.com`: Inspect HTTP headers.
- `nmcli`: Network Manager CLI for managing connections.

### Port & Socket Monitoring:
- `ss -tulpn`: Show all listening ports and the processes owning them (Modern `netstat`).
- `lsof -i :80`: See what is running on port 80.
- `dig <domain>`: Query DNS records.
- `nslookup <domain>`: Simple DNS lookup.

---

## 🔒 2. Security Foundations
Securing a Linux box is a multi-layered process.

### SSH (Secure Shell):
- Path: `/etc/ssh/sshd_config`
- `ssh-keygen`: Generate public/private key pairs.
- `ssh-copy-id <user>@<ip>`: Copy your public key for passwordless login.
- **Best Practice**: Disable root login and password authentication.

### Firewall (UFW / IPTables):
- `ufw status`: Check firewall status.
- `ufw allow 22/tcp`: Allow SSH.
- `ufw allow 80,443/tcp`: Allow web traffic.
- `ufw enable`: Turn on the firewall.

### Permissions & Sudo:
- `sudo`: Execute commands with superuser privileges.
- `/etc/sudoers`: The configuration file (edit with `visudo`).
- `fail2ban`: An essential tool to block IP addresses that show malicious signs (like too many failed SSH logins).

---

### 🛡️ SELinux & AppArmor:
These are Mandatory Access Control (MAC) systems that provide granular security policies beyond standard permissions.
- `sestatus`: Check SELinux status.
- `aa-status`: Check AppArmor status.
