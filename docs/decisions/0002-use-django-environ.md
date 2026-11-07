# ADR 0002: Use django-environ for environment configuration

## Status
Accepted

## Context
Secrets (SECRET_KEY, database credentials) and environment-specific settings
(DEBUG, ALLOWED_HOSTS) must not be committed to GitHub, and must differ between
local development and production.

## Decision
Use django-environ to read settings from environment variables, with a `.env`
file for local development only (listed in `.gitignore`).

## Alternatives considered
- python-dotenv: only loads the `.env` file; no type conversion or DATABASE_URL parsing.
- python-decouple: similar features, but not Django-focused.
- pydantic-settings: suited to FastAPI/Pydantic projects; this project doesn't use Pydantic.

## Consequences
- Type conversion built in (e.g. `env.bool("DEBUG")`), so no string-to-bool bugs.
- A single `DATABASE_URL` configures the database.
- Production reads real environment variables; no `.env` file on the server.
- One extra dependency; a committed `.env.example` documents the required variables.
