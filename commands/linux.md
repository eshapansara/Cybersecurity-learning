# Linux Commands

## Quick Reference

| **Command**  | **Think**                            | **What it does**                                      | **Example**                    |
| ------------ | ------------------------------------ | ----------------------------------------------------- | ------------------------------ |
| `pwd`        | **Where am I?**                      | Shows the current working directory                   | `pwd`                          |
| `ls`         | **What's here?**                     | Lists files and directories                           | `ls`                           |
| `cd`         | **Go somewhere else**                | Changes directories                                   | `cd /home`                     |
| `mkdir`      | **Make a folder**                    | Creates a directory                                   | `mkdir labs`                   |
| `touch`      | **Make a file**                      | Creates an empty file                                 | `touch notes.txt`              |
| `cp`         | **Copy**                             | Copies files or directories                           | `cp notes.txt backup.txt`      |
| `mv`         | **Move/rename**                      | Moves or renames files/directories                    | `mv old.txt new.txt`           |
| `rm`         | **Delete**                           | Removes files or directories                          | `rm notes.txt`                 |
| `rmdir`      | **Remove a folder**                  | Removes an empty directory                            | `rmdir labs`                   |
| `cat`        | **Read this file**                   | Displays the contents of a file                       | `cat notes.txt`                |
| `less`       | **Read a big file**                  | Views a file one page at a time                       | `less logfile.txt`             |
| `grep`       | **Search inside files**              | Searches for text patterns inside files               | `grep "error" logfile.txt`     |
| `find`       | **Find files**                       | Searches for files and directories                    | `find /home -name "notes.txt"` |
| `chmod`      | **Change permissions**               | Changes file or directory permissions                 | `chmod 755 script.sh`          |
| `chown`      | **Change ownership**                 | Changes the owner of a file or directory              | `sudo chown user file.txt`     |
| `sudo`       | **Act as administrator**             | Runs a command with elevated privileges               | `sudo apt update`              |
| `whoami`     | **Who am I?**                        | Shows the current username                            | `whoami`                       |
| `id`         | **What's my user info?**             | Shows user ID, group ID, and groups                   | `id`                           |
| `ps`         | **What processes are running?**      | Displays running processes                            | `ps aux`                       |
| `top`        | **What's running right now?**        | Monitors running processes in real time               | `top`                          |
| `kill`       | **Stop a process**                   | Terminates a process using its PID                    | `kill 1234`                    |
| `ip`         | **What's my network configuration?** | Displays and manages network interfaces and addresses | `ip addr`                      |
| `ping`       | **Can I reach it?**                  | Tests network connectivity to another host            | `ping google.com`              |
| `ss`         | **What connections/ports exist?**    | Displays network sockets and connections              | `ss -tuln`                     |
| `curl`       | **Talk to a web server**             | Makes HTTP requests and retrieves data                | `curl https://example.com`     |
| `dig`        | **Investigate DNS**                  | Queries DNS information                               | `dig example.com`              |
| `nslookup`   | **Look up DNS**                      | Looks up DNS information for a domain                 | `nslookup example.com`         |
| `traceroute` | **How does traffic get there?**      | Shows the network hops packets take to a destination  | `traceroute google.com`        |

---

# Command Examples

## Navigation

### `pwd`

Shows the current working directory.

```bash
pwd
```

Example output:

```text
/home/John
```

---

### `ls`

Lists files and directories.

```bash
ls
```

Detailed listing:

```bash
ls -l
```

Show hidden files:

```bash
ls -la
```

---

### `cd`

Changes directories.

```bash
cd /home
```

Go to the parent directory:

```bash
cd ..
```

Go to your home directory:

```bash
cd ~
```

---

# File and Directory Management

### `mkdir`

Creates a directory.

```bash
mkdir labs
```

---

### `touch`

Creates an empty file.

```bash
touch notes.txt
```

---

### `cp`

Copies a file.

```bash
cp notes.txt backup.txt
```

Copy a file into a directory:

```bash
cp notes.txt labs/
```

---

### `mv`

Moves or renames files.

Rename:

```bash
mv old.txt new.txt
```

Move:

```bash
mv notes.txt labs/
```

---

### `rm`

Removes a file.

```bash
rm notes.txt
```

Be careful with `rm` because deleted files may not be recoverable.

---

### `rmdir`

Removes an empty directory.

```bash
rmdir labs
```

---

# Reading and Searching Files

### `cat`

Displays the contents of a file.

```bash
cat notes.txt
```

---

### `less`

Views a file one page at a time.

```bash
less logfile.txt
```

Useful for reading large files such as logs.

**Useful keys inside `less`:**

```text
Space       → Next page
b           → Previous page
↑ / ↓       → Move up/down
q           → Quit
```

---

### `grep`

Searches for text patterns inside files.

```bash
grep "error" logfile.txt
```

Example for security logs:

```bash
grep "failed" /var/log/auth.log
```

This can help identify failed authentication attempts.

---

