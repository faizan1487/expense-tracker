# ADR 0002: Use rest_framework_simplejwt for authentication

## Status
Accepted

## Context
Need an auth system which makes each request stateless, nothing should be stored on server and any instane of the app should be able to authenticate the user

## Decision
Use rest_framework_simplejwt it provides built in views to handle login and use rest_framework_simplejwt.token_blacklist to blacklist tokens when users log out

## Alternatives considered
- DRF SessionAuthentication: stores sessions server-side and relies on cookies; stateful.
- DRF TokenAuthentication: one permanent token per user, looked up in the database on every request; stateful and never expires.
- django-rest-knox: expiring, per-device tokens, but still stored and checked in the database.
- Hand-rolled JWT with PyJWT: full control, but we'd write refresh, expiry and blacklisting ourselves.
- django-oauth-toolkit: full OAuth2 provider; too heavy since no third parties need access.

## Consequences
- Any app instance verifies access tokens with the secret key alone; no database lookup.
- Logout is not instant: blacklisting only blocks the refresh token, so the access token stays valid until it expires; keep its lifetime short (e.g. 5–15 minutes).
- The blacklist is stored in the database, so logout and refresh are not fully stateless.
- Tokens are stored by the frontend, so XSS must be guarded against.