# Linux Fundamentals

## 1. Linux Filesystem

Linux uses a hierarchical filesystem that starts at the root directory:

```text
/
├── bin
├── boot
├── dev
├── etc
├── home
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── tmp
├── usr
└── var
```

The `/` directory is called the **root directory**.

---

## Important Directories

### `/home`

Contains the home directories of normal users.

Example:

```text
/home/John
```

---

### `/root`

Home directory of the **root user**.

Note that `/root` and `/` are different:

* `/` = filesystem root
* `/root` = root user's home directory

---

### `/etc`

Contains system configuration files.

Examples:

```text
/etc/passwd
/etc/group
/etc/hosts
```

---

### `/var`

Contains files that frequently change.

Examples:

* Logs
* Application data
* Caches

A common location for logs is:

```text
/var/log
```

---

### `/tmp`

Used for temporary files.

---

### `/usr`

Contains many user programs, libraries, and other system resources.

---

### `/bin`

Contains essential command-line programs.

---

### `/sbin`

Contains system administration programs.

---

### `/dev`

Contains device files representing hardware and other devices.

---

### `/proc`

A virtual filesystem containing information about running processes and the Linux kernel.

For example:

```text
/proc/cpuinfo
/proc/meminfo
```

---

## 2. Linux Permissions

Linux permissions control who can **read, write, or execute** a file.

The three basic permissions are:

| Permission | Symbol | Meaning            |
| ---------- | ------ | ------------------ |
| Read       | `r`    | View file contents |
| Write      | `w`    | Modify file        |
| Execute    | `x`    | Run a file/program |

Permissions are assigned to three categories:

| Category | Meaning                        |
| -------- | ------------------------------ |
| User     | File owner                     |
| Group    | Group associated with the file |
| Others   | Everyone else                  |

---

### Example

Run:

```bash
ls -l
```

You might see:

```text
-rwxr-xr--
```

Breakdown:

```text
- rwx r-x r--
  │   │   │
  │   │   └── Others
  │   └────── Group
  └────────── Owner
```

Therefore:

```text
Owner:  rwx
Group:  r-x
Others: r--
```

The owner can:

* Read
* Write
* Execute

The group can:

* Read
* Execute

Others can:

* Read

---

## Numeric Permissions

Linux permissions can also be represented numerically.

```text
r = 4
w = 2
x = 1
```

Add the values together.

```text
rwx = 4 + 2 + 1 = 7
rw- = 4 + 2 = 6
r-x = 4 + 1 = 5
r-- = 4
```

Example:

```bash
chmod 755 script.sh
```

Means:

```text
Owner:  7 = rwx
Group:  5 = r-x
Others: 5 = r-x
```

Another common example:

```bash
chmod 644 file.txt
```

Means:

```text
Owner:  6 = rw-
Group:  4 = r--
Others: 4 = r--
```

---

# 3. Users and Groups

Linux uses **users and groups** to manage access.

Check the current user:

```bash
whoami
```

Check user information:

```bash
id
```

List users:

```bash
cat /etc/passwd
```

List groups:

```bash
cat /etc/group
```

Check which groups you belong to:

```bash
groups
```

---

## Root

The `root` user has extensive administrative privileges.

Commands requiring administrative privileges are often run with:

```bash
sudo
```

Example:

```bash
sudo apt update
```

**Important:** `sudo` should be used carefully because commands run with elevated privileges can modify important system files.

---

# 4. Processes

A **process** is a running instance of a program.

For example, when you run:

```bash
python3 script.py
```

Linux creates a process for the Python program.

Every process has a **PID (Process ID)**.

---

## View Processes

```bash
ps
```

Show more detailed processes:

```bash
ps aux
```

Interactive process viewer:

```bash
top
```

---

## Kill a Process

First find its PID:

```bash
ps aux
```

Then:

```bash
kill PID
```

Example:

```bash
kill 1234
```

If a process does not respond, a stronger signal can be used:

```bash
kill -9 1234
```

Use `kill -9` carefully because it immediately terminates the process.

---

## Why Processes Matter in Cybersecurity

Understanding processes helps security analysts identify:

* Suspicious programs
* Malware
* Unexpected network connections
* High CPU usage
* Processes running with elevated privileges

Example:

```bash
ps aux
```

can help you investigate whether an unfamiliar process is running.

---

# 5. Basic Linux Commands

## Navigation

### `pwd`

Prints the current working directory.

```bash
pwd
```

Example output:

```text
/home/isha
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

Copies files.

```bash
cp notes.txt backup.txt
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

Removes files.

```bash
rm notes.txt
```

Remove an empty directory:

```bash
rmdir directory
```

Be careful with `rm` because deleted files may not be recoverable.

---

# Reading Files

### `cat`

Displays the contents of a file.

```bash
cat notes.txt
```

---

### `less`

Views a file one page at a time.

```bash
less notes.txt
```

Useful for large files such as logs.

---

### `grep`

Searches for text patterns.

```bash
grep "error" logfile.txt
```

Example:

```bash
grep "failed" /var/log/auth.log
```

This can be useful when investigating authentication failures.

---

### `find`

Searches for files and directories.

```bash
find /home -name "notes.txt"
```

Example:

```bash
find /var/log -type f
```

---

# Permissions

### `chmod`

Changes permissions.

```bash
chmod 755 script.sh
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

---

# Useful Networking Commands

### `ip`

Displays and manages network configuration.

```bash
ip addr
```

---

### `ping`

Tests connectivity to another host.

```bash
ping google.com
```

---

### `ss`

Displays network sockets and connections.

```bash
ss
```

Show listening ports:

```bash
ss -tuln
```

---

### `curl`

Makes HTTP requests and retrieves data from URLs.

```bash
curl https://example.com
```

---

### `dig`

Queries DNS information.

```bash
dig example.com
```

---

### `nslookup`

Looks up DNS information.

```bash
nslookup example.com
```

---

### `traceroute`

Shows the network hops packets take to reach a destination.

```bash
traceroute google.com
```

On some Linux systems, the command may not be installed by default.

---