### `find`

Searches for files and directories.

```bash
find /home -name "notes.txt"
```

Find all files inside `/var/log`:

```bash
find /var/log -type f
```

---

# Permissions and Ownership

### `chmod`

Changes file permissions.

```bash
chmod 755 script.sh
```

Example:

```text
755
│││
││└── Others: Read + Execute
│└─── Group:  Read + Execute
└──── Owner:  Read + Write + Execute
```

---

### `chown`

Changes file ownership.

```bash
sudo chown user file.txt
```

---

# Administrative Commands

### `sudo`

Runs a command with elevated privileges.

```bash
sudo command
```

Example:

```bash
sudo apt update
```

`sudo` is commonly used when performing administrative tasks.

---

# Users and Groups

### `whoami`

Shows the username of the current user.

```bash
whoami
```

Example output:

```text
John
```

---

### `id`

Shows information about the current user, including UID, GID, and groups.

```bash
id
```

Example output:

```text
uid=1000(John) gid=1000(John) groups=1000(John),27(sudo)
```

---

# Processes

### `ps`

Displays running processes.

```bash
ps
```

Show processes for all users with more information:

```bash
ps aux
```

---

### `top`

Provides a real-time view of running processes and system resource usage.

```bash
top
```

Press:

```text
q
```

to quit.

---

### `kill`

Terminates a process using its PID.

First find the process:

```bash
ps aux
```

Then:

```bash
kill 1234
```

where `1234` is the process ID (PID).

A stronger termination signal:

```bash
kill -9 1234
```

Use `kill -9` carefully because it immediately terminates the process.

---

# Networking Commands

### `ip`

Displays network configuration.

```bash
ip addr
```

Useful for viewing:

* IP addresses
* Network interfaces
* Interface status

---

### `ping`

Tests whether another host can be reached.

```bash
ping google.com
```

Example:

```bash
ping 8.8.8.8
```

---

### `ss`

Displays network sockets and connections.

```bash
ss
```

Show listening TCP/UDP ports:

```bash
ss -tuln
```

This is particularly useful in cybersecurity when investigating what services are listening on a machine.

---

### `curl`

Makes HTTP requests and retrieves data from a web server.

```bash
curl https://example.com
```

You can use it to inspect a webpage's response:

```bash
curl -I https://example.com
```

`-I` requests the HTTP headers instead of the entire page.

---

### `dig`

Queries DNS information.

```bash
dig example.com
```

Useful for investigating:

* IP addresses
* DNS records
* Name servers
* Mail servers

For example:

```bash
dig example.com A
```

---

### `nslookup`

Looks up DNS information.

```bash
nslookup example.com
```

Example:

```bash
nslookup google.com
```

---

### `traceroute`

Shows the network hops between your computer and a destination.

```bash
traceroute google.com
```

Example output will show multiple hops:

```text
1    192.168.1.1
2    10.0.0.1
3    ...
4    ...
```

Each hop represents a router or network device along the path.

**Note:** `traceroute` may not be installed by default on some Linux systems.

---

# Useful Command Options

Many Linux commands have **options/flags** that modify their behavior.

| **Command** | **Option** | **Meaning**               | **Example**                    |
| ----------- | ---------- | ------------------------- | ------------------------------ |
| `ls`        | `-l`       | Detailed listing          | `ls -l`                        |
| `ls`        | `-a`       | Show hidden files         | `ls -a`                        |
| `ls`        | `-la`      | Detailed + hidden files   | `ls -la`                       |
| `ps`        | `aux`      | Detailed process list     | `ps aux`                       |
| `ss`        | `-t`       | TCP connections           | `ss -t`                        |
| `ss`        | `-u`       | UDP connections           | `ss -u`                        |
| `ss`        | `-l`       | Listening sockets         | `ss -l`                        |
| `ss`        | `-n`       | Don't resolve names       | `ss -n`                        |
| `curl`      | `-I`       | Show HTTP headers         | `curl -I https://example.com`  |
| `dig`       | `A`        | Query IPv4 address record | `dig example.com A`            |
| `find`      | `-name`    | Search by filename        | `find /home -name "notes.txt"` |
| `find`      | `-type f`  | Find files                | `find /var/log -type f`        |

---

# Cybersecurity Commands to Know Especially Well

These are worth becoming very comfortable with because you'll use them frequently in cybersecurity labs:

```bash
ls -la
```

**Inspect files, including hidden files and permissions**

```bash
ps aux
```

**Inspect running processes**

```bash
ss -tuln
```

**Inspect listening network ports**

```bash
grep "failed" /var/log/auth.log
```

**Search authentication logs**

```bash
find /var/log -type f
```

**Find log files**

```bash
chmod 755 script.sh
```

**Modify permissions**

```bash
ip addr
```

**Inspect network interfaces**

```bash
whoami
```

**Identify the current user**

```bash
id
```

**Inspect user and group information**

```bash
sudo command
```

**Execute a command with elevated privileges**
