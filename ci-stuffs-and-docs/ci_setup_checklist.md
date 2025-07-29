# ✅ CI Setup Checklist (SkilledUp.Life)

> **Note:** This checklist covers both frontend (Vue) and backend (Laravel) CI setup, plus cross-repo test tracking.

## 📝 Test Coverage Tracker Setup

- [x] Create Google Sheet for test coverage tracker (Title: "Test Coverage Tracker – SkilledUp.Life Modules")
- [ ] Add test coverage tracker link to frontend README
- [ ] Add test coverage tracker link to backend README

# ✅ CI Setup — Frontend (Vue)

## ✅ 1. Linting & Formatting Setup

- [x] Prettier is installed.
- [x] Create a Prettier config file (e.g. `.prettierrc`).
- [ ] Add Prettier script to `package.json`:
  ```json
  "scripts": {
    "lint": "eslint src/ tests/ *.js --ext .js,.vue",
    "format": "prettier --check src/ tests/ *.js"
  }
  ```
  Update `package.json` and commit it to ensure CI and dev workflows are consistent.
  Modify paths as needed if your source files are in folders other than `src/` or `tests/`.
- [ ] Install ESLint (if not installed):
  ```bash
  npm install --save-dev eslint
  npx eslint --init
  ```
- [ ] Create an ESLint config file (e.g. `.eslintrc.js` or `.eslintrc.json`).
- [ ] Commit `.prettierrc`, `.eslintrc.*`, and updated `package.json`.
- [ ] Run `npm run format` and `npm run lint` locally to verify setup.
- [ ] Confirm both scripts work and catch issues as expected.

## ✅ 2. Dev Setup Reminder

📝 **Dev Setup Reminder:**
After ESLint and Prettier are added to the repo, each developer must run:

```bash
npm install
```

This ensures all linting/formatting tools are installed locally via `package-lock.json`.

## ✅ 3. Ensure Lock File Exists / Update After Dependency Changes

- [x] `frontend/package-lock.json` exists.
- [ ] After installing ESLint or any new dependency, run:

  ```bash
  npm install
  ```

  - Commit the updated `package-lock.json` to the repo if it changes.

## ✅ 4. Setup Workflow

- [ ] Create this path:
  ```
  frontend/.github/workflows/ci-frontend.yml
  ```
- [ ] Add the lint-only version of `ci-frontend.yml` initially (with echo placeholders for other jobs)
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
- [ ] Replace placeholder `echo` in `ci-frontend.yml` with:
  ```bash
  npm run test:unit
  npx playwright test
  ```
- [ ] Run tests locally to verify setup

## ✅ 6. Clarify ESLint/Prettier Roles vs CI + Dev Workflow

**Clarification for team:**

- ESLint and Prettier enforce code standards _locally and in CI_.
- Developers should run `npm run lint` and `npm run format` before **every commit**.
- If skipped, CI will catch errors on PR and block the merge.

**Typical CI error output:**

```
Error:  Unexpected console statement. (no-console)
✖ 1 problem (1 error, 0 warnings)
```

To fix: Run `npm run lint`, follow the hints, and recommit changes.

## ✅ 7. Vue-Specific ESLint + Prettier Rules

**Use this base ESLint config:**

`.eslintrc.js`:

```js
module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
    es2021: true,
  },
  extends: ['eslint:recommended', 'plugin:vue/vue3-essential', 'prettier'],
  rules: {
    'no-console': 'warn',
    'no-unused-vars': 'warn',
    'vue/no-mutating-props': 'error',
    'vue/require-default-prop': 'warn',
    'vue/component-name-in-template-casing': ['error', 'PascalCase'],
  },
}
```

**And add `.prettierrc` config:**

```json
{
  "semi": false,
  "singleQuote": true,
  "printWidth": 100,
  "trailingComma": "es5"
}
```

These rules encourage readable, maintainable Vue code without frustrating devs.

## ✅ 8. Enhanced CI Configuration

- [ ] Update CI config to include detailed lint/format checking:

  ```yaml
  - name: Run Lint and Format Check
    run: npm run lint && npm run format

  - name: Show Unformatted Files
    run: prettier --list-different src/ tests/ *.js
  ```

  This flags files that require formatting without auto-fixing in CI—promotes developer accountability.

## ✅ 9. README Additions for Dev Expectations

📋 **Workflow Expectations:**

- Always run `npm run lint` and `npm run format` before submitting a PR.
- Use ESLint and Prettier plugins in your IDE (e.g. VS Code) to catch issues early.
- CI will reject unformatted or error-prone code during PR reviews.

## ✅ 10. Note on Husky + lint-staged (Optional Extension)

🔒 **Optional Enhancement: Pre-commit linting (recommended for growing teams)**
Use `husky` + `lint-staged` to automatically run checks before commits.

- Benefits: Prevents errors _before_ CI review.
- Considered industry standard by many teams.

**To install:**

```bash
npm install husky lint-staged --save-dev
npx husky install
```

**Add this to `package.json`:**

```json
"lint-staged": {
  "*.{js,vue}": ["eslint", "prettier --check"]
}
```

Enable only when team size or merge issues make it worthwhile.

---

## 🧩 Strategic Clarifications

### 💡 Why CI doesn't auto-fix (and shouldn't):

Auto-fixing in CI creates Git discrepancies. Developers should fix **locally**, learn from errors, and recommit. CI ensures accountability without intruding on authoring flow. That's the "gentle enforcement."

### 🎯 Teaching vs Protecting Codebase

You can absolutely achieve both:

- **Protect** with ESLint/Prettier + CI blocking
- **Teach** via transparent errors and README culture tips

Even volunteers can benefit from learning better coding habits through your tooling. It adds value to their time and respects the codebase.

### 🧱 Defining & Communicating Standards

1. **Define:** Codify in ESLint rules and Prettier config. That's your technical baseline.
2. **Communicate:** Add usage notes in the README, onboarding doc, and checklist steps.
3. **Enforce (automate):** Via CI pipeline (already in place) and optionally via Husky.
4. **Guide team:** Offer Vue linting rules that reflect clean component design and prop management.

If Asinsala or Christian want to extend this later (e.g. enforce scoped styles or test coverage), you'll already have the framework to plug those in.

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
  backend/.github/workflows/ci-backend.yml
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
