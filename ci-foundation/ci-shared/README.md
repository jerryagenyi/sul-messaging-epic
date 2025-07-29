# 📦 SkilledUp Life CI Shared Config – Philosophy & Usage

This folder contains configuration files designed to be reused across SkilledUp Life repositories. All files should be copied into `.github/ci-shared/` folders in the production repositories.

## 📐 Naming Convention

Files follow the pattern: `tool.module.config.js`

Examples:
- `eslint.vue.config.js` – Vue + ESLint ruleset
- `prettier.base.config.js` – Shared Prettier formatting
- `jest.vue.config.js` – (Future) Vue unit testing

## 🧠 Educational Design

Each config file includes:
- Sample `module.exports` structure
- Comment headers showing where they should live in production
- Inline explanations if needed

This folder is optimized to teach and scale:
- ✅ Reduce CI drift across repos
- ✅ Improve onboarding for rotating contributors
- ✅ Create clarity without needing external docs

## 🛠 Usage Notes

- Don't use `../../` paths when extending configs in `.eslintrc.js`. Instead, copy files into production repo's structure.
- Modify only the local `.eslintrc.js` or `prettier.config.js` to add repo-specific overrides.

## 💡 Example Usage

```js
module.exports = {
  ...require('./.github/ci-shared/eslint-config/eslint.vue.config'),
  // Optional overrides here
};
```

## 📁 Folder Structure

```
ci-shared/
├── eslint-config/
│   ├── eslint.vue.config.js
│   └── eslint.backend.config.js
├── prettier-config/
│   └── prettier.base.config.js
└── test-config/
    └── jest.vue.config.js         # For future use
```

## 🧪 Future: Unit Testing Presets

- `jest.vue.config.js` staged for Vue-based unit testing
- Intended to be copied into: `.github/ci-shared/test-config/`
- Will be activated when CI pipeline reaches unit testing phase

---

## 🚧 Repository Context

This configuration lives in the staging repository:
`https://github.com/jerryagenyi/skilleduplife-ci`

It is designed for transfer into:

- Frontend: [`https://github.com/skilleduplife/frontend`](https://github.com/skilleduplife/frontend)
- Backend: [`https://github.com/skilleduplife/backend`](https://github.com/skilleduplife/backend)

Please adjust file paths to reflect `.github/ci-shared/` folder within each repo.

See [`ci_shared_setup_checklist.md`](./ci_shared_setup_checklist.md) for detailed implementation steps. 