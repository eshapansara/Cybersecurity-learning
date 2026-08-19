# Networking Fundamentals

Networking is the foundation of cybersecurity. Security professionals need to understand how devices communicate, how data moves across networks, and where attacks can occur.

---

# 1. IP Addresses

An **IP address** identifies a device/interface on a network.

Think:

> **IP address = Where is this device?**

There are two main versions:

* IPv4
* IPv6

---

## IPv4

IPv4 addresses consist of four numbers separated by periods.

Example:

```text
192.168.1.10
```

Each number can range from `0` to `255`.

Example:

```text
192.168.1.10
10.0.0.5
8.8.8.8
```

---

## Public vs Private IP Addresses

### Private IP

Used inside local/private networks.

Common private ranges include:

```text
10.0.0.0 – 10.255.255.255
172.16.0.0 – 172.31.255.255
192.168.0.0 – 192.168.255.255
```

Example:

```text
192.168.1.25
```

Your computer might have a private IP assigned by your router.

---

### Public IP

Used to identify a network/device on the public Internet.

Example:

```text
8.8.8.8
```

Public IP addresses are globally routable.

---

## Loopback Address

The IPv4 loopback address is:

```text
127.0.0.1
```

It refers to the local computer itself.

You may also see:

```text
localhost
```

Example:

```bash
ping 127.0.0.1
```

Think:

> **127.0.0.1 = This computer**

---

## Checking Your IP Address

On Linux:

```bash
ip addr
```

or:

```bash
ip a
```

---

# 2. TCP and UDP

TCP and UDP are **transport-layer protocols**.

They determine how data is transported between applications.

Think:

> **TCP/UDP = How should the data be delivered?**

---

## TCP

**TCP = Transmission Control Protocol**

TCP is **connection-oriented** and focuses on reliable delivery.

TCP provides:

* Reliable delivery
* Ordered data
* Error detection
* Retransmission of lost data
* Connection establishment

---

### TCP Three-Way Handshake

Before sending data, TCP establishes a connection using a three-way handshake:

```text
Client                  Server
  |                       |
  | ------ SYN ---------> |
  | <----- SYN-ACK ------ |
  | ------ ACK ---------> |
  |                       |
       Connection
       established
```

### Steps

**1. SYN**

Client asks to establish a connection.

**2. SYN-ACK**

Server acknowledges the request and responds.

**3. ACK**

Client acknowledges the server.

The TCP connection can now be established.

---

## UDP

**UDP = User Datagram Protocol**

UDP is **connectionless**.

It does not establish a connection before sending data.

UDP generally provides:

* Lower overhead
* Faster transmission
* No guaranteed delivery
* No guaranteed ordering
* No retransmission mechanism like TCP

---

## TCP vs UDP

| **TCP**               | **UDP**                                   |
| --------------------- | ----------------------------------------- |
| Connection-oriented   | Connectionless                            |
| Reliable delivery     | No delivery guarantee                     |
| Ordered data          | No ordering guarantee                     |
| Retransmits lost data | Does not provide TCP-style retransmission |
| More overhead         | Less overhead                             |
| Generally slower      | Generally faster                          |
| Web traffic (HTTPS)   | DNS commonly uses UDP                     |
| SSH                   | DHCP                                      |
| Email                 | Streaming/real-time applications          |

### Memory trick

> **TCP = "Take Care of Packets"**
> **UDP = "User Datagram Protocol"**

The key distinction is **reliability/connection management vs lightweight connectionless transport**.

---

# 3. Ports

A **port** identifies a specific network service or application on a device.

Think:

> **IP address = Which device?**
> **Port = Which service on that device?**

For example:

```text
192.168.1.10:443
```

Means:

* `192.168.1.10` → device
* `443` → service/application endpoint

---

## Port Numbers

Ports range from:

```text
0 – 65535
```

Commonly grouped as:

| Range         | Name                  |
| ------------- | --------------------- |
| `0–1023`      | Well-known ports      |
| `1024–49151`  | Registered ports      |
| `49152–65535` | Dynamic/private ports |

---

## Common Ports

| **Port** | **Protocol/Service** | **Purpose**            |
| -------: | -------------------- | ---------------------- |
|  `20/21` | FTP                  | File transfer          |
|     `22` | SSH                  | Secure remote access   |
|     `23` | Telnet               | Remote access          |
|     `25` | SMTP                 | Email transfer         |
|     `53` | DNS                  | Domain name resolution |
|     `80` | HTTP                 | Web traffic            |
|    `110` | POP3                 | Email retrieval        |
|    `143` | IMAP                 | Email retrieval        |
|    `443` | HTTPS                | Secure web traffic     |
|   `3389` | RDP                  | Windows remote desktop |

