
# ✅ CI Setup Checklist (SkilledUp.Life)

> **Note:** We use a 'Module > Feature > User Story > Task' structure (Modules = Epics). This checklist covers both frontend (Vue) and backend (Laravel) CI setup, plus cross-repo test tracking.

## 📝 Test Coverage Tracker Setup
- [x] Create Google Sheet for test coverage tracker (Title: "Test Coverage Tracker – SkilledUp.Life Modules")
- [ ] Add test coverage tracker link to frontend README
- [ ] Add test coverage tracker link to backend README

# ✅ CI Setup — Frontend (Vue)

## ✅ 1. Linting & Formatting Setup

- [ ] Install Prettier (if not installed):
  ```bash
  npm install --save-dev prettier
  ```
- [x] Check if Prettier is installed.
- [ ] Create a Prettier config file (e.g. `.prettierrc`).
- [ ] Add Prettier script to `package.json`:
  ```json
  "format": "prettier --check src/"
  ```
- [ ] Install ESLint (if not installed):
  ```bash
  npm install --save-dev eslint
  npx eslint --init
  ```
- [ ] Create an ESLint config file (e.g. `.eslintrc.js` or `.eslintrc.json`).
- [ ] Add ESLint script to `package.json`:
  ```json
  "lint": "eslint src/ --ext .js,.vue"
  ```
- [ ] Commit `.prettierrc`, `.eslintrc.*`, and updated `package.json`.
- [ ] Run `npm run format` and `npm run lint` locally to verify setup.
- [ ] Confirm both scripts work and catch issues as expected.

## ✅ 2. Ensure Lock File Exists

- [ ] Check if `frontend/package-lock.json` exists
- [ ] If not:
  - Run: `npm install`
  - Commit the generated `package-lock.json` to the repo

## ✅ 3. Setup Workflow

- [ ] Create this path:
  ```
  frontend/.github/workflows/ci.yml
  ```
- [ ] Add the lint-only version of `ci.yml` initially (with echo placeholders for other jobs)
- [ ] Confirm it's committed to the correct path

## ✅ 4. Trigger Workflow at Least Once

- [ ] Open a PR from a test branch → `dev` or `main`
- [ ] Confirm `CI Pipeline / Lint Frontend` shows up on the PR

## ✅ 5. Enable Status Check (Admin Only)

- [ ] Ask PO to enable status check for:
  - `CI Pipeline / Lint Frontend`
- [ ] Path: GitHub → Settings → Branches → Protection Rules

## ✅ 6. Prepare Test Files

- [ ] Collect existing Vue unit + E2E tests from devs
- [ ] Structure:
  ```
  frontend/tests/unit/
  frontend/tests/e2e/
  ```
- [ ] Replace placeholder `echo` in `ci.yml` with:
  ```bash
  npm run test:unit
  npx playwright test
  ```
- [ ] Run tests locally to verify setup

---

# ✅ CI Setup — Backend (Laravel)

## ✅ 1. Inspect for Composer or NPM

- [ ] Check if `composer.json` and `composer.lock` exist
- [ ] If not:
  - Run: `composer install`
  - Commit the generated `composer.lock`

- [ ] Also check if `package.json` is used (optional — for frontend assets)

## ✅ 2. Setup Workflow

- [ ] Path must be:
  ```
  backend/.github/workflows/ci.yml
  ```
- [ ] Use a basic version with:
  - Lint check (if PHP linter installed)
  - Unit test placeholder (Laravel)

## ✅ 3. Trigger the Workflow

- [ ] Open PR from any branch to `dev` or `main`
- [ ] Confirm `CI Pipeline / Backend Tests` (or similar name) shows up in GitHub Checks

## ✅ 4. Enable Status Checks (Admin Only)

- [ ] Ask PO to enable status checks:
  - `CI Pipeline / Backend Tests`

## ✅ 5. Prepare Tests

- [ ] Ensure Laravel tests are in:
  ```
  backend/tests/
  ```
- [ ] Replace placeholder in `ci.yml`:
  ```bash
  php artisan test
  ```
- [ ] Run tests locally to verify setup
