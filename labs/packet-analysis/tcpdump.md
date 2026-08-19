
# tcpdump Packet Analysis

## Objective

Use tcpdump to capture and analyze network traffic from my Ubuntu VM and identify source IP addresses, destination IP addresses, protocols, and ports.

## What I Did

1. Opened the Ubuntu terminal.
2. Used tcpdump to capture general network traffic.
3. Generated ICMP traffic using `ping google.com`.
4. Used tcpdump to filter for DNS traffic on port 53.
5. Used `nslookup google.com` to generate DNS traffic.
6. Used tcpdump to capture TCP traffic.
7. Used `curl https://example.com` to generate web traffic.
8. Used tcpdump to filter for UDP traffic.
9. Examined source IPs, destination IPs, source ports, destination ports, and protocols.

---

## Investigation 1 — General Traffic

### Command

```bash
sudo tcpdump -i any -n
````

### Traffic Generated

```bash
ping google.com
```

### Observation

* **Source IP:** `192.168.64.2`
* **Destination IP:** `172.253.124.102`
* **Protocol:** `ICMP`
* **Traffic Type:** Ping / ICMP Echo Request and Echo Reply

The `ping` command generated ICMP traffic between my Ubuntu VM and the destination IP.

### What This Means

```text
192.168.64.2
      ↓
ICMP Echo Request
      ↓
172.253.124.102
      ↓
ICMP Echo Reply
      ↓
192.168.64.2
```

ICMP is used for network communication such as testing whether a host is reachable. Unlike TCP and UDP, ICMP does not use TCP or UDP ports.

---

## Investigation 2 — DNS Traffic

### Command

```bash
sudo tcpdump -i any -n port 53
```

### Traffic Generated

```bash
nslookup google.com
```

### Observation

* **Source IP:** `192.168.64.2`
* **Destination IP:** `192.168.64.1`
* **Source Port:** `52212`
* **Destination Port:** `53`
* **Application Protocol:** `DNS`
* **Transport Protocol:** `UDP`

### Additional DNS Observation

I also observed another DNS request:

* **Source IP:** `192.168.64.2`
* **Destination IP:** `192.168.64.1`
* **Source Port:** `40782`
* **Destination Port:** `53`
* **Domain Queried:** `www.nbcnews.com`
* **Transport Protocol:** `UDP`

### What This Means

```text
192.168.64.2:52212
        ↓
       UDP
        ↓
192.168.64.1:53
        ↓
    DNS Query
```

DNS is an application-layer protocol that commonly uses UDP as its transport protocol.

Port `53` is the standard port associated with DNS.

I also noticed that the source port can change between different DNS requests, while the destination port remains `53`.

---

## Investigation 3 — TCP Traffic

### Command

```bash
sudo tcpdump -i any -n tcp
```

### Traffic Generated

```bash
curl https://example.com
```

### Observation

* **Source IP:** `192.168.64.2`
* **Destination IP:** `104.20.23.154`
* **Protocol:** `TCP`
* **Source Port:** `37780`
* **Destination Port:** `80`

I observed TCP traffic involving a web connection.

### What This Means

```text
192.168.64.2:37780
        ↓
       TCP
        ↓
104.20.23.154:80
```

Port `80` is commonly associated with HTTP.

Port `443` is commonly associated with HTTPS.

A TCP connection is established using a three-way handshake:

```text
Client → SYN
Server → SYN-ACK
Client → ACK
```

This allows the two devices to establish a TCP connection before communicating.

---

## Investigation 4 — UDP Traffic

### Command

```bash
sudo tcpdump -i any -n udp
```

### Traffic Generated

```bash
nslookup google.com
```

### Observation

* **Source IP:** `192.168.64.2`
* **Destination IP:** `192.168.64.1`
* **Source Port:** `33798`
* **Destination Port:** `53`
* **Application Protocol:** `DNS`
* **Transport Protocol:** `UDP`

### What This Means

This was another example of DNS traffic being transported using UDP.

```text
192.168.64.2:33798
        ↓
       UDP
        ↓
192.168.64.1:53
        ↓
    DNS Query
```

This confirmed that DNS commonly uses UDP and destination port `53`.

---

## What I Learned

This lab helped me understand how tcpdump can be used to capture and analyze network traffic from the command line.

I learned how to identify:

* Source IP addresses
* Destination IP addresses
* Source ports
* Destination ports
* ICMP traffic
* TCP traffic
* UDP traffic
* DNS traffic
* HTTP traffic

I also learned the difference between application-layer protocols and transport-layer protocols.

For example:

```text
DNS
 ↓
Application Layer
 ↓
UDP
 ↓
Transport Layer
 ↓
Port 53
```

I learned that:

* **ICMP** is used by tools such as `ping` and does not use TCP/UDP ports.
* **DNS** commonly uses UDP port `53`.
* **HTTP** commonly uses TCP port `80`.
* **HTTPS** commonly uses TCP port `443`.
* Source ports can be temporary/dynamic ports chosen by the client.
* Destination ports commonly identify the service the client is communicating with.

## Conclusion

Using tcpdump allowed me to see the networking concepts I learned in actual network traffic. I was able to identify IP addresses, ports, TCP, UDP, ICMP, and DNS traffic from the command line.

This lab helped me connect networking fundamentals to practical packet analysis and provides a foundation for understanding how network traffic can be monitored and investigated in cybersecurity.
