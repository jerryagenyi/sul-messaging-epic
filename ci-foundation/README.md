# ⚙️ SkilledUp.Life CI/CD Foundation

## 🔍 Purpose

This folder contains the standardized CI/CD configurations, workflows, and setup guides used across SkilledUp.Life projects. It is designed to enforce consistency and automation for both frontend (Vue) and backend (Laravel) codebases.

👉 Original focus on the Messaging Epic (TDD/BDD) remains documented in the main repo for future reference.

---

## 📂 Contents

- `ci-setup-checklist.md` — Step-by-step CI setup instructions
- `workflow-templates/` — GitHub Actions workflows for Vue & Laravel
- `eslint-config/` — Reusable ESLint rules (to be added)
- `prettier-config/` — Prettier formatting standards (to be added)
- `README.md` — This document

---

## 🛠️ Setup Summary

1. Run `npm install` in your local frontend repo.
2. Verify and commit `.prettierrc`, `.eslintrc`, and updated `package.json`.
3. Trigger workflow via PR → `main` to see CI in action.
4. Add test coverage and track it via linked sheet.

Refer to [CI Setup Checklist](./ci-setup-checklist.md) for full instructions.

---

## 🚀 Future Plans

- Add templates for test runners (Jest, Playwright)
- Extend workflows to integrate coverage reports
- Modularize CI setups for component-level enforcement

---

## 👤 Maintainer

Built and curated by [@jerryagenyi](https://github.com/jerryagenyi)  
Product Lead at SkilledUp.Life
