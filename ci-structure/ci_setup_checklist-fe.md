# ✅ Frontend CI Setup Checklist (SkilledUp.Life)

> **Note:** This checklist covers frontend (Vue) CI setup with ESLint, Prettier, and future testing integration.

## 🚀 SHORT VERSION - Quick Implementation

### 📁 New Files & Folders to Create
- `.github/workflows/ci-frontend.yml` - GitHub Actions workflow
- `.github/ci-shared/prettier-config/prettier.frontend.config.js` - Frontend Prettier config
- `.github/ci-shared/eslint-config/eslint.vue.config.js` - Shared ESLint config
- `tests/` - Complete test structure
  - `config/` - All test configurations
    - `vitest.config.js` - Unit & component testing
    - `playwright.config.js` - E2E testing
    - `setup.js` - Test setup and mocks
  - `e2e/` - End-to-end tests
    - `critical/` - Critical user flows
    - `user-journeys/` - Complete user journeys
  - `components/` - Component tests
  - `unit/` - Utility & composable tests
  - `regression/` - Regression snapshots & fixtures
    - `fixtures/` - Test data and files
- `.eslintrc.js` - ESLint configuration (extends shared config)
- `.prettierrc.json` - Prettier configuration (extends shared config)

### 🔧 Files to Modify
- `package.json` - Add lint/format scripts

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
   cp ci-structure/workflow-templates/ci-frontend.yml .github/workflows/
   ```

3. **Install ESLint:**
   ```bash
   npm install --save-dev eslint eslint-plugin-vue @vue/eslint-config-prettier prettier
   ```

4. **Copy config files:**
   ```bash
   cp ci-structure/ci-shared/eslint-config/eslint.vue.config.js .github/ci-shared/eslint-config/eslint.vue.config.js
   cp ci-structure/ci-shared/prettier-config/prettier.base.config.js .github/ci-shared/prettier-config/prettier.frontend.config.js
   ```

5. **Add scripts to package.json:**
   ```json
   {
     "scripts": {
       "lint": "eslint src/ tests/ *.js --ext .js,.vue",
       "format": "prettier --check src/ tests/ *.js",
       "format:fix": "prettier --write src/ tests/ *.js"
     }
   }
   ```

6. **Create PR → see CI in action!**

---

> **Note:** This checklist covers detailed frontend (Vue) CI setup. For shared principles and quick setup, see [CI Setup Checklist](./ci_setup_checklist.md).

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

## ✅ 2. Linting & Formatting Setup

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

## ✅ 3. Dev Setup Reminder

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

## ✅ 4. Ensure Lock File Exists / Update After Dependency Changes

- [x] `frontend/package-lock.json` exists.
- [ ] After installing ESLint or any new dependency, run:

  ```bash
  npm install
  ```

  - Commit the updated `package-lock.json` to the repo if it changes.

## ✅ 5. Setup Workflow

- [ ] Create this path:
  ```
  frontend/.github/workflows/ci-frontend.yml
  ```
- [ ] Add the baseline CI for style and structure checks version of `workflow-templates/ci-frontend.yml` initially (with echo placeholders for other jobs)
- [ ] Confirm it's committed to the correct path

## ✅ 6. Trigger Workflow at Least Once

- [ ] Create a test sub-branch from `ci-implementation`:
  ```bash
  git checkout ci-implementation
  git checkout -b test/ci-workflow
  # Make a small change (e.g., add a comment)
  git add .
  git commit -m "test: trigger CI workflow"
  git push origin test/ci-workflow
  ```
- [ ] Open a PR from `test/ci-workflow` → `ci-implementation`
- [ ] Confirm `CI Pipeline / Lint Frontend` shows up on the PR
- [ ] Verify workflow passes and merge the test PR

### 📋 Sub-Branch Strategy for Testing

**For testing features during CI implementation:**
```bash
# Always create sub-branches from ci-implementation
git checkout ci-implementation
git checkout -b feature/your-feature-name

# Work on your feature
# Commit and push
git add .
git commit -m "feat: your feature description"
git push origin feature/your-feature-name

