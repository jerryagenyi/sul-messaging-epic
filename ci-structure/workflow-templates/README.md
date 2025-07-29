# Workflow Templates

> **Industry-standard GitHub Actions workflows for SkilledUp.Life projects**

This folder contains production-ready GitHub Actions workflow templates that can be copied and customized for different project types. These templates follow industry best practices and are ready for immediate implementation.

## 📁 Contents

### Available Templates

- **[ci-frontend.yml](./ci-frontend.yml)** - Vue.js frontend CI/CD workflow
- **[ci-backend.yml](./ci-backend.yml)** - Laravel backend CI/CD workflow
- **[regression-check.yml](./regression-check.yml)** - Regression testing prototype (owner-facing)

### Template Features

#### Frontend Workflow (`ci-frontend.yml`)
- **Linting & Formatting** - ESLint and Prettier validation
- **Unit Testing** - Jest/Vitest with coverage reporting
- **E2E Testing** - Playwright with artifact uploads
- **Build Validation** - Production build verification
- **Caching** - npm dependency caching for faster builds

#### Backend Workflow (`ci-backend.yml`)
- **PHP Linting** - PHP_CodeSniffer and PHPStan analysis
- **Testing** - PHPUnit with database integration
- **Security Scanning** - Composer audit and Symfony security checker
- **Build Optimization** - Laravel production optimizations
- **Coverage Reporting** - Test coverage with Codecov integration

#### Regression Workflow (`regression-check.yml`)
- **Smoke Testing** - Basic functionality validation
- **Prototype Status** - Owner-facing workflow for future stability validation
- **Future Integration** - Foundation for chained CI workflows after PR merges

## 🔧 Usage

1. **Copy the template** to your project's `.github/workflows/` directory
2. **Customize for your project** - Update paths, branch names, and environment variables
3. **Configure secrets** - Add required environment secrets in GitHub settings
4. **Test the workflow** - Create a PR to trigger the CI pipeline

## 🚀 Quick Setup

### Frontend Project
```bash
# Copy the frontend workflow
cp ci-foundation/workflow-templates/ci-frontend.yml .github/workflows/

# Update package.json scripts (if not already present)
npm pkg set scripts.lint="eslint src/ --ext .js,.vue"
npm pkg set scripts.format="prettier --check src/"
npm pkg set scripts."test:unit"="jest"
npm pkg set scripts."test:e2e"="playwright test"
```

### Backend Project
```bash
# Copy the backend workflow
cp ci-foundation/workflow-templates/ci-backend.yml .github/workflows/

# Install required dev dependencies
composer require --dev phpunit/phpunit squizlabs/php_codesniffer phpstan/phpstan
```

## ⚙️ Configuration

### Environment Variables
Configure these in your repository settings:

**Frontend:**
- `NODE_VERSION` - Node.js version (default: 18)
- `CODECOV_TOKEN` - Codecov integration token

**Backend:**
- `PHP_VERSION` - PHP version (default: 8.2)
- `DATABASE_URL` - Test database connection
- `CODECOV_TOKEN` - Codecov integration token

### Branch Protection
Enable these status checks:
- `CI Pipeline - Frontend / Lint & Format Check`
- `CI Pipeline - Frontend / Unit Tests`
- `CI Pipeline - Frontend / E2E Tests`
- `CI Pipeline - Frontend / Build Check`
- `CI Pipeline - Backend / PHP Lint & Style Check`
- `CI Pipeline - Backend / Unit & Feature Tests`
- `CI Pipeline - Backend / Security Scan`
- `CI Pipeline - Backend / Build Check`

## 📊 Quality Gates

### Required for Merge
- ✅ All linting checks pass
- ✅ All tests pass with minimum coverage
- ✅ Security scans show no vulnerabilities
- ✅ Build process completes successfully

### Optional Enhancements
- 📈 Coverage thresholds (80% minimum recommended)
- 🔒 Security scanning integration
- 🚀 Performance testing
- 📦 Automated deployments

## 📚 Documentation

- **[CI/CD Foundation](../README.md)** - Complete foundation overview
- **[Setup Checklist](../ci-setup-checklist.md)** - Implementation guide
- **[GitHub Actions Docs](https://docs.github.com/en/actions)** - Official documentation

## 🔄 Customization

### Adding Custom Steps
1. Copy the template to your project
2. Add project-specific steps (e.g., database seeding, custom tests)
3. Update environment variables and secrets
4. Test thoroughly before enabling branch protection

### Framework-Specific Modifications
- **Vue.js**: Update ESLint rules for Vue 3 components
- **Laravel**: Add custom artisan commands or database migrations
- **Testing**: Integrate with your preferred testing framework
- **Deployment**: Add deployment steps for your hosting platform

---

*These templates are part of the SkilledUp.Life CI/CD Foundation. For questions or improvements, please contribute through our standard process.*

---

## 🚧 Implementation Notes

🚧 This configuration lives in a staging repo (`https://github.com/jerryagenyi/skilleduplife-ci`)  
🚀 Intended to be implemented in:
- Frontend: `https://github.com/skilleduplife/frontend`
- Backend: `https://github.com/skilleduplife/backend`

Please copy config files and adjust paths to match the actual production repo's structure.

---

## 🛠 Trigger Caveats & Future Plans

Only PR-Triggered Workflows (Current Scope):
- All active workflows (`ci-frontend.yml`, `ci-backend.yml`, `regression-check.yml`) are triggered via `pull_request` events
- `ci-frontend.yml` and `ci-backend.yml` serve developer onboarding, CI enforcement, and scoped validation
- `regression-check.yml` serves as a **lead developer/owner-facing prototype** for validating stability across merged PRs — not a required status check

Push-Triggered `workflow_run` Chaining (Planned Only):
- GitHub's `workflow_run` only works on `push` events to the default branch (`main`)
- These events occur **after** PRs are merged — usually by a maintainer or lead engineer
- They cannot run on PRs, which is why CI chaining lives only in sample `.txt` files for now
- See `ci-frontend-reg-check.txt` and `ci-backend-reg-check.txt` for future architecture
- **Product Owner Context:** This means additional safety checks will automatically run after code is merged, acting as a final quality gate before changes reach users

Regression Check Clarification:
- `regression-check.yml` runs on `pull_request` events only
- It does NOT run on `push` events at this time — we are not using `workflow_run` yet
- The file is scoped for internal QA/stability review by the lead developer
- It is not a required status check: failed runs appear as warnings but do not block merging

🧪 Regression Check – Current & Future Logic

- Located in [`skilleduplife-ci/workflow-templates/regression-check.yml`](https://github.com/jerryagenyi/skilleduplife-ci/blob/master/ci-foundation/workflow-templates/regression-check.yml)
- Currently runs on `pull_request` events only (branches: `main`, `dev`)
- Future plan: trigger downstream CI workflows using `workflow_run` after successful merge
- Goal: catch regressions before production deploy pipelines run
- Non-blocking today: failed runs do not prevent merging
