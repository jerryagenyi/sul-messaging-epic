
# ✅ CI Setup Checklist (SkilledUp.Life)

> **Note:** We use a 'Module > Feature > User Story > Task' structure (Modules = Epics). This checklist covers both frontend (Vue) and backend (Laravel) CI setup, plus cross-repo test tracking.

## 📝 Test Coverage Tracker Setup
- [ ] Create Google Sheet for test coverage tracker (Title: "Test Coverage Tracker – SkilledUp.Life Modules")
- [ ] Add test coverage tracker link to frontend README
- [ ] Add test coverage tracker link to backend README

# ✅ CI Setup — Frontend (Vue)

## ✅ 1. Inspect package.json

- [ ] Check if ESLint is installed
- [ ] Check if Prettier is installed
- [ ] Add these scripts to "scripts" in `package.json`:
  ```json
  "lint": "eslint src/ --ext .js,.vue",
  "format": "prettier --check src/"
  ```

---

### 🧰 Option B — Install ESLint (Recommended Long-Term)
If you want to do this right (recommended for professional-grade apps), then:

#### 🛠️ Install ESLint
From the `frontend/` folder, run:
```bash
npm install --save-dev eslint
npx eslint --init
```

**During the interactive setup, choose:**
| Prompt                                      | Recommended Answer                |
|----------------------------------------------|-----------------------------------|
| How would you like to use ESLint?            | To check syntax, find problems... |
| What type of modules does your project use?  | JavaScript modules (import/export)|
| Which framework does your project use?       | Vue.js                            |
| Does your project use TypeScript?            | No (unless you are using it)      |
| Where does your code run?                    | Browser                           |
| How would you like to define a style?        | Use a popular style guide         |
| Which style guide do you want to follow?     | Airbnb (or Standard)              |
| What format for your config file?            | JSON or JavaScript                |
| Install dependencies now?                    | ✅ Yes                            |

This will:
- Install ESLint and any required plugins
- Create `.eslintrc.js` (or `.eslintrc.json`)
- Let you run `npm run lint` if configured

#### ➕ Pros:
- Enforces syntax + logic rules
- Detects potential bugs early

#### 2. Add to package.json Scripts (if not already)
```json
"scripts": {
  "lint": "eslint src/ --ext .js,.vue"
}
```
Adjust `src/` if your code lives elsewhere.

#### 3. Run ESLint Locally
```bash
npm run lint
```
If it returns warnings/errors, ESLint is working. Commit both `.eslintrc.*` and `package.json` (if changed).

#### 4. ✅ You're Ready for CI!
No need to update the ci-frontend.yml since it's already set up to use:
```bash
cd frontend
npm run lint
```

---

#### 🧠 TL;DR — What Should You Do Today?
- Run `npx eslint --init` and accept recommended answers for Vue
- Add `"lint": "eslint src/ --ext .js,.vue"` to package.json
- Run `npm run lint` once
- Commit `.eslintrc.*` and package.json
- CI will now catch lint issues automatically

---

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