# Create PR: feature/your-feature-name → ci-implementation
# This triggers CI and tests your changes safely
```

**Key Points:**
- ✅ **Target**: All PRs should target `ci-implementation` (not `develop` or `main`)
- ✅ **Source**: Create feature branches from `ci-implementation`
- ✅ **Testing**: CI runs on every PR to `ci-implementation`
- ✅ **Safety**: No risk to production code during testing

## ✅ 7. Enable Status Check (Admin Only)

- [ ] Ask PO to enable status check for:
  - `CI Pipeline / Lint Frontend`
- [ ] Path: GitHub → Settings → Branches → Protection Rules
- [ ] **Important**: During trial phase, CI uses warnings (not errors) to avoid blocking PRs
- [ ] **Note**: Only critical rules (like `no-debugger`) will block merges during testing

## ✅ 8. Prepare Test Files

- [ ] Create test structure in frontend repo:
  ```bash
  mkdir -p tests/{config,e2e/{critical,user-journeys},components,unit,regression/fixtures}
  ```
- [ ] Structure will be:
  ```
  frontend/tests/
  ├── config/                  # All test configurations
  │   ├── vitest.config.js     # Unit & component testing
  │   ├── playwright.config.js # E2E testing
  │   └── setup.js            # Test setup and mocks
  ├── e2e/                     # End-to-end tests
  │   ├── critical/           # Critical user flows
  │   └── user-journeys/      # Complete user journeys
  ├── components/              # Component tests
  ├── unit/                    # Utility & composable tests
  └── regression/              # Regression snapshots & fixtures
      └── fixtures/           # Test data and files
  ```
- [ ] Replace placeholder `echo` in `workflow-templates/ci-frontend.yml` with:
  ```bash
  npm run test:unit
  npx playwright test
  ```
- [ ] Run tests locally to verify setup

## ✅ 9. Clarify ESLint/Prettier Roles vs CI + Dev Workflow

**Clarification for team:**

- ESLint and Prettier enforce code standards _locally and in CI_.
- Developers should run `npm run lint` and `npm run format` before **every commit**.
- If skipped, CI will catch errors on PR and block the merge.

## ✅ 10. Baseline CI Explanation

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

## ✅ 11. Vue-Specific ESLint + Prettier Rules

**Use the provided config files:**
- ESLint config: [`ci-structure/ci-shared/eslint-config/eslint.vue.config.js`](../ci-shared/eslint-config/eslint.vue.config.js)
- Prettier config: [`ci-structure/ci-shared/prettier-config/prettier.base.config.js`](../ci-shared/prettier-config/prettier.base.config.js)

These rules encourage readable, maintainable Vue code without frustrating devs.

## ✅ 12. Enhanced CI Configuration

- [ ] Update CI config to include detailed lint/format checking:

  ```yaml
  - name: Run Lint and Format Check
    run: npm run lint && npm run format

  - name: Show Unformatted Files
    run: prettier --list-different src/ tests/ *.js
  ```

  This flags files that require formatting without auto-fixing in CI—promotes developer accountability.

## ✅ 13. README Additions for Dev Expectations

📋 **Workflow Expectations:**

- Always run `npm run lint` and `npm run format` before submitting a PR.
- Use ESLint and Prettier plugins in your IDE (e.g. VS Code) to catch issues early.
- CI will reject unformatted or error-prone code during PR reviews.

## ✅ 14. Staging Branch Implementation Strategy

### 🎯 Why Use a Staging Branch?
- **Safe testing**: Implement CI without affecting main branch
- **Real environment**: Full API communication, databases, deployments
- **Team coordination**: One developer can test while others continue on main
- **Easy rollback**: Delete branch if issues arise
- **Boss-friendly**: No repository duplication needed

### 🚀 Implementation Approach

#### **Phase 1: Setup Staging Branch**
```bash
# 1. Create staging branch from main
git checkout main
git pull origin main
git checkout -b ci-implementation

# 2. Implement all CI changes on this branch
# - Copy workflow files
# - Install dependencies
# - Update configs
# - Test locally

# 3. Push staging branch
git add .
git commit -m "feat: implement CI/CD pipeline"
git push origin ci-implementation
```

#### **Phase 2: Single Developer Test**

**Set up Branch Protection for ci-implementation:**
```
GitHub → Settings → Branches → Add rule
Branch name pattern: ci-implementation
✅ Require status checks to pass before merging
✅ Require branches to be up to date before merging
✅ Include administrators (optional)
```

**Developer Workflow Options:**

**Option A: Direct Push (if allowed)**
```bash
# Work directly on ci-implementation branch
git checkout ci-implementation
# Make changes, commit, push
git add .
git commit -m "feat: add new feature"
git push origin ci-implementation  # Triggers workflow directly
```

**Option B: PR Workflow (Recommended)**
```bash
# Create feature branch from ci-implementation
git checkout ci-implementation
git checkout -b feature/login

