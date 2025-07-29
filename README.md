# SkilledUp.Life CI/CD Foundation

**Repository:** https://github.com/jerryagenyi/sul-messaging-epic

> **🚀 Central CI/CD Implementation Hub for SkilledUp.Life Projects**

This repository has been repurposed to serve as the central CI/CD foundation for all SkilledUp.Life projects. It provides standardized workflows, quality gates, and development guidelines to ensure consistent code quality and deployment reliability across our entire platform.

## 📋 Repository Pivot

**Original Purpose:** Messaging module implementation using TDD/BDD  
**Current Purpose:** Central CI/CD foundation for SkilledUp.Life projects

The original messaging-related content has been preserved for future reference while the repository now focuses on CI/CD standardization and implementation.

## 🚀 CI/CD Foundation

### Quick Access

- **[CI/CD Setup Guide](ci-foundation/README.md)** - Complete foundation overview
- **[Getting Started](ci-foundation/getting-started-ci.md)** - Developer onboarding
- **[Setup Checklist](ci-foundation/ci-setup-checklist.md)** - Step-by-step implementation

### What's Included

- **Standardized Workflows** - Reusable GitHub Actions templates
- **Quality Gates** - ESLint, Prettier, and testing automation
- **Developer Guidelines** - Clear expectations and best practices
- **Configuration Examples** - ESLint and Prettier rule samples

## 🎯 Project Overview

This project implements a complete messaging solution with:

- **Role-based permissions** - Control who can message whom based on user types and subscription levels
- **Admin configuration** - System administrators can configure messaging settings through a dashboard
- **Profile integration** - Message buttons on user profiles for easy conversation initiation
- **Real-time messaging** - Live messaging interface with search and conversation management

## 📋 Epic Structure

### Features

1. **[Feature-01](docs/specs/messaging-epic/feature-01-role-based-permissions.md)**: Role-Based Messaging Permissions System
2. **[Feature-02](docs/specs/messaging-epic/feature-02-admin-settings.md)**: Admin Configurable Messaging Settings
3. **[Feature-03](docs/specs/messaging-epic/feature-03-profile-buttons.md)**: Profile Message Buttons Integration
4. **[Feature-04](docs/specs/messaging-epic/feature-04-messaging-interface.md)**: Core Messaging Interface & Functionality

### Documentation Structure

```
sul-messaging-epic/
├── docs/
│   ├── specs/messaging-epic/          # Feature specifications
│   ├── gherkin/messaging-epic/        # BDD scenarios
│   └── testing/messaging-epic/        # Test matrices
├── src/                               # Source code
├── tests/                             # Automated tests
├── spec-to-test/                      # Framework documentation
└── .github/workflows/                 # CI/CD workflows
```

## 🚀 Getting Started

### Prerequisites

- Node.js (v16+)
- Git
- Access to SkilledUp.Life platform APIs

### Development Workflow

This project follows the **Spec-to-Test Framework v2.2** for unified development:

1. **Epic Overview** → [docs/specs/messaging-epic/epic-overview.md](docs/specs/messaging-epic/epic-overview.md)
2. **Feature Specifications** → [docs/specs/messaging-epic/](docs/specs/messaging-epic/)
3. **Gherkin Scenarios** → [docs/gherkin/messaging-epic/](docs/gherkin/messaging-epic/)
4. **Test Matrices** → [docs/testing/messaging-epic/](docs/testing/messaging-epic/)
5. **Implementation** → TDD approach with automated tests
6. **CI/CD** → GitHub Actions for quality gates

### Quick Start

```bash
# Clone the repository
git clone https://github.com/jerryagenyi/sul-messaging-epic.git
cd sul-messaging-epic

# Install dependencies
pip install -r requirements.txt
npm install  # For development scripts

# Run tests
npm test

# Start development server
npm run dev
```

### 📋 Workflow Expectations

- Always run `npm run quality` before submitting a PR
- Use Python linting plugins in your IDE (e.g. VS Code) to catch issues early
- CI will reject unformatted or error-prone code during PR reviews
- Run `npm run format:fix` and `npm run imports:fix` to auto-fix formatting issues locally

## 📊 Team Roles & Responsibilities

