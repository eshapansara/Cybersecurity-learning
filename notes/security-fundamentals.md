# Security Fundamentals

## 1. CIA Triad

The **CIA Triad** is one of the fundamental concepts in cybersecurity. It describes the three main goals of information security:

### Confidentiality

Ensures that information is only accessible to **authorized people or systems**.

**Examples:**

* Passwords
* Encryption
* Access controls
* File permissions

**Example scenario:**
A company's employee records should only be accessible to authorized HR employees.

---

### Integrity

Ensures that information is **accurate, trustworthy, and has not been improperly modified**.

**Examples:**

* Hashing
* Digital signatures
* File integrity monitoring
* Version control

**Example scenario:**
An attacker changes a bank transaction from `$100` to `$10,000`. This is an integrity violation.

---

### Availability

Ensures that systems and information are **accessible when authorized users need them**.

**Examples:**

* Backups
* Redundant servers
* Disaster recovery
* DDoS protection
* Monitoring

**Example scenario:**
A company's website becomes unavailable because of a DDoS attack.

---

### CIA Triad Summary

| Principle       | Goal                              | Example    |
| --------------- | --------------------------------- | ---------- |
| Confidentiality | Prevent unauthorized access       | Encryption |
| Integrity       | Prevent unauthorized modification | Hashing    |
| Availability    | Keep systems accessible           | Backups    |

**Memory trick:**
**C = Can they see it?**
**I = Is it accurate?**
**A = Is it available?**

---

# 2. Threats vs Vulnerabilities vs Risks

These three concepts are related but are **not the same thing**.

## Threat

A **threat** is something that has the potential to cause harm to a system or organization.

Examples:

* Malware
* Phishing
* Hackers
* Insider threats
* Natural disasters

**Think:** "What could hurt us?"

---

## Vulnerability

A **vulnerability** is a **weakness** that could be exploited.

Examples:

* Outdated software
* Weak passwords
* Misconfigured firewall
* Unpatched operating system
* Excessive permissions

**Think:** "What weakness could be exploited?"

---

## Risk

**Risk** is the potential for a threat to exploit a vulnerability and cause harm.

A simplified way to think about it:

> **Risk = Threat × Vulnerability × Impact**

Risk considers both the likelihood of something happening and the consequences if it happens.

---

### Example

A company has an internet-facing server running outdated software.

* **Threat:** Attacker
* **Vulnerability:** Unpatched software
* **Risk:** Attacker exploits the software and gains access to the server
* **Impact:** Data theft or system downtime

### Easy way to remember

> **Threat = danger**
> **Vulnerability = weakness**
> **Risk = potential damage from the danger exploiting the weakness**

---

# 3. Authentication vs Authorization

## Authentication

**Authentication** answers:

> **"Who are you?"**

It verifies a user's identity.

Examples:

* Username + password
* MFA
* Fingerprint
* Face recognition
* Security keys

---

## Authorization

**Authorization** answers:

> **"What are you allowed to do?"**

It determines what an authenticated user can access or modify.

Examples:

* Read a file
* Edit a database
* Access an admin dashboard
* Delete an account

---

### Example

You log into a company's system.

1. You enter your username and password.
2. The system verifies your identity → **Authentication**
3. The system determines that you're allowed to view employee records but not modify them → **Authorization**

**Memory trick:**

> **Authentication = Who are you?**
> **Authorization = What can you do?**

