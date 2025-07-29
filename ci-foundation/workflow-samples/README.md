# Workflow Samples

> **Reusable GitHub Actions workflows for SkilledUp.Life projects**

This folder contains standardized GitHub Actions workflow templates that can be copied and customized for different project types.

## 📁 Contents

### Available Workflows

- **[ci-frontend.yml](./ci-frontend.yml)** - Vue.js frontend CI workflow
- **[ci-backend.yml](./ci-backend.yml)** - Laravel backend CI workflow

### Planned Workflows

- **Deployment Workflows** - Production and staging deployment templates
- **Security Scanning** - Dependency and code security checks
- **Performance Testing** - Load and performance validation workflows
- **Cross-Platform** - Multi-framework CI/CD templates

## 🔧 Usage

1. Copy the relevant workflow file to your project's `.github/workflows/` directory
2. Customize the workflow for your specific project needs
3. Update branch names and triggers as required
4. Test the workflow with a sample PR

## 📋 Workflow Features

### Frontend CI Workflow

- **Linting** - ESLint code quality checks
- **Formatting** - Prettier formatting validation
- **Unit Tests** - Jest/Vitest test execution
- **E2E Tests** - Playwright/Cypress end-to-end testing
- **Build Validation** - Production build verification

### Backend CI Workflow

- **PHP Linting** - PHP_CodeSniffer or similar tools
- **Unit Tests** - PHPUnit test execution
- **Integration Tests** - API and service testing
- **Database Migrations** - Migration validation
- **Security Checks** - Dependency vulnerability scanning

## 🚀 Customization

### Environment Variables

Update these in your repository settings:

- `NODE_VERSION` - Node.js version for frontend builds
- `PHP_VERSION` - PHP version for backend builds
- `DATABASE_URL` - Database connection for tests

### Branch Protection

Enable these status checks:

- `CI Pipeline / Lint Frontend`
- `CI Pipeline / Lint Backend`
- `CI Pipeline / Tests`
- `CI Pipeline / Build`

## 📚 Documentation

- **[Getting Started Guide](../getting-started-ci.md)** - Workflow setup instructions
- **[Setup Checklist](../ci-setup-checklist.md)** - Complete implementation guide
- **[GitHub Actions Docs](https://docs.github.com/en/actions)** - Official documentation

---

_This folder is part of the SkilledUp.Life CI/CD Foundation. Contributions welcome!_
