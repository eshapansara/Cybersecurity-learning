# Web Security Fundamentals

Web security is about protecting websites, web applications, APIs, users, and the data they handle.

---

# 1. HTTP

**HTTP = Hypertext Transfer Protocol**

HTTP is the protocol used for communication between a client and a web server.

Think:

> **HTTP = Rules for web communication**

Basic flow:

```text
Browser
   |
   | HTTP Request
   ↓
Web Server
   |
   | HTTP Response
   ↓
Browser
```

## HTTP Request

A request contains information such as:

* HTTP method
* URL/path
* Headers
* Optional body

Example:

```http
GET /index.html HTTP/1.1
Host: example.com
```

## HTTP Response

The server responds with:

```http
HTTP/1.1 200 OK
Content-Type: text/html
```

followed by the response body.

## Common HTTP Methods

| Method   | Purpose               |
| -------- | --------------------- |
| `GET`    | Retrieve data         |
| `POST`   | Send/create data      |
| `PUT`    | Replace/update data   |
| `PATCH`  | Partially update data |
| `DELETE` | Delete data           |

## Common HTTP Status Codes

| Code  | Meaning                 |
| ----- | ----------------------- |
| `200` | OK                      |
| `201` | Created                 |
| `301` | Moved Permanently       |
| `400` | Bad Request             |
| `401` | Authentication required |
| `403` | Forbidden               |
| `404` | Not Found               |
| `500` | Internal Server Error   |

---

# 2. REST APIs

**REST = Representational State Transfer**

A REST API allows applications to communicate with a server using HTTP.

Think:

> **REST API = A way for applications to communicate with a server**

Example:

```text
Mobile App
    |
    | GET /accounts/123
    ↓
API Server
    |
    ↓
Database
```

The server may return JSON:

```json
{
  "account_id": 123,
  "balance": 1500
}
```

## REST API Example

```text
GET    /users
GET    /users/123
POST   /users
PUT    /users/123
DELETE /users/123
```

These endpoints represent resources and operations.

## API Security

APIs should properly handle:

* Authentication
* Authorization
* Input validation
* Rate limiting
* Access control
* Sensitive data
* Error handling

Important:

> **Being logged in does NOT mean you can access everything.**

Authentication and authorization are different.

---

# 3. Authentication

Authentication answers:

> **"Who are you?"**

It verifies a user's identity.

Examples:

* Username + password
* MFA
* Security keys
* Biometrics

Example:

```text
User
 ↓
Username + Password
 ↓
Authentication System
 ↓
Valid?
 ↓
Authenticated
```

---

# 4. Authorization

Authorization answers:

> **"What are you allowed to do?"**

After a user is authenticated, the application determines what they are allowed to access.

Example:

```text
Alice → Can view her account
Alice → Cannot view Bob's account
Admin → Can manage users
```

## Authentication vs Authorization

| Authentication    | Authorization          |
| ----------------- | ---------------------- |
| Who are you?      | What can you do?       |
| Verifies identity | Determines permissions |
| Password/MFA      | Roles/permissions      |

### Memory trick

> **Authentication = WHO?**
> **Authorization = WHAT?**

---

# 5. Cookies

A **cookie** is a small piece of information that a website stores in your browser.

Think:

> **Cookie = Website remembers something about you**

Cookies can be used for:

* Login sessions
* Preferences
* Tracking
* Authentication

Example:

```http
Set-Cookie: session_id=abc123
```

The browser can then send it back:

```http
Cookie: session_id=abc123
```

### Simple flow

```text
Website
   ↓
"Here's your cookie"
   ↓
Browser stores it
   ↓
Browser sends it back later
```

## Important Cookie Security Flags

### `Secure`

The cookie should only be sent over HTTPS.

### `HttpOnly`

Prevents JavaScript from directly accessing the cookie.

This can help reduce the impact of certain XSS attacks.

### `SameSite`

Controls when cookies are sent with cross-site requests.

Common values:

```text
Strict
Lax
None
```

`SameSite` can help protect against CSRF.

---

# 6. Sessions

A **session** allows a website to remember that you are logged in.

Think:

> **Session = Website remembers that you're logged in**