# Make changes, commit, push
git add .
git commit -m "feat: add login feature"
git push origin feature/login

# Create PR: feature/login → ci-implementation
# This triggers workflow and blocks merge if tests fail
```

**Key Difference:**
- **Direct push**: Triggers workflow on the branch itself
- **PR workflow**: Triggers workflow on the PR, blocks merge if failed

#### **Phase 3: Merge to Main**
```bash
# 1. Sync with main (resolve conflicts)
git checkout ci-implementation
git merge main

# 2. Final testing
# 3. Create PR: ci-implementation → main
# 4. All developers now use CI
```

### 🛡️ Conflict Prevention Strategy

#### **Daily Sync (Recommended)**
```bash
# Every day, sync your staging branch
git checkout ci-implementation
git merge main
# Fix conflicts immediately (smaller = easier)
```

#### **Frequent Syncing Strategy for ci-implementation**
**Best Approach: Regular PRs from develop/main to ci-implementation**

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

#### **Communication Plan**
- **Tell team**: "Working on CI implementation branch"
- **Ask them**: "Hold off on major changes to main"
- **Coordinate**: "Let's merge this quickly"

#### **Backup Plan**
```bash
# If conflicts get too complex
git checkout main
git checkout -b ci-implementation-v2
# Start fresh with latest main
```

### 📋 Single Developer Best Practices

#### **Why One Developer First?**
- **Lower risk**: Easier to coordinate and fix issues
- **Faster feedback**: Quick validation of CI workflow
- **Learning opportunity**: Developer learns CI process
- **Team confidence**: Success builds momentum

#### **Developer Selection Criteria**
- **Experienced**: Someone comfortable with Git and npm
- **Available**: Can dedicate time to testing
- **Communicative**: Will report issues and feedback
- **Patient**: Understands this is a learning process

#### **Testing Checklist for Single Developer**
- [ ] Can create feature branches from `ci-implementation`
- [ ] Can submit PRs to `ci-implementation`
- [ ] CI runs on PRs and shows results
- [ ] Can fix linting/formatting issues locally
- [ ] Can push fixes and see CI pass
- [ ] Can merge PRs to `ci-implementation`
- [ ] API endpoints work normally
- [ ] No performance issues with CI

#### **Communication Template**
```
Subject: CI Implementation Testing - Need Your Help

Hi [Developer Name],

We're implementing a CI/CD pipeline to improve code quality. 
I'd like you to test it for a week on a staging branch.

What this means:
- You'll work on a branch called 'ci-implementation'
- You'll encounter automated code checks (ESLint, Prettier)
- You'll need to fix formatting issues before merging

Benefits:
- Learn modern development practices
- Help improve our codebase quality
- No risk to main branch

Testing period: Once validated, we'll roll it out to everyone.

Are you available to help test this?
```

### 🔄 Rollback Strategy

**Before implementing CI changes:**
- [ ] Document current working state before CI changes
- [ ] Create a staging branch for CI implementation
- [ ] Test CI on the staging branch first
- [ ] Have a "disable CI" option for emergency fixes

**If issues arise:**
```bash
# Option 1: Fix on staging branch
git checkout ci-implementation
# Fix issues, test, then continue

# Option 2: Start fresh
git checkout main
git checkout -b ci-implementation-v2
# Copy CI files again, test

# Option 3: Abandon (worst case)
# Delete ci-implementation branch
# Return to main branch
# Plan different approach
```

## ✅ 15. Environment-Specific Configs

**Current Implementation:**
- Single CI workflow for PRs from developers
- Focus on code quality and formatting checks

**Future Implementation (Advanced):**
- **Development PRs:** Current workflow (linting, formatting, unit tests)
- **Production Merges:** Enhanced workflow with regression testing
- **Deployment Pipeline:** Full E2E testing and security scans

**Approach:**
1. Start with single workflow for all PRs
2. Later add conditional steps based on target branch
3. Implement regression testing for main branch merges

## ✅ 16. Future Enhancements (Optional)

### 🚀 Advanced: Testing Integration
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