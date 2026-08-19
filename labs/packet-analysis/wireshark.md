# Wireshark Packet Analysis

## Objective

Capture network traffic using Wireshark and identify source and destination IP addresses, protocols, transport protocols, and ports.

## What I Did

1. Opened Wireshark in my Ubuntu VM.
2. Selected my active network interface.
3. Started a packet capture.
4. Generated network traffic by browsing websites and using network commands.
5. Stopped the capture.
6. Used Wireshark filters to examine DNS, TCP, and UDP traffic.
7. Examined source IPs, destination IPs, source ports, and destination ports.

## What I Observed

### DNS Traffic

I observed DNS traffic while generating DNS requests.

- Source IP: `192.168.64.2`
- Destination IP: `192.168.64.1`
- Protocol: DNS
- Transport protocol: UDP
- Source port: `40782`
- Destination port: `53`
- Domain queried: `www.nbcnews.com`

I also observed another DNS request with:

- Source port: `33798`
- Destination port: `53`

This showed me that DNS commonly uses UDP and destination port 53. The source port can change between different DNS requests.

### TCP Traffic

I observed TCP traffic involving a web connection.

- Source IP: `192.168.64.2`
- Destination IP: `104.20.23.154`
- Protocol: TCP
- Source port: `37780`
- Destination port: `80`

I also used the Wireshark filter:

`tcp.port == 443`

to look for TCP traffic involving port 443.

I learned that:

- Port `80` is commonly used for HTTP.
- Port `443` is commonly used for HTTPS.
- TCP uses a connection-establishment process involving SYN, SYN-ACK, and ACK packets.

### UDP Traffic

I observed UDP traffic associated with DNS.

- Source IP: `192.168.64.2`
- Destination IP: `192.168.64.1`
- Protocol: DNS
- Transport protocol: UDP
- Source port: `33798`
- Destination port: `53`

## What I Learned

This lab helped me connect networking concepts to actual network traffic.

I learned how to identify:

- Source IP addresses
- Destination IP addresses
- Source ports
- Destination ports
- TCP traffic
- UDP traffic
- DNS traffic
- HTTP/HTTPS traffic

I also learned that DNS is an application-layer protocol that commonly uses UDP as its transport protocol and port 53.

Wireshark makes it possible to inspect individual packets and see information about where traffic is coming from, where it is going, and which protocols and ports are being used.