HTTP itself is stateless, meaning each request is normally independent.

Sessions allow the server to connect multiple requests to the same user.

## Simple Session Flow

```text
You log in
    ↓
Server verifies you
    ↓
Server creates a session
    ↓
Browser gets a session ID
    ↓
Browser stores it in a cookie
    ↓
Browser sends cookie with future requests
    ↓
Server recognizes your session
```

### Cookie vs Session

Think:

> **Cookie = stored in your browser**

> **Session = information the server keeps about your login/state**

They are often used together.

## Session Security

Important protections include:

* HTTPS
* Secure cookies
* HttpOnly cookies
* SameSite cookies
* Session expiration
* Secure session IDs
* Regenerating sessions after login

---

# 7. JWT

**JWT = JSON Web Token**

A JWT is a type of token that can be used to represent information about a user between a client and server.

Think:

> **JWT = Digital pass/token**

Simple flow:

```text
You log in
    ↓
Server verifies you
    ↓
Server gives you a JWT
    ↓
You send JWT with future requests
    ↓
Server checks the JWT
```

A JWT looks something like:

```text
xxxxx.yyyyy.zzzzz
```

A JWT commonly contains:

```text
Header.Payload.Signature
```

## Important

JWTs are generally **encoded, not encrypted**.

That means you should **not put passwords or secrets inside a JWT payload**.

## JWT Security Problems

Problems can occur if an application:

* Doesn't properly verify signatures
* Uses weak signing secrets
* Doesn't check expiration
* Stores tokens insecurely
* Puts sensitive information in the payload

---

# 8. SQL Injection

**SQL Injection (SQLi)** happens when an attacker puts malicious input into a website and that input changes a database query.

Think:

> **SQL Injection = Mess with the database through input**

Basic idea:

```text
User Input
    ↓
Website
    ↓
Database
```

If the website doesn't handle input safely:

```text
Attacker Input
    ↓
Changes SQL Query
    ↓
Database does something unintended
```

Possible consequences:

* Reading data
* Changing data
* Deleting data
* Bypassing authentication
* Accessing sensitive information

## Prevention

Use **parameterized queries/prepared statements**.

Don't build SQL by directly combining SQL and user input.

```text
Unsafe:
SQL + user input

Safer:
SQL statement + parameter
```

Other defenses include:

* Input validation
* Least-privilege database accounts
* Secure ORM usage
* Proper error handling

---

# 9. XSS

**XSS = Cross-Site Scripting**

XSS happens when an attacker gets their own code to run in another user's browser.

Think:

> **XSS = Make code run in someone's browser**

Simple flow:

```text
Attacker
   ↓
Malicious input
   ↓
Website
   ↓
Victim visits website
   ↓
Code runs in victim's browser
```

Possible consequences include:

* Stealing information
* Performing actions as the victim
* Changing what the victim sees

## Types of XSS

### Stored XSS

Malicious content is saved by the website.

```text
Attacker
   ↓
Website
   ↓
Database
   ↓
Victim views page
   ↓
Code executes
```

### Reflected XSS

Malicious input is immediately returned by the server.

```text
Attacker
   ↓
Malicious request
   ↓
Server
   ↓
Response
   ↓
Victim's browser
```

### DOM-Based XSS

The vulnerability happens in client-side JavaScript when unsafe input is inserted into a webpage.

## XSS Prevention

Common defenses include:

* Output encoding
* Input validation
* Content Security Policy (CSP)
* Avoiding unsafe DOM APIs
* Properly configured cookies

---

# 10. CSRF

**CSRF = Cross-Site Request Forgery**

CSRF tricks a user's browser into making a request that the user **didn't intend to make**.

Think:

> **CSRF = Make the victim's browser do something**

Example:

```text
User is logged into a website
        ↓
User visits attacker's website
        ↓
Attacker tricks the browser
        ↓
Browser sends request to the first website
        ↓
Unwanted action happens
```

The problem is that the website may trust the request because the user's browser automatically includes authentication information such as cookies.

## CSRF Prevention

Common defenses include:

* CSRF tokens
* SameSite cookies
* Checking request origin
* Re-authentication for sensitive actions

