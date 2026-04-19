# Module 11.0: Ubuntu & Linux Command Cheat Sheet

This guide serves as a quick reference for the most essential commands you will use daily in Ubuntu and other Debian-based systems.

---

## 📦 1. Package Management (Ubuntu/Debian `apt`)
Keeping your system updated and installing software.

- `sudo apt update`: Update the package index (checks for new versions).
- `sudo apt upgrade`: Install all available updates for currently installed packages.
- `sudo apt install <package>`: Install a new software package.
- `sudo apt remove <package>`: Remove a package.
- `sudo apt autoremove`: Remove unused dependencies/old kernels.
- `sudo apt search <term>`: Search for a package in the repository.

---

## 📂 2. File & Directory Operations
Navigating and manipulating the filesystem.

- `ls`: List directory contents.
- `ls -lah`: List all files with human-readable sizes and hidden files.
- `cd <dir>`: Change directory.
- `pwd`: Print working directory.
- `mkdir <dir>`: Create a new directory.
- `cp <src> <dest>`: Copy files.
- `mv <src> <dest>`: Move or rename files.
- `rm <file>`: Delete a file.
- `rm -rf <dir>`: Recursively force-delete a directory.
- `touch <file>`: Create an empty file.

---

## 🔍 3. Text Processing & Viewing
Searching and displaying file content.

- `cat <file>`: Display the whole file.
- `head -n 20 <file>`: Show the first 20 lines.
- `tail -n 20 <file>`: Show the last 20 lines.
- `tail -f <file>`: Follow a file in real-time (Great for logs!).
- `grep "pattern" <file>`: Search for text inside a file.
- `grep -r "pattern" <dir>`: Search recursively through a directory.
- `echo "text" > <file>`: Write text to a file (overwrites).
- `echo "text" >> <file>`: Append text to a file.
- `find /path -name "*.log"`: Find files by name.
- `locate <file>`: Quickly find files by database (Run `sudo updatedb` first).

---

## ⚙️ 4. Process & System Monitoring
Seeing what is running and managing resources.

- `top`: Real-time system monitoring.
- `ps aux`: List all running processes.
- `ps aux | grep <name>`: Find a specific running process.
- `kill <pid>`: Gracefully stop a process.
- `kill -9 <pid>`: Forcefully kill a process.
- `free -h`: Check RAM/Swap usage.
- `df -h`: Check Disk usage.
- `du -sh <dir>`: Check size of a specific directory.
- `uptime`: See how long the system has been up and its load.

---

## 🌐 5. Basic Networking
- `ip addr`: Show IP addresses.
- `ping <host>`: Check connectivity.
- `curl <url>`: Fetch data from a URL.
- `wget <url>`: Download a file from the web.
- `ssh user@host`: Connect to a remote server.
