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