---

# 11. IDOR

**IDOR = Insecure Direct Object Reference**

IDOR happens when a user can change an ID in a request and access **someone else's information**.

Think:

> **IDOR = Change the ID → access something I shouldn't**

Example:

You access:

```text
/account/123
```

You change it to:

```text
/account/124
```

If you can now see another person's account:

```text
Your account
    ↓
/account/123

Change ID
    ↓
/account/124
    ↓
Someone else's account
```

That's an access control problem.

## Why IDOR Happens

The application checks:

```text
"Does this account exist?"
```

but fails to check:

```text
"Is this user allowed to access this account?"
```

## Prevention

The server must always perform an authorization check:

```text
Request
   ↓
Authenticate user
   ↓
Identify requested object
   ↓
Check authorization
   ↓
Allow or deny
```

---

# 12. SSRF

**SSRF = Server-Side Request Forgery**

SSRF happens when an attacker tricks a **server** into making a request that the attacker shouldn't be able to make directly.

Think:

> **SSRF = Make the server go somewhere for me**

Example:

```text
Attacker
   ↓
Website Server
   ↓
Internal Resource
```

For example, an application might allow users to provide a URL:

```text
https://example.com/image.jpg
```

The server then downloads the image.

If the application doesn't properly restrict where the server can connect, an attacker may manipulate the URL and make the server request an unintended resource.

## Why SSRF Is Dangerous

SSRF can potentially expose:

* Internal services
* Internal APIs
* Cloud metadata services
* Internal network resources

## Prevention

Defenses can include:

* Allowlisting destinations
* Validating URLs
* Restricting outbound network access
* Blocking private/internal destinations where appropriate
* Network segmentation
* Carefully handling redirects

### Easy Comparison

```text
CSRF
→ Make the VICTIM'S BROWSER do something

SSRF
→ Make the SERVER do something
```

---

# 13. OWASP Top 10

**OWASP Top 10** is a list of major types of web application security problems.

Think:

> **OWASP Top 10 = Big list of web security problems you should know**

The 2021 edition contains:

| #   | Category                                   |
| --- | ------------------------------------------ |
| A01 | Broken Access Control                      |
| A02 | Cryptographic Failures                     |
| A03 | Injection                                  |
| A04 | Insecure Design                            |
| A05 | Security Misconfiguration                  |
| A06 | Vulnerable and Outdated Components         |
| A07 | Identification and Authentication Failures |
| A08 | Software and Data Integrity Failures       |
| A09 | Security Logging and Monitoring Failures   |
| A10 | Server-Side Request Forgery (SSRF)         |

## A01 — Broken Access Control

Users can access things they shouldn't.

Example:

```text
Normal user → accesses admin page
```

Think:

> **Can this user access this resource?**

---

## A02 — Cryptographic Failures

Sensitive information isn't properly protected.

Examples:

* Weak encryption
* Sensitive data sent without HTTPS
* Poor key management
* Passwords stored improperly

Think:

> **Is sensitive data protected?**

---

## A03 — Injection

User input changes a command or query.

Example:

```text
SQL Injection
```

Think:

> **Can user input change what the application does?**

---

## A04 — Insecure Design

Security wasn't properly considered when designing the application.

Examples:

* No rate limiting
* Unsafe workflows
* Missing security controls

Think:

> **Was security considered during design?**

---

## A05 — Security Misconfiguration

A system is configured insecurely.

Examples:

* Default passwords
* Debug mode enabled
* Unnecessary services
* Excessive permissions

Think:

> **Is the system configured securely?**

---

## A06 — Vulnerable and Outdated Components

The application uses software with known security vulnerabilities.

Examples:

* Old libraries
* Vulnerable frameworks
* Unsupported software

Think:

> **Are we using vulnerable software?**

---

## A07 — Identification and Authentication Failures

Problems with verifying users or managing authentication.

Examples:

* Weak passwords
* Poor session management
* Authentication bypasses

Think:

> **Can the application properly verify who the user is?**

---

## A08 — Software and Data Integrity Failures

The application doesn't properly verify the integrity of software or data.

Examples:

