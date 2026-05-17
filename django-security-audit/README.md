# Product Review App

A Django web application built for practicing web security and scalability concepts.

## Features

- Submit product reviews
- Store reviews in a database
- Display user-generated reviews
- CSRF protection
- XSS-safe rendering
- ORM-based database queries
- Cached homepage

## Technologies Used

- Python
- Django
- SQLite

## Security Features

### CSRF Protection

All POST forms include Django's `{% csrf_token %}` to prevent cross-site request forgery attacks.

### XSS Prevention

User-generated content is rendered using Django auto-escaped template syntax:

```html
{{ review.content }}
```

The application does not use the unsafe `|safe` filter for untrusted user content.

### SQL Injection Prevention

The project uses Django ORM queries instead of raw SQL string concatenation.

Example:

```python
Review.objects.all()
```

Django ORM automatically escapes user input and reduces SQL injection risk.

### Environment Variables

Sensitive configuration values such as `SECRET_KEY` are loaded from environment variables instead of being hardcoded into `settings.py`.

## Caching

The homepage view uses Django's `@cache_page` decorator with a 15-minute timeout.

This reduces repeated database queries and improves performance.

Potential risk: newly submitted reviews may not appear immediately until the cache expires.

## Scalability Design

If this application needed to support 10x more users, I would first use vertical scaling by upgrading the server CPU and memory because it is the fastest short-term solution.

As traffic increased further, I would move to horizontal scaling using multiple Django application servers behind a load balancer such as Nginx.

Session data should be stored using a shared system such as Redis or database-backed sessions so users remain logged in even when requests are routed to different servers.

For the database layer, replication would likely be added first to distribute read queries across multiple replicas. If the dataset became extremely large, partitioning or sharding could also be considered.

## Running the Project

```bash
python manage.py runserver
```