Important:

> A port number doesn't inherently make something secure or insecure. The service and configuration matter.

---

## Listening Ports

A server can listen for incoming connections on a port.

Check listening ports on Linux:

```bash
ss -tuln
```

You might see something like:

```text
LISTEN 0 128 0.0.0.0:22
```

This means a service is listening on port `22`.

From a cybersecurity perspective, unnecessary open ports can increase the **attack surface**.

---

# 4. DNS

**DNS = Domain Name System**

DNS translates domain names into IP addresses.

Think:

> **DNS = Internet phone book**

Humans prefer:

```text
google.com
```

Computers communicate using IP addresses such as:

```text
142.250.x.x
```

DNS helps translate between them.

---

## Example

When you enter:

```text
https://example.com
```

your computer needs to determine the IP address associated with `example.com`.

A DNS query helps find that information.

---

## DNS Flow

Simplified:

```text
You
 |
 v
DNS Resolver
 |
 v
DNS Servers
 |
 v
IP Address
 |
 v
Website
```

---

## Common DNS Record Types

| **Record** | **Purpose**                                                   |
| ---------- | ------------------------------------------------------------- |
| `A`        | Maps domain → IPv4 address                                    |
| `AAAA`     | Maps domain → IPv6 address                                    |
| `CNAME`    | Alias for another domain                                      |
| `MX`       | Specifies mail servers                                        |
| `NS`       | Specifies authoritative name servers                          |
| `TXT`      | Stores text information, often used for verification/security |

---

## DNS Commands

Use:

```bash
dig example.com
```

or:

```bash
nslookup example.com
```

For an IPv4 address specifically:

```bash
dig example.com A
```

---

# 5. HTTP and HTTPS

## HTTP

**HTTP = Hypertext Transfer Protocol**

HTTP is used for communication between web clients and web servers.

Think:

> **HTTP = Rules for communicating with websites**

Example:

```text
Client → HTTP Request → Server
Client ← HTTP Response ← Server
```

---

## HTTP Request

A browser might send a request such as:

```http
GET /index.html HTTP/1.1
Host: example.com
```

The server processes the request and sends a response.

---

## HTTP Response

A server might respond with:

```http
HTTP/1.1 200 OK
```

followed by the requested content.

---

## Common HTTP Methods

| **Method** | **Purpose**           |
| ---------- | --------------------- |
| `GET`      | Retrieve data         |
| `POST`     | Send/create data      |
| `PUT`      | Replace/update data   |
| `PATCH`    | Partially update data |
| `DELETE`   | Delete data           |

---

## HTTP Status Codes

| **Code** | **Meaning**           |
| -------: | --------------------- |
|    `200` | OK                    |
|    `201` | Created               |
|    `301` | Moved Permanently     |
|    `302` | Found/redirect        |
|    `400` | Bad Request           |
|    `401` | Unauthorized          |
|    `403` | Forbidden             |
|    `404` | Not Found             |
|    `500` | Internal Server Error |
|    `503` | Service Unavailable   |

---

# HTTPS

**HTTPS = HTTP Secure**

HTTPS uses **TLS (Transport Layer Security)** to protect HTTP communication.

It provides:

* Encryption
* Authentication of the server
* Integrity protection

Example:

```text
HTTP
Client ------------------> Server
       readable traffic


HTTPS
Client ==================> Server
       encrypted traffic
```

HTTPS normally uses:

```text
Port 443
```

HTTP normally uses:

```text
Port 80
```

---

## Why HTTPS Matters in Cybersecurity

Without encryption, sensitive information transmitted over a network could potentially be exposed.

HTTPS helps protect information such as:

* Passwords
* Session cookies
* Personal information
* Payment information

---

# 6. Client and Server

A **client** requests a service.

A **server** provides a service.

Think:

> **Client = asks**,
> **Server = provides**

---

## Example: Visiting a Website

```text
             Request
Client --------------------> Server
Browser                     Web Server
             Response
Client <-------------------- Server
```

Your browser is the **client**.

The website's computer/system is the **server**.

---

## Client

Examples:

* Web browser
* Mobile application
* SSH client
* Email client

---

## Server

Examples:

* Web server
* DNS server
* Email server
* Database server
* SSH server

---

## Important

A device can act as both a client and a server.

For example, your computer could:

* Act as a client when browsing a website
* Act as a server when hosting a web application

---

# 7. Firewalls

A **firewall** controls network traffic based on predefined rules.

Think:

> **Firewall = Security guard for network traffic**

A firewall can allow or block traffic based on things such as:

