# ✅ Backend CI Setup Checklist (SkilledUp.Life)

> **Note:** This checklist covers backend (Laravel) CI setup with PHP linting, testing, and future deployment integration.

## 🚀 SHORT VERSION - Quick Implementation

### 📁 New Files & Folders to Create
- `.github/workflows/ci-backend.yml` - GitHub Actions workflow
- `.github/ci-shared/prettier-config/prettier.backend.config.js` - Backend Prettier config
- `.github/ci-shared/eslint-config/eslint.backend.config.js` - Shared ESLint config
- `phpstan.neon` - PHPStan configuration
- `tests/Feature/` - Feature test directory
- `tests/Unit/` - Unit test directory

### 🔧 Files to Modify
- `composer.json` - Add lint/format/test scripts

**Overview of Steps to Implement:**

1. **Ensure you are on staging branch:**
   ```bash
   git checkout ci-implementation
   # If branch doesn't exist, create it:
   # git checkout main
   # git pull origin main
   # git checkout -b ci-implementation
   ```

2. **Copy workflow template:**
   ```bash
   cp ci-structure/workflow-templates/ci-backend.yml .github/workflows/
   ```

3. **Install PHP dependencies:**
   ```bash
   composer install
   ```

4. **Setup Laravel environment:**
   ```bash
   cp .env.example .env
   php artisan key:generate
   ```

5. **Run tests locally to verify:**
   ```bash
   php artisan test
   ```

6. **Create PR → see CI in action!**

---

> **Note:** This checklist covers detailed backend (Laravel) CI setup. For shared principles and quick setup, see [CI Setup Checklist](./ci_setup_checklist.md).

---

## ✅ 1. Create Staging Branch

- [ ] Create staging branch for safe CI implementation:
  ```bash
  git checkout main
  git pull origin main
  git checkout -b ci-implementation
  ```
- [ ] This allows testing CI without affecting main branch
- [ ] All subsequent steps will be implemented on this branch

## ✅ 2. Inspect for Composer or NPM

- [ ] Check if `composer.json` and `composer.lock` exist
- [ ] If not:
  - Run: `composer install`
  - Commit the generated `composer.lock`

- [ ] Also check if `package.json` is used (optional — for frontend assets)

## ✅ 3. Setup Workflow

- [ ] Path must be:
  ```
  backend/.github/workflows/ci-backend.yml
  ```
- [ ] Use a basic version with:
  - Lint check (if PHP linter installed)
  - Unit test placeholder (Laravel)

## ✅ 4. Trigger the Workflow

- [ ] Create a test sub-branch from `ci-implementation`:
  ```bash
  git checkout ci-implementation
  git checkout -b test/ci-backend-workflow
  # Make a small change (e.g., add a comment to a PHP file)
  git add .
  git commit -m "test: trigger backend CI workflow"
  git push origin test/ci-backend-workflow
  ```
- [ ] Open PR from `test/ci-backend-workflow` → `ci-implementation`
- [ ] Confirm `CI Pipeline / Backend Tests` (or similar name) shows up in GitHub Checks
- [ ] Verify workflow passes and merge the test PR

### 📋 Sub-Branch Strategy for Testing

**For testing features during CI implementation:**
```bash
# Always create sub-branches from ci-implementation
git checkout ci-implementation
git checkout -b feature/your-backend-feature

# Work on your feature
# Commit and push
git add .
git commit -m "feat: your backend feature description"
git push origin feature/your-backend-feature

# Create PR: feature/your-backend-feature → ci-implementation
# This triggers CI and tests your changes safely
```

**Key Points:**
- ✅ **Target**: All PRs should target `ci-implementation` (not `develop` or `main`)
- ✅ **Source**: Create feature branches from `ci-implementation`
- ✅ **Testing**: CI runs on every PR to `ci-implementation`
- ✅ **Safety**: No risk to production code during testing

## ✅ 5. Enable Status Checks (Admin Only)

- [ ] Ask PO to enable status checks:
  - `CI Pipeline / Backend Tests`

## ✅ 6. Prepare Tests

- [ ] Ensure Laravel tests are in:
  ```
  backend/tests/
  ```
- [ ] Replace placeholder in `workflow-templates/ci-backend.yml`:
  ```bash
  php artisan test
  ```
- [ ] Run tests locally to verify setup

## ✅ 7. PHP Linting Setup

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

## ✅ 8. Laravel-Specific Configuration

- [ ] Ensure `.env.testing` exists for test environment
- [ ] Configure database for testing:
  ```bash
  php artisan config:cache --env=testing
  ```

- [ ] Add test database configuration to CI workflow

## ✅ 9. Enhanced CI Configuration

- [ ] Update CI config to include detailed checking:

  ```yaml
  - name: Run PHP Linting
    run: composer run lint

  - name: Check Code Formatting
    run: composer run format

  - name: Run Tests
    run: composer run test
  ```

## ✅ 10. Rollback Strategy

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

### 📋 Syncing Strategy for ci-implementation

**Best Approach: Regular merges from develop to ci-implementation**

```bash
# Option 1: Daily sync (recommended)
git checkout ci-implementation
git merge develop
# Resolve any conflicts and push
git push origin ci-implementation

# Option 2: Weekly sync
git checkout ci-implementation
git merge develop
git push origin ci-implementation

# Option 3: Before major feature work
git checkout ci-implementation
git merge develop
git push origin ci-implementation
```

**Why This Approach:**
- ✅ **Keeps ci-implementation current** with other developers' work
- ✅ **Prevents massive conflicts** when merging to develop later
- ✅ **Tests CI with real code changes** from the team
- ✅ **Maintains team collaboration** during CI testing phase

**Recommended Frequency:**
- **Daily**: If team is very active
- **Every 2-3 days**: Standard approach
- **Weekly**: If team is small or changes are minimal

## ✅ 11. Environment-Specific Configs

**Current Implementation:**
- Single CI workflow for PRs from developers
- Focus on code quality and testing

**Future Implementation (Advanced):**
- **Development PRs:** Current workflow (linting, formatting, unit tests)
- **Production Merges:** Enhanced workflow with integration testing
- **Deployment Pipeline:** Full API testing and security scans

**Approach:**
1. Start with single workflow for all PRs
2. Later add conditional steps based on target branch
3. Implement integration testing for main branch merges

## ✅ 12. Future Enhancements (Optional)

### 🚀 Advanced: Testing Integration
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