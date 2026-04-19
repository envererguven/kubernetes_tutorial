# Module 11.5: Shell Scripting Foundation

## 🐚 1. Why Bash Scripting?
Automating repetitive tasks is the difference between a Junior and a Senior SysAdmin.

### Anatomy of a Script:
```bash
#!/bin/bash
# This is a comment

NAME="User"
echo "Hello $NAME, today is $(date)"
```

---

## 🏗️ 2. Core Concepts

### Variables:
- `VAR="value"`: Assign.
- `$VAR`: Access.

### Conditional Logic (if/else):
```bash
if [ -f "/etc/passwd" ]; then
    echo "Filesystem is accessible."
else
    echo "Warning: Critical file missing!"
fi
```

### Loops (for/while):
```bash
# Iterating over files
for file in *.md; do
    echo "Processing document: $file"
done
```

---

## 🛠️ 3. Useful Scripting Tools
- `awk`: Powerful text processing (column extraction).
- `sed`: Stream editor for find and replace.
- `cut`: Extract pieces of lines based on delimiters.
- `xargs`: Pass output of one command as arguments to another.

### Example: A basic backup script
```bash
#!/bin/bash
BACKUP_DIR="/backups"
SOURCE_DIR="/var/www/html"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR
tar -czf $BACKUP_DIR/backup_$TIMESTAMP.tar.gz $SOURCE_DIR
echo "Backup saved to $BACKUP_DIR"
```

---

### 📝 Lab Exercise:
1. Create a file called `hello.sh`.
2. Add the Shebang (`#!/bin/bash`).
3. Make it print your current user and uptime.
4. Run `chmod +x hello.sh`.
5. Execute it with `./hello.sh`.
