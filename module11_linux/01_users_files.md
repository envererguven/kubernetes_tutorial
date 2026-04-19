# Module 11.1: User & File Management

## 👥 1. User Management
Linux is a multi-user system. Managing accounts is fundamental.

### Essential Commands:
- `useradd -m <username>`: Create a new user with a home directory.
- `passwd <username>`: Set or change a password.
- `usermod -aG sudo <username>`: Add a user to the sudoers group (admin rights).
- `userdel -r <username>`: Delete a user and their files.
- `id`: Show the current UID/GID and groups.
- `whoami`: Display the current logged-in user.

### Groups:
- Groups allow you to manage permissions for multiple users at once.
- `/etc/passwd`: Stores user account info.
- `/etc/group`: Stores group info.
- `/etc/shadow`: Stores encrypted passwords.

---

## 📂 2. File Management & Permissions
Everything in Linux is a file.

### Navigating & Manipulating:
- `ls -lah`: List files with details and hidden files.
- `cp -r <src> <dest>`: Copy files or directories recursively.
- `mv <old_name> <new_name>`: Rename or move files.
- `rm -rf <path>`: Force delete files and directories (USE WITH CARE).
- `mkdir -p <path>`: Create nested directories.

### Permissions (The Mode):
Permissions are expressed as `Owner | Group | Others`.
Example: `-rwxr-xr--` (754)

- **r (Read)**: 4
- **w (Write)**: 2
- **x (Execute)**: 1

**Commands:**
- `chmod 755 <file>`: Set permissions (Owner full, others read/exec).
- `chown user:group <file>`: Change the owner and group of a file.
- `ls -l`: Check current permissions.

---

### 🔍 Finding Files:
- `find / -name "config.yaml"`: Search the entire system.
- `grep -r "error" /var/log`: Search for text inside files.
- `locate <filename>`: Faster search using a database (`updatedb`).
