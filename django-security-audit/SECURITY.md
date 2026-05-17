# Security Audit — Product Review App

## Finding 1: Secret key exposed in settings.py

*Risk:* If the secret key is exposed, attackers may forge session cookies or impersonate users.

*Fix:* Moved SECRET_KEY into environment variables using os.environ.get().

*Location:* myproject/settings.py


## Finding 2: Missing CSRF protection risk

*Risk:* Attackers could submit forms on behalf of authenticated users.

*Fix:* Added {% csrf_token %} to all POST forms.

*Location:* reviews/templates/reviews/index.html


## Finding 3: Potential XSS vulnerability

*Risk:* User-generated content could execute malicious JavaScript in another user's browser.

*Fix:* Used Django auto-escaped {{ review.content }} instead of the |safe filter.

*Location:* reviews/templates/reviews/index.html


## Finding 4: SQL Injection prevention

*Risk:* Raw SQL string concatenation can allow attackers to manipulate database queries.

*Fix:* Used Django ORM queries instead of raw SQL queries.

*Location:* reviews/views.py


## Finding 5: Added caching

*Risk:* Without caching, repeated database queries may reduce performance under heavy traffic.

*Fix:* Added Django @cache_page decorator with a 15-minute timeout.

*Location:* reviews/views.py