# ✅ Frontend CI Setup Checklist (SkilledUp.Life)

> **Note:** This checklist covers frontend (Vue) CI setup with ESLint, Prettier, and future testing integration.

## 🚀 SHORT VERSION - Quick Implementation

### 📁 New Files & Folders to Create
- `.github/workflows/ci-frontend.yml` - GitHub Actions workflow
- `.github/ci-shared/prettier-config/prettier.shared.config.js` - Shared Prettier config
- `.github/ci-shared/eslint-config/eslint.vue.config.js` - Shared ESLint config
- `.github/ci-shared/test-config/jest.vue.config.js` - Shared Jest config (future use)
- `.eslintrc.js` - ESLint configuration (extends shared config)
- `.prettierrc.json` - Prettier configuration (extends shared config)
- `tests/unit/` - Unit test directory
- `tests/e2e/` - E2E test directory

### 🔧 Files to Modify
- `package.json` - Add lint/format scripts

**For developers who want to get CI running in 5 minutes:**

1. **Copy workflow template:**
   ```bash
   cp ci-structure/workflow-templates/ci-frontend.yml .github/workflows/
   ```

2. **Install ESLint:**
   ```bash
   npm install --save-dev eslint eslint-plugin-vue @vue/eslint-config-prettier prettier
   ```

3. **Copy config files:**
   ```bash
   cp ci-structure/ci-shared/eslint-config/eslint.vue.config.js .github/ci-shared/eslint-config/eslint.vue.config.js
   cp ci-structure/ci-shared/prettier-config/prettier.shared.config.js .github/ci-shared/prettier-config/prettier.shared.config.js
   cp ci-structure/ci-shared/test-config/jest.vue.config.js .github/ci-shared/test-config/jest.vue.config.js
   cp ci-structure/ci-shared/test-config/playwright.config.js .github/ci-shared/test-config/playwright.config.js
   ```

4. **Add scripts to package.json:**
   ```json
   {
     "scripts": {
       "lint": "eslint src/ tests/ *.js --ext .js,.vue",
       "format": "prettier --check src/ tests/ *.js",
       "format:fix": "prettier --write src/ tests/ *.js"
     }
   }
   ```

5. **Create PR → see CI in action!**

---

> **Note:** This checklist covers detailed frontend (Vue) CI setup. For shared principles and quick setup, see [CI Setup Checklist](./ci_setup_checklist.md).

---

## ✅ 1. Linting & Formatting Setup

- [x] Prettier is installed.
- [x] Create a Prettier config file (`.prettierrc.js`).
- [ ] Add Prettier script to `package.json`:
  ```json
  "scripts": {
    "lint": "eslint src/ tests/ *.js --ext .js,.vue",
    "format": "prettier --check src/ tests/ *.js",
    "format:fix": "prettier --write src/ tests/ *.js"
  }
  ```
  Update `package.json` and commit it to ensure CI and dev workflows are consistent.
  Modify paths as needed if your source files are in folders other than `src/` or `tests/`.
- [ ] Install ESLint (if not installed):
  ```bash
  npm install --save-dev eslint eslint-plugin-vue @vue/eslint-config-prettier prettier
  npx eslint --init
  ```
- [ ] Create an ESLint config file (`.eslintrc.js`).
- [ ] Commit `.prettierrc.js`, `.eslintrc.js`, and updated `package.json`.
- [ ] Run `npm run format` and `npm run lint` locally to verify setup.
- [ ] Confirm both scripts work and catch issues as expected.

## ✅ 2. Dev Setup Reminder

📝 **Dev Setup Reminder:**
After ESLint and Prettier are added to the repo, each developer must run:

```bash
npm install
```

This ensures all linting/formatting tools are installed locally via `package-lock.json`.

📦 **Dev Setup Requirement:**
After pulling or cloning the repo, each developer must run:

```bash
npm install
```

This ensures all ESLint and Prettier tools are installed locally.

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
- [ ] Add the baseline CI for style and structure checks version of `workflow-templates/ci-frontend.yml` initially (with echo placeholders for other jobs)
- [ ] Confirm it's committed to the correct path

## ✅ 5. Trigger Workflow at Least Once

- [ ] Open a PR from a test branch → `dev` or `main`
- [ ] Confirm `CI Pipeline / Lint Frontend` shows up on the PR