* Untrusted dependencies
* Insecure software updates
* Compromised build processes

Think:

> **Can we trust the software and data?**

---

## A09 — Security Logging and Monitoring Failures

Security events aren't properly recorded or monitored.

Examples:

* Failed logins aren't logged
* No alerts for suspicious activity
* Logs aren't monitored

Think:

> **Would we know if an attack happened?**

---

## A10 — SSRF

An attacker tricks the server into making unintended requests.

Think:

> **Can an attacker control where the server sends requests?**

---

# 14. Important Relationships

These concepts are connected.

## Authentication → Authorization

```text
Authentication
      ↓
Who are you?
      ↓
Authorization
      ↓
What can you access?
```

---

## Cookies → Sessions

```text
User logs in
      ↓
Server creates session
      ↓
Session ID
      ↓
Cookie in browser
      ↓
Browser sends cookie
      ↓
Server recognizes user
```

---

## User Input → Vulnerabilities

User input can travel through many parts of an application:

```text
User Input
     ↓
Application
     ↓
 ┌───────────────┐
 ↓       ↓       ↓
Database  Web    Server
 ↓        Page    Requests
SQLi       ↓       ↓
          XSS     SSRF
```

---

## Object IDs → IDOR

```text
User
  ↓
Object ID
  ↓
Server
  ↓
Authorization check?
  ↓
Allow / Deny
```

If the authorization check is missing:

```text
User
  ↓
Change ID
  ↓
Access someone else's data
  ↓
IDOR
```

---

# 15. Quick Memory Table

| **Concept**    | **Think**                                             |
| -------------- | ----------------------------------------------------- |
| HTTP           | **How does the browser communicate with the server?** |
| REST API       | **How do applications communicate with a server?**    |
| Authentication | **Who are you?**                                      |
| Authorization  | **What are you allowed to do?**                       |
| Cookie         | **Website remembers something in my browser**         |
| Session        | **Website remembers I'm logged in**                   |
| JWT            | **Digital pass/token**                                |
| SQL Injection  | **Mess with the database through input**              |
| XSS            | **Make code run in someone's browser**                |
| CSRF           | **Make someone's browser do something**               |
| IDOR           | **Change an ID → access something I shouldn't**       |
| SSRF           | **Make the server go somewhere for me**               |
| OWASP Top 10   | **Major web security problems to know**               |

---

# 16. The Ones You Should NOT Mix Up

## XSS

```text
Attacker
   ↓
Code
   ↓
Victim's BROWSER
```

> **XSS = Code runs in the browser**

---

## CSRF

```text
Attacker
   ↓
Tricks
   ↓
Victim's BROWSER
   ↓
Unwanted action
```

> **CSRF = Browser does something the user didn't intend**

---

## SSRF

```text
Attacker
   ↓
Tricks
   ↓
SERVER
   ↓
Unwanted request
```

> **SSRF = Server makes a request it shouldn't**

---

## IDOR

```text
User
   ↓
Changes ID
   ↓
Someone else's data
```

> **IDOR = Access something you shouldn't**

---

# 17. Cybersecurity Mental Model

When looking at a web application, ask:

### 1. Who is the user?

```text
Authentication
```

### 2. What are they allowed to access?

```text
Authorization
```

### 3. How does the application remember them?

```text
Cookies
Sessions
JWT
```

### 4. What can the user control?

```text
Forms
URLs
Headers
API parameters
Files
```

### 5. Where does that input go?

```text
Database
    ↓
SQL Injection

Web Page
    ↓
XSS

Server-side request
    ↓
SSRF

Object ID
    ↓
IDOR
```

### 6. Can another website make the user's browser do something?

```text
CSRF
```

---

# Key Takeaways

```text
HTTP
    ↓
Browser ↔ Server

REST API
    ↓
Application ↔ API

Authentication
    ↓
Who are you?

Authorization
    ↓
What can you access?

Cookies / Sessions / JWT
    ↓
How does the application remember/identify you?

User Input
    ↓
Must be handled safely
    ↓
SQL Injection
XSS
SSRF
IDOR
CSRF

OWASP Top 10
    ↓
Major categories of web application security risks
```
