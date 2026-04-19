# Module 11.4: Professional SysAdmin: Troubleshooting & Booting

## 📊 1. System Monitoring
Knowing what happens under the hood is vital.

### Resource Checks:
- `top`: Real-time view of CPU/Memory usage and processes.
- `htop`: A more interactive, colorized version of `top`.
- `df -h`: View disk space usage in human-readable format.
- `free -m`: View RAM and Swap usage.
- `uptime`: How long the system has been running and load average.
- `iotop`: Monitor disk I/O per process.

---

## 🔧 2. Troubleshooting & Logs
When things break, the logs have the answer.

### Log Locations:
- `/var/log/syslog`: General system logs.
- `/var/log/auth.log`: Security/Login logs.
- `/var/log/apache2/error.log`: Web server errors.
- `/var/log/dmesg`: Kernel and hardware logs.

### Command Power:
- `journalctl -u <service> -f`: Stream logs for a specific service.
- `tail -f /var/log/syslog`: Watch logs in real-time.
- `dmesg | grep -i error`: Look for hardware/kernel failures.
- `strace <command>`: Trace system calls (Advanced debugging).

---

## 🚀 3. Boot Process & Runlevels
What happens from Power On to Login?

1. **BIOS/UEFI**: Basic hardware check.
2. **Bootloader (GRUB)**: Loads the Linux Kernel.
3. **Kernel**: Initializes hardware and starts `init` (PID 1).
4. **Init (Systemd)**: Starts all system services.

### Key Knowledge:
- **Runlevels / Targets**:
  - `multi-user.target`: Standard server mode (No UI).
  - `graphical.target`: Standard desktop mode.
- `reboot`: Safely restart.
- `shutdown -h now`: Shutdown immediately.
