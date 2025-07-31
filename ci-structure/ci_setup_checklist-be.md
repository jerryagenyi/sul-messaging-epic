# ✅ Backend CI Setup Checklist (SkilledUp.Life)

> **Note:** This checklist covers backend (Laravel) CI setup with PHP linting, testing, and future deployment integration.

## 🚀 SHORT VERSION - Quick Implementation

### 📁 New Files & Folders to Create
- `.github/workflows/ci-backend.yml` - GitHub Actions workflow
- `.github/ci-shared/prettier-config/prettier.shared.config.js` - Shared Prettier config
- `.github/ci-shared/eslint-config/eslint.backend.config.js` - Shared ESLint config
- `phpstan.neon` - PHPStan configuration
- `tests/Feature/` - Feature test directory
- `tests/Unit/` - Unit test directory

### 🔧 Files to Modify
- `composer.json` - Add lint/format/test scripts

**For developers who want to get CI running in 5 minutes:**

1. **Copy workflow template:**
   ```bash
   cp ci-structure/workflow-templates/ci-backend.yml .github/workflows/
   ```

2. **Install PHP dependencies:**
   ```bash
   composer install
   ```

3. **Setup Laravel environment:**
   ```bash
   cp .env.example .env
   php artisan key:generate
   ```

4. **Run tests locally to verify:**
   ```bash
   php artisan test
   ```

5. **Create PR → see CI in action!**

---

> **Note:** This checklist covers detailed backend (Laravel) CI setup. For shared principles and quick setup, see [CI Setup Checklist](./ci_setup_checklist.md).

---

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
- [ ] Replace placeholder in `workflow-templates/ci-backend.yml`:
  ```bash
  php artisan test
  ```
- [ ] Run tests locally to verify setup

## ✅ 6. PHP Linting Setup

- [ ] Install PHP linting tools:
  ```bash
  composer require --dev phpstan/phpstan
  composer require --dev laravel/pint
  ```

- [ ] Add scripts to `composer.json`:
  ```json
  {
    "scripts": {
      "test": "php artisan test",
      "lint": "phpstan analyse",
      "format": "pint --test"
    }
  }
  ```

- [ ] Create PHPStan config file (`phpstan.neon`):
  ```yaml
  parameters:
    level: 5
    paths:
      - app
      - tests
    excludePaths:
      - app/Console/Kernel.php
  ```

## ✅ 7. Laravel-Specific Configuration

- [ ] Ensure `.env.testing` exists for test environment
- [ ] Configure database for testing:
  ```bash
  php artisan config:cache --env=testing
  ```

- [ ] Add test database configuration to CI workflow

## ✅ 8. Enhanced CI Configuration

- [ ] Update CI config to include detailed checking:

  ```yaml
  - name: Run PHP Linting
    run: composer run lint

  - name: Check Code Formatting
    run: composer run format

  - name: Run Tests
    run: composer run test
  ```

## ✅ 9. Rollback Strategy

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

## ✅ 10. Environment-Specific Configs

**Current Implementation:**
- Single CI workflow for PRs from developers
- Focus on code quality and testing

**Future Implementation (Phase 3):**
- **Development PRs:** Current workflow (linting, formatting, unit tests)
- **Production Merges:** Enhanced workflow with integration testing
- **Deployment Pipeline:** Full API testing and security scans

**Approach:**
1. Start with single workflow for all PRs
2. Later add conditional steps based on target branch
3. Implement integration testing for main branch merges

## ✅ 11. Future Enhancements (Optional)

### 🚀 Phase 2: Advanced Testing
- [ ] Add API testing with Pest or PHPUnit
- [ ] Integrate database testing
- [ ] Add test coverage reporting
- [ ] Performance testing integration

### 🔒 Pre-commit Hooks (Optional)
Use `husky` + `lint-staged` to automatically run checks before commits.

**To install:**
```bash
composer require --dev husky
npx husky install
```

**Add this to `package.json`:**
```json
"lint-staged": {
  "*.php": ["pint", "phpstan analyse"]
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
- [ ] Database migration testing
- [ ] Automated deployment to staging 