* Source IP
* Destination IP
* Port
* Protocol
* Direction
* Other connection information

---

## Example

Suppose a server only needs HTTPS.

The firewall might allow:

```text
TCP → Port 443 → ALLOW
```

and block:

```text
TCP → Port 22 → BLOCK
```

if SSH access is not needed.

---

## Firewall Example

```text
Internet
    |
    v
+-----------+
| Firewall  |
+-----------+
    |
    | Allowed traffic
    v
+-----------+
|  Server   |
+-----------+
```

The firewall sits between networks or devices and applies traffic rules.

---

## Inbound vs Outbound

### Inbound

Traffic coming **into** a system.

Example:

```text
Internet → Server
```

### Outbound

Traffic leaving a system.

Example:

```text
Server → Internet
```

Firewalls can control both.

---

## Why Firewalls Matter

Firewalls can help:

* Reduce attack surface
* Block unauthorized connections
* Restrict access to services
* Segment networks
* Control inbound and outbound traffic

A firewall is **not** a complete security solution. It works as one layer of a broader defense strategy.

---

# 8. Packets

A **packet** is a small unit of data transmitted across a network.

Think:

> **Packet = A small package of network data**

Large amounts of information are typically broken into smaller pieces for transmission.

---

## Simplified Packet Journey

```text
Application Data
       ↓
     Packet
       ↓
    Network
       ↓
    Router
       ↓
    Network
       ↓
 Destination
```

---

## What's Inside a Packet?

A packet contains information used to deliver the data.

Depending on the protocol and layer, this can include:

* Source IP address
* Destination IP address
* Source port
* Destination port
* Protocol information
* Payload/data

---

## Example

Imagine:

```text
Source IP:      192.168.1.10
Destination IP: 8.8.8.8
Source Port:    52341
Destination Port: 53
Protocol:       UDP
```

This could represent a DNS query being sent to a DNS server.

---

# 9. Putting Everything Together

When you visit a website, many of these concepts work together.

Suppose you enter:

```text
https://example.com
```

### Step 1 — DNS

Your computer needs the IP address for:

```text
example.com
```

DNS provides the address.

---

### Step 2 — Client/Server

Your browser acts as the:

```text
Client
```

The website's system acts as the:

```text
Server
```

---

### Step 3 — Port

HTTPS normally uses:

```text
TCP port 443
```

---

### Step 4 — TCP

The client establishes a TCP connection with the server.

```text
SYN
   ↓
SYN-ACK
   ↓
ACK
```

---

### Step 5 — HTTPS

TLS protects the HTTP communication.

Your browser can then securely communicate with the web server.

---

### Step 6 — Packets

The information is transmitted across the network in packets.

```text
Your Computer
      |
      | packets
      v
   Router(s)
      |
      | packets
      v
 Web Server
```

---

### Step 7 — Firewall

Firewalls along the path may inspect traffic and determine whether it should be allowed or blocked.

---

# 10. The Big Picture

Remember these relationships:

```text
IP Address
    ↓
Identifies the device/interface
    ↓
Port
    ↓
Identifies the service/application endpoint
    ↓
TCP / UDP
    ↓
Determines how data is transported
    ↓
Packets
    ↓
Carry the data across the network
    ↓
DNS
    ↓
Maps human-readable names to IP addresses
    ↓
HTTP / HTTPS
    ↓
Defines web communication
    ↓
Client ↔ Server
    ↓
Firewall
    ↓
Controls whether network traffic is allowed
```

## Quick Memory Table

| **Concept** | **Think**                           | **Example**           |
| ----------- | ----------------------------------- | --------------------- |
| IP address  | **Where is the device?**            | `192.168.1.10`        |
| Port        | **Which service?**                  | `443`                 |
| TCP         | **Reliable connection**             | HTTPS                 |
| UDP         | **Fast, connectionless**            | DNS                   |
| DNS         | **What's this domain's IP?**        | `example.com → IP`    |
| HTTP        | **Web communication**               | `GET /index.html`     |
| HTTPS       | **Secure web communication**        | `https://example.com` |
| Client      | **Who is asking?**                  | Browser               |
| Server      | **Who is providing?**               | Web server            |
| Firewall    | **Should this traffic be allowed?** | Allow/block port 443  |
| Packet      | **Small piece of network data**     | IP + port + payload   |

## Useful Commands

```bash
# View IP addresses
ip addr

# Test connectivity
ping google.com

# View listening ports
ss -tuln

# DNS lookup
dig example.com

# DNS lookup
nslookup example.com

# Make an HTTP request
curl https://example.com

# View HTTP headers
curl -I https://example.com

# Trace network path
traceroute google.com
```
