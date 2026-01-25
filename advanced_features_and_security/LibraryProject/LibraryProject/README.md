- The user model has four permissions can_view, can_edit, can_delete, and can_create.
- Three groups of users have been created, Editors, viewoers and admins.

## Security Measures Implemented

- DEBUG disabled to prevent sensitive information leakage
- CSRF protection enabled using `{% csrf_token %}` in all forms
- Django ORM used exclusively to prevent SQL injection
- Secure cookies enforced using HTTPS-only flags
- Browser security headers enabled (XSS filter, no-sniff, frame denial)
- Content Security Policy implemented using django-csp middleware
