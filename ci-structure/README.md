# ⚙️ SkilledUp.Life CI/CD Structure

## 🔍 Purpose

This folder contains the standardized CI/CD configurations, workflows, and setup guides used across SkilledUp.Life projects. It is designed to enforce consistency and automation for both frontend (Vue) and backend (Laravel) codebases. This modular structure serves as a reusable hub of CI logic for long-term scalability.

👉 Original focus on the Messaging Epic (TDD/BDD) remains documented in the main repo for future reference.

---

## 📂 Contents

- `ci_setup_checklist.md` – Unified CI setup checklist with shared principles
- `ci_setup_checklist-fe.md` – Detailed frontend (Vue) CI setup instructions
- `ci_setup_checklist-be.md` – Detailed backend (Laravel) CI setup instructions
- `ci-shared/` – Shared configuration files and setup guides
- `workflow-templates/` – GitHub Actions workflows for Vue & Laravel
- `README.md` – This document

---

## 🛠️ Setup Summary

1. Run `npm install` in your local frontend repo.
2. Verify and commit `.prettierrc`, `.eslintrc`, and updated `package.json`.
3. Trigger workflow via PR → `main` to see CI in action.
4. Add test coverage and track it via linked sheet.

Refer to [CI Setup Checklist](./ci_setup_checklist.md) for quick setup and shared principles, or the detailed [Frontend](./ci_setup_checklist-fe.md) and [Backend](./ci_setup_checklist-be.md) checklists for specific implementation steps.

---

## 🚀 Future Plans

- Add templates for test runners (Jest, Playwright)
- Extend workflows to integrate coverage reports
- Modularize CI setups for component-level enforcement

---

## 🧱 CI Pipeline Implementation Roadmap (Frontend Focus)

We are phasing CI in the following stages:

1. ✅ Basic CI – Linting & Formatting
   - Enforce Prettier and ESLint rules on all PRs

2. 🔬 Unit Tests
   - Add CI steps for frontend unit testing (e.g., Jest/Vitest)

3. 🎯 E2E Tests
   - Include steps for Playwright end-to-end testing

4. 🧪 Regression Prototyping
   - Build a standalone `regression-check.yml` workflow to validate smoke coverage
   - Future plans: trigger chained CI after regression passes using `workflow_run`
   - Currently runs on `pull_request` events only (non-blocking)
   - Goal: catch regressions before production deploy pipelines run

---

## 🚧 Repository Usage

This configuration lives in a staging repo (`https://github.com/jerryagenyi/skilleduplife-ci`)  
🚀 Intended to be implemented in:
- Frontend: `https://github.com/skilleduplife/frontend`
- Backend: `https://github.com/skilleduplife/backend`

Please copy config files and adjust paths to match the actual production repo's structure.

See [`ci-shared/README.md`](./ci-shared/README.md) for detailed usage instructions and configuration philosophy.
See [`ci-shared/ci_shared_setup_checklist.md`](./ci-shared/ci_shared_setup_checklist.md) for implementation steps.

---

## 👤 Maintainer

Built and curated by [@jerryagenyi](https://github.com/jerryagenyi-sul)  
Product Lead at SkilledUp.Life
