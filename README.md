# ClipLink — Scalable URL Compression Platform

ClipLink is a high-performance URL shortening system built using Flask, Redis, and SQLAlchemy. It demonstrates scalable backend design with caching, rate limiting, and analytics — simulating real-world systems like Bitly.

---

## Overview

ClipLink is designed to efficiently shorten long URLs and provide fast redirection using caching and optimized database lookups. The system ensures high performance and reliability through Redis-based caching and rate limiting.

---

## Architecture

The system follows a scalable backend architecture:

1. User submits a long URL via API
2. System generates a unique short code
3. URL mapping is stored in the database
4. Frequently accessed URLs are cached in Redis
5. On access, user is redirected instantly
6. Click analytics are tracked
7. Rate limiting prevents abuse

---

## Features

* URL shortening and redirection
* Redis caching for fast lookups
* Rate limiting per user/IP
* Click analytics tracking
* REST API endpoints
* Scalable and efficient backend design

---

## Tech Stack

* Backend: Python (Flask)
* Database: SQLite (SQLAlchemy ORM)
* Cache: Redis
* Rate Limiting: Redis-based
* DevOps: Docker (for Redis setup)

---

## Project Structure

```id="r1"
cliplink/
│
├── api/
│   └── app.py
│
├── services/
│   ├── shortener.py
│   ├── analytics.py
│   └── rate_limiter.py
│
├── database/
│   └── models.py
│
├── cache/
│   └── redis_client.py
│
├── utils/
│   └── encoder.py
│
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## Installation & Setup

### Step 1: Clone Repository

```id="r2"
git clone https://github.com/your-username/cliplink.git
cd cliplink
```

### Step 2: Install Dependencies

```id="r3"
pip install -r requirements.txt
```

---

## 🚀 How to Run

### Step 1

```id="r4"
pip install -r requirements.txt
```

### Step 2

```id="r5"
docker-compose up
```

### Step 3

```id="r6"
python api/app.py
```

---

## Test API

### Shorten URL

POST http://localhost:5000/shorten

```id="r7"
{
  "url": "https://google.com"
}
```

---

### Redirect

Open in browser:

```id="r8"
http://localhost:5000/abc123
```

---

### Analytics

GET:

```id="r9"
http://localhost:5000/stats/abc123
```

---

## API Endpoints

* POST /shorten → Create short URL
* GET /<short_code> → Redirect to original URL
* GET /stats/<short_code> → Get analytics

---

## Rate Limiting

* Limits requests per IP using Redis
* Prevents system abuse and ensures fair usage

---

## Analytics

Tracks:

* Total click count per URL
* Original URL mapping

---

## Future Enhancements

* Custom short URLs
* Expiry-based links
* User authentication
* Dashboard for analytics
* Deployment on AWS

---

## Why This Project Matters

This project demonstrates:

* System design fundamentals
* Caching strategies using Redis
* Rate limiting techniques
* Backend scalability principles
* Real-world URL shortening architecture

---

## Author

Lipsa Pattanaik
ITER, SOA University

---

## License

This project is intended for educational and portfolio purposes.