| Role               | Primary Responsibilities        | Secondary Support        |
| ------------------ | ------------------------------- | ------------------------ |
| **PO/PM**          | Feature specs, Epic overview    | Review Gherkin scenarios |
| **QA**             | Gherkin scenarios, Test input   | Review feature specs     |
| **Lead**           | Test matrices, GitHub issues    | Review all artifacts     |
| **Dev**            | Write tests, Implement features | Fix CI failures          |
| **GitHub Actions** | Run tests in CI                 | Automated quality gates  |

## 🧪 Testing Strategy

### Test-Driven Development (TDD)

- Tests written before or alongside development
- Guided by Gherkin scenarios from specifications
- All tests must pass in CI before merging

### Test Types

- **Unit Tests**: Individual component/function testing
- **Integration Tests**: API and service integration
- **E2E Tests**: Full user workflow testing
- **Permission Tests**: Role-based access validation

### Test Matrix

See [docs/testing/messaging-epic/test-matrix.md](docs/testing/messaging-epic/test-matrix.md) for complete test coverage mapping.

## 🔧 Configuration

### Messaging Permission Settings

#### Company Profiles (6 Settings)

| Setting                 | Volunteers | PRO Volunteers | Volunteer Applicants | Companies | Customers |
| ----------------------- | ---------- | -------------- | -------------------- | --------- | --------- |
| Setting 1               | ✅         | ✅             | ✅                   | ✅        | ✅        |
| Setting 2               | ✅         | ✅             | ✅                   | ❌        | ✅        |
| Setting 3               | ✅         | ✅             | ✅                   | ❌        | ❌        |
| **Setting 4 (default)** | ❌         | ✅             | ✅                   | ❌        | ❌        |
| Setting 5               | ❌         | ❌             | ✅                   | ❌        | ❌        |
| Setting 6               | ❌         | ✅             | ❌                   | ❌        | ❌        |

#### Volunteer Profiles

| Setting          | Volunteers | PRO Volunteers | Companies | Plan 1 Customers | Plan 2 Customers |
| ---------------- | ---------- | -------------- | --------- | ---------------- | ---------------- |
| Setting 1        | ✅         | ✅             | ✅        | ✅               | ✅               |
| Setting 2        | ❌         | ✅             | ✅        | ✅               | ✅               |
| **Settings 3-6** | ❌         | ❌             | ❌        | ❌               | ❌               |

## 🚦 CI/CD Pipeline

### GitHub Actions Workflows

- **Test Runner**: Runs all automated tests on PR
- **Linting**: Code quality and style checks
- **Build**: Validates successful build process
- **Deploy**: Automated deployment (future)

### Quality Gates

- All tests must pass ✅
- Code coverage requirements met ✅
- Linting passes ✅
- PR review approved ✅

## 📚 Documentation

### Framework Documentation

- **[Spec-to-Test Framework v2.2](spec-to-test/Spec-to-Test_framework_v2.2.md)** - Complete development framework
- **[Original Messaging Specification](Specification_Messaging.md)** - Business requirements

### Feature Documentation

- **[Epic Overview](docs/specs/messaging-epic/epic-overview.md)** - High-level business objectives
- **[Feature Specifications](docs/specs/messaging-epic/)** - Detailed feature requirements
- **[Gherkin Scenarios](docs/gherkin/messaging-epic/)** - BDD test scenarios
- **[Test Matrix](docs/testing/messaging-epic/test-matrix.md)** - Test coverage mapping

## 🤝 Contributing

### Development Process

1. **Review** feature specifications and acceptance criteria
2. **Write tests** based on Gherkin scenarios
3. **Implement** features to pass tests
4. **Submit PR** with all tests passing
5. **Code review** by Lead and QA
6. **Merge** after approval

### Issue Labels

- `epic` - Epic-level work items
- `feature` - Feature development
- `test-case` - Test implementation
- `qa` - Quality assurance tasks
- `tdd` - Test-driven development

## 📞 Support

For questions or support:

- **GitHub Issues**: [Create an issue](https://github.com/jerryagenyi/sul-messaging-epic/issues)
- **Documentation**: Check [docs/](docs/) folder
- **Framework Guide**: [Spec-to-Test Framework v2.2](spec-to-test/Spec-to-Test_framework_v2.2.md)

## 📄 License

This project is part of the SkilledUp.Life platform. All rights reserved.

---

_Built with the Spec-to-Test Framework v2.2 for unified, test-driven development._
