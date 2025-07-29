# 🚀 Getting Started with CI/CD at SkilledUp.Life

> **Developer Onboarding Guide for CI/CD Implementation**

Welcome to SkilledUp.Life's CI/CD foundation! This guide will walk you through setting up and working with our standardized CI/CD practices.

## 📋 Prerequisites

Before you begin, ensure you have:

- **Node.js** (v16+) installed
- **Git** configured with your credentials
- **VS Code** or preferred IDE with ESLint/Prettier extensions
- **GitHub account** with access to SkilledUp.Life repositories

## 🛠️ Local Setup

### 1. Install ESLint and Prettier

```bash
# Install development dependencies
npm install --save-dev eslint prettier

# For Vue.js projects, also install:
npm install --save-dev @vue/eslint-config-prettier eslint-plugin-vue

# For Laravel projects with frontend assets:
npm install --save-dev eslint prettier
```

### 2. Configure Your IDE

#### VS Code Extensions

Install these extensions for the best development experience:

- **ESLint** - Real-time linting feedback
- **Prettier** - Automatic code formatting
- **Vetur** (for Vue.js projects) - Vue.js support

#### VS Code Settings

Add to your `.vscode/settings.json`:

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "eslint.validate": ["javascript", "javascriptreact", "vue"]
}
```

### 3. Run Quality Checks Locally

Before committing any code, always run:

```bash
# Check for linting issues
npm run lint

# Check formatting
npm run format

# Fix formatting issues automatically
npm run format:fix

# Run all quality checks
npm run quality
```

## 🔄 Workflow Integration

### Understanding CI Triggers

Our CI workflows are triggered by:

- **Pull Requests** to `main` or `dev` branches
- **Direct pushes** to protected branches (if enabled)
- **Manual workflow runs** (for testing)

### Typical CI Pipeline

1. **Lint Check** - ESLint validates code quality
2. **Format Check** - Prettier ensures consistent formatting
3. **Test Suite** - Unit and integration tests run
4. **Build Process** - Ensures code compiles successfully

### CI Status Checks

Look for these status checks on your PRs:

- ✅ **CI Pipeline / Lint Frontend** - Vue.js linting
- ✅ **CI Pipeline / Lint Backend** - Laravel/PHP linting
- ✅ **CI Pipeline / Tests** - Test suite execution
- ✅ **CI Pipeline / Build** - Build process validation

## 🚨 Fixing CI Violations

### Common Issues and Solutions

#### ESLint Errors

**Problem**: `Unexpected console statement. (no-console)`

**Solution**: Remove console.log statements or configure ESLint to allow them:

```js
// In .eslintrc.js
rules: {
  'no-console': 'warn' // or 'off' for development
}
```

#### Prettier Formatting Issues

**Problem**: Files don't match Prettier formatting

**Solution**: Run auto-formatting:

```bash
npm run format:fix
```

#### Test Failures

**Problem**: Tests failing in CI

**Solution**:

1. Run tests locally first: `npm test`
2. Check for environment-specific issues
3. Ensure all dependencies are properly installed

### Before Submitting PRs

Always run this checklist:

```bash
# 1. Install dependencies
npm install

# 2. Run quality checks
npm run quality

# 3. Run tests
npm test

# 4. Check for any remaining issues
npm run lint
npm run format
```

## 📚 Using the Setup Checklist

The [`ci-setup-checklist.md`](./ci-setup-checklist.md) is your comprehensive reference for:

- **Initial project setup** - Complete CI/CD implementation
- **Workflow configuration** - GitHub Actions setup
- **Quality gate configuration** - ESLint and Prettier rules
- **Team expectations** - Development standards

### When to Reference the Checklist

- **New project setup** - Follow step-by-step
- **Adding new quality gates** - Reference specific sections
- **Troubleshooting issues** - Check configuration examples
- **Team training** - Use as reference material

## 🔧 Customization Guidelines

### ESLint Rules

When customizing ESLint rules:

1. **Start with the foundation** - Use our base configurations
2. **Add project-specific rules** - Document the reasoning
3. **Test thoroughly** - Ensure rules work for your team
4. **Update documentation** - Keep the foundation current

### Prettier Configuration

Prettier configurations should be:

- **Consistent across projects** - Use the same base settings
- **Team-approved** - Get consensus on formatting preferences
- **Well-documented** - Explain any customizations

## 🚀 Advanced Features

### Pre-commit Hooks (Optional)

For teams ready for advanced automation:

```bash
# Install Husky and lint-staged
npm install --save-dev husky lint-staged

# Initialize Husky
npx husky install

# Add pre-commit hook
npx husky add .husky/pre-commit "npm run quality"
```

### Continuous Deployment

When ready for CD:

1. **Set up deployment workflows** - Copy from `workflow-samples/`
2. **Configure environment secrets** - Secure deployment credentials
3. **Test deployment process** - Ensure reliability
4. **Monitor deployments** - Track success rates

## 🆘 Getting Help

### Common Resources

- **[Setup Checklist](./ci-setup-checklist.md)** - Complete implementation guide
- **[Workflow Samples](./workflow-samples/)** - Reusable CI/CD templates
- **[Configuration Examples](./eslint-config/)** - ESLint customizations
- **[Formatting Standards](./prettier-config/)** - Prettier configurations

### Support Channels

- **GitHub Issues** - Report bugs or request features
- **Team Chat** - Quick questions and discussions
- **Maintainer Contact** - Jeremiah Agenyi for complex issues

## 📈 Best Practices

### For Developers

- **Run checks locally first** - Don't rely on CI to catch issues
- **Keep configurations updated** - Stay current with foundation changes
- **Document customizations** - Help others understand your choices
- **Contribute improvements** - Share learnings with the team

### For Teams

- **Regular reviews** - Assess CI/CD effectiveness monthly
- **Continuous improvement** - Evolve practices based on feedback
- **Knowledge sharing** - Train new team members on processes
- **Tool updates** - Keep dependencies current and secure

---

_This guide is part of the SkilledUp.Life CI/CD Foundation. For questions or improvements, please contribute through our standard process._