## ✅ 6. Enable Status Check (Admin Only)

- [ ] Ask PO to enable status check for:
  - `CI Pipeline / Lint Frontend`
- [ ] Path: GitHub → Settings → Branches → Protection Rules

## ✅ 7. Prepare Test Files

- [ ] Collect existing Vue unit + E2E tests from devs
- [ ] Structure:
  ```
  frontend/tests/unit/
  frontend/tests/e2e/
  ```
- [ ] Replace placeholder `echo` in `workflow-templates/ci-frontend.yml` with:
  ```bash
  npm run test:unit
  npx playwright test
  ```
- [ ] Run tests locally to verify setup

## ✅ 8. Clarify ESLint/Prettier Roles vs CI + Dev Workflow

**Clarification for team:**

- ESLint and Prettier enforce code standards _locally and in CI_.
- Developers should run `npm run lint` and `npm run format` before **every commit**.
- If skipped, CI will catch errors on PR and block the merge.

## ✅ 9. Baseline CI Explanation

**Basic Static Analysis CI:**
- Includes ESLint for code quality and error detection
- Includes Prettier for formatting consistency across the codebase
- This is our baseline check before any tests are added
- Ensures all code follows the same style and structure standards

**Typical CI error output:**

```
Error:  Unexpected console statement. (no-console)
✖ 1 problem (1 error, 0 warnings)
```

To fix: Run `npm run lint`, follow the hints, and recommit changes.

## ✅ 10. Vue-Specific ESLint + Prettier Rules

**Use the provided config files:**
- ESLint config: [`ci-structure/eslint-config/.eslintrc.js`](../eslint-config/.eslintrc.js)
- Prettier config: [`ci-structure/ci-shared/prettier-config/prettier.shared.config.js`](../ci-shared/prettier-config/prettier.shared.config.js)

These rules encourage readable, maintainable Vue code without frustrating devs.

## ✅ 11. Enhanced CI Configuration

- [ ] Update CI config to include detailed lint/format checking:

  ```yaml
  - name: Run Lint and Format Check
    run: npm run lint && npm run format

  - name: Show Unformatted Files
    run: prettier --list-different src/ tests/ *.js
  ```

  This flags files that require formatting without auto-fixing in CI—promotes developer accountability.

## ✅ 12. README Additions for Dev Expectations

📋 **Workflow Expectations:**

- Always run `npm run lint` and `npm run format` before submitting a PR.
- Use ESLint and Prettier plugins in your IDE (e.g. VS Code) to catch issues early.
- CI will reject unformatted or error-prone code during PR reviews.

## ✅ 13. Rollback Strategy

**Before implementing CI changes:**
- [ ] Document current working state before CI changes
- [ ] Create a feature branch for CI implementation
- [ ] Test CI on the feature branch first
- [ ] Have a "disable CI" option for emergency fixes

**Branch-based testing approach:**
- Create a `ci-implementation` branch
- Test the entire workflow including PRs on this branch
- Only merge to main after thorough testing
- This allows full testing without affecting production development

## ✅ 14. Environment-Specific Configs

**Current Implementation:**
- Single CI workflow for PRs from developers
- Focus on code quality and formatting checks

**Future Implementation (Phase 3):**
- **Development PRs:** Current workflow (linting, formatting, unit tests)
- **Production Merges:** Enhanced workflow with regression testing
- **Deployment Pipeline:** Full E2E testing and security scans

**Approach:**
1. Start with single workflow for all PRs
2. Later add conditional steps based on target branch
3. Implement regression testing for main branch merges

## ✅ 15. Future Enhancements (Optional)

### 🚀 Phase 2: Testing Integration
- [ ] Add Jest/Vitest for unit testing
- [ ] Integrate Playwright for E2E testing
- [ ] Add test coverage reporting

### 🔒 Pre-commit Hooks (Optional)
Use `husky` + `lint-staged` to automatically run checks before commits.

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

### 📊 Metrics & Success Tracking (Optional)
- [ ] CI adoption rate tracking
- [ ] Time to first CI pass metrics
- [ ] Error frequency analysis
- [ ] Test coverage trends

### 🔄 Advanced CI/CD (Future)
- [ ] Dependabot for dependency updates
- [ ] CodeQL for security scanning
- [ ] Deployment previews for PRs
- [ ] Automated release management 