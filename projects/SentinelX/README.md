# SentinelX

SentinelX is a backend authentication project built with Python, FastAPI, PostgreSQL, SQLAlchemy, JWT, and bcrypt.

## Features

* User registration
* Secure password hashing with bcrypt
* User login with JWT access tokens
* Protected user profile endpoint
* Role-based admin authorization
* Logout through client-side JWT disposal
* REST API testing with Postman

## Tech Stack

* **Python**
* **FastAPI**
* **PostgreSQL**
* **SQLAlchemy**
* **JWT**
* **bcrypt**
* **Postman**

## API Endpoints

| Method | Endpoint    | Description                               | Authentication            |
| ------ | ----------- | ----------------------------------------- | ------------------------- |
| GET    | `/`         | Check that SentinelX is running           | None                      |
| POST   | `/register` | Register a new user                       | None                      |
| POST   | `/login`    | Authenticate a user and receive a JWT     | None                      |
| GET    | `/profile`  | Retrieve the authenticated user's profile | JWT required              |
| GET    | `/admin`    | Access the admin area                     | JWT + admin role required |
| POST   | `/logout`   | Log out by discarding the client-side JWT | JWT required              |

## Authentication

Passwords are hashed with **bcrypt** before being stored in PostgreSQL. During login, the submitted password is verified against the stored bcrypt hash.

Successful login generates a **JWT access token** that is used to access protected endpoints such as `/profile` and `/admin`.

Admin authorization checks the user's `is_admin` role before allowing access to the `/admin` endpoint.

The logout endpoint uses a stateless JWT approach: the client discards its access token. Tokens are not server-side blacklisted and remain valid until they expire if they are still possessed by a client.

## Testing

API functionality was tested using **Postman**, including:

* Successful user registration
* Successful login
* Incorrect password rejection
* Authenticated profile access
* Logout
* Rejection of unauthenticated requests
* Rejection of non-admin users attempting to access `/admin`

The PostgreSQL database was also checked to confirm that user passwords are stored as bcrypt hashes rather than plaintext passwords.

## Running the Project

Activate the virtual environment:

```bash
source venv/bin/activate
```

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The API runs locally at:

```text
http://127.0.0.1:8000
```

FastAPI's interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```
