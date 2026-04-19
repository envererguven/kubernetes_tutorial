# Module 11.3: Services & Web Serving

## ⚡ 1. Systemd (Service Management)
Systemd is the init system used by most modern Linux distributions (Ubuntu, Debian, RHEL).

### Essential Commands:
- `systemctl start <service>`: Start a service.
- `systemctl stop <service>`: Stop a service.
- `systemctl restart <service>`: Restart a service (stops then starts).
- `systemctl reload <service>`: Hot-reload configuration without stopping.
- `systemctl enable <service>`: Set service to start automatically on boot.
- `systemctl status <service>`: View health and recent logs.

---

## 🌎 2. Web Serving: Apache (and Nginx)
Serving a website is the most common use case for Linux servers.

### Apache HTTP Server:
- **Install**: `apt install apache2`
- **Root Directory**: `/var/www/html`
- **Config Path**: `/etc/apache2/apache2.conf`
- **Virtual Hosts**: `/etc/apache2/sites-available/`

**Key Commands:**
- `a2ensite <site>`: Enable a website configuration.
- `a2enmod rewrite`: Enable the URL rewrite module.
- `apache2ctl configtest`: Verify syntax before restarting.

### DNS (Domain Name System):
How your server maps names to IPs.
- **Local Settings**: `/etc/hosts`
- **Resolver**: `/etc/resolv.conf` (Nameservers).
- **BIND9**: The industry standard for running your own DNS server.

---

## 🛠️ 3. Environment Variables
- `export MY_VAR="value"`: Set a temporary variable.
- `printenv`: Show all environment variables.
- `~/.bashrc`: Place to set persistent variables for a user.
- `/etc/environment`: System-wide persistent variables.
