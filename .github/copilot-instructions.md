# Copilot instructions for this repository

Purpose: Provide concise, actionable guidance so an AI coding agent can be immediately productive in this repo.
(Replace placeholders below with concrete details from the codebase.)

---

## 1) Big picture (short, 1–2 paragraphs) 🔧
- What to fill in: short architecture summary (e.g., frontend /backend /infra dirs), primary runtime(s), and the "why" behind major structure choices.
- Example placeholder: `"Monorepo: /api (Node/Express), /web (React), infra in /deploy"` — replace with your repo details.

## 2) Local dev & commands (exact, copyable commands) ▶️
- Add the exact commands to run, build, test, and lint locally, e.g.:
  - Install deps: `npm ci` (or `pip install -r requirements.txt`)
  - Start dev server: `pnpm --filter web dev` or `python -m uvicorn api.main:app --reload`
  - Run tests: `npm test` or `pytest tests/`
  - Run linter/format: `npm run lint` / `prettier --check .`
- If the repo uses Docker, include the relevant compose commands (e.g., `docker-compose up --build -d`).

> NOTE: The agent should always prefer the project-specific commands listed here over generic guesses.

## 3) CI / test expectations ✅
- File locations: add where CI config lives (e.g., `.github/workflows/ci.yml`, `azure-pipelines.yml`).
- What a passing run means in this project (lint + unit tests + build). If there are flaky tests or long-running integration tests, document them and mark which ones can be skipped for quick iterations.

## 4) Project-specific conventions & patterns ✨
- Include naming, folder-layout rules, and code-style hooks (e.g., `.eslintrc`, `.prettierrc`, `pyproject.toml`), and any deviations from common patterns (e.g., tests colocated vs in `/tests`).
- Point to canonical examples in the repo (add file paths): e.g., `See /api/routes/user.py for request/response pattern`.

## 5) Integration points & secrets 🔌
- List external services and how to run against them locally (mock/stub services or necessary env vars). E.g., `Uses SQS, Postgres, and Stripe; local dev uses LocalStack and a dockerized Postgres at PORT 5432`.
- Where to find infra-as-code or secret placeholders (e.g., `infra/terraform` or `.env.example`).

## 6) Data flows & contracts 📡
- If there are API contracts (OpenAPI / protobuf / GraphQL schema), note their paths and canonical files (e.g., `/api/openapi.yaml` or `/proto/*.proto`).
- Describe high-level event flows (producer → bus → consumer) and point to files that implement them.

## 7) Typical change & review workflow 🧭
- Preferred branching strategy and PR checklist items to verify (add repository specifics): tests, linter, changelog, update schema/migrations.
- When to open a draft PR vs full PR and how to signal maintainers (e.g., labels to apply).

## 8) What the agent should not do 🚫
- Do not push directly to `main`/`master`. Always open a PR.
- Avoid making credentials/secret changes — instead add placeholders and document required env variables.
- Do not change versioning/release pipelines without maintainers’ approval.

## 9) Example tasks an agent can safely perform first 🟢
- Run test suite locally and fix failing unit tests with clear human-readable commit messages.
- Add small, self-contained refactors in a single package/module; include tests and update docs.
- Add missing docs/comments in critical modules (point to files to update).

## 10) What I couldn't infer (fill these in) ❗
- Local DB setup and sample seed data
- Exact commands to run the app in dev/prod
- Key maintainers / Slack/GitHub handles for quick questions

---

If this template looks good, please fill the placeholders with actual commands and a few canonical file examples (paths) from the repo. If you want, I can re-run a scan after you add repo files and then update this file to include concrete examples and verify commands. 

Feedback request: Are there any repository-specific constraints or sensitive directories I should call out (e.g., a private mono-repo, constrained CI minutes, or special deploy windows)? Please reply with those and I'll update the instructions.