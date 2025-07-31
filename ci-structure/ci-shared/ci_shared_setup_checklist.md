# ✅ CI Shared Config Setup Checklist (SkilledUp Life – ESLint/Prettier/Test)

This checklist guides you in setting up shared CI configuration files from staging repo [`skilleduplife-ci`](https://github.com/jerryagenyi/skilleduplife-ci) into the production repositories:

- **Frontend (Vue):** [`https://github.com/skilleduplife/frontend`](https://github.com/skilleduplife/frontend)
- **Backend (Laravel):** [`https://github.com/skilleduplife/backend`](https://github.com/skilleduplife/backend)

---

## 📁 1. Create Target Folder Structure in Live Repo(s)

Create this path in each production repo:

```bash
.github/ci-shared/
├── eslint-config/
├── prettier-config/
└── test-config/           # For future use
```

✅ Use the `tool.module.config.js` naming pattern for clarity

---

## 📄 2. Copy Staging Config Files Into Production Repos

From: `skilleduplife-ci/ci-structure/ci-shared/`  
To:
- Frontend → `.github/ci-shared/` in Vue repo
- Backend → `.github/ci-shared/` in Laravel repo

| File                         | Destination Path                                                                   |
|-----------------------------|-------------------------------------------------------------------------------------|
| eslint.vue.config.js        | frontend/.github/ci-shared/eslint-config/eslint.vue.config.js                      |
| eslint.backend.config.js    | backend/.github/ci-shared/eslint-config/eslint.backend.config.js                   |
| prettier.shared.config.js     | frontend/.github/ci-shared/prettier-config/prettier.shared.config.js (also backend)  |
| jest.vue.config.js          | frontend/.github/ci-shared/test-config/jest.vue.config.js (future use)             |

---

## 🧠 3. Update `.eslintrc.js` in Production Repo

Example for Vue modules (inside frontend):

```js
module.exports = {
  ...require('./.github/ci-shared/eslint-config/eslint.vue.config'),
  // Add module-specific overrides here
}
```

⚠️ Avoid `../../` path references — assume config files live locally inside production repo structure.

---

## 🎨 4. Update `.prettierrc` or `prettier.config.js` References

Use this import syntax:

```js
module.exports = {
  ...require('./.github/ci-shared/prettier-config/prettier.shared.config'),
  // Project-specific overrides here
}
```

---

## 🧪 5. Plan for Future Testing Preset Integration

In `ci-shared/test-config/`, keep `jest.vue.config.js` as a placeholder with comments for future use. Add roadmap note in staging repo's README:

```md
🧪 Future: Unit Testing Presets

- `jest.vue.config.js` staged for Vue-based unit testing
- Intended to be copied into: `.github/ci-shared/test-config/`
```

---

## 🗣️ 6. Update Staging Repo Comments to Guide Usage

In the header of each config file, include where the file should eventually live:

```js
// 🔧 SkilledUp Life ESLint Config – Vue Frontend
// Copy this file to: skilleduplife/frontend/.github/ci-shared/eslint-config/
```

---

## 📢 7. Echo These Steps in Staging Repo Docs

In `ci-shared/README.md`, ensure this content is reflected:
- Purpose of `ci-shared/`
- File naming convention
- Implementation examples
- Future plan notes

---

## 🚀 Quick Implementation Commands

### Frontend Repo Setup:
```bash
# Create folder structure
mkdir -p .github/ci-shared/{eslint-config,prettier-config,test-config}

# Copy config files (adjust paths as needed)
cp ../../skilleduplife-ci/ci-structure/ci-shared/eslint-config/eslint.vue.config.js .github/ci-shared/eslint-config/
cp ../../skilleduplife-ci/ci-structure/ci-shared/prettier-config/prettier.shared.config.js .github/ci-shared/prettier-config/
cp ../../skilleduplife-ci/ci-structure/ci-shared/test-config/jest.vue.config.js .github/ci-shared/test-config/

# Update .eslintrc.js
echo "module.exports = {
  ...require('./.github/ci-shared/eslint-config/eslint.vue.config'),
  // Add module-specific overrides here
}" > .eslintrc.js
```

### Backend Repo Setup:
```bash
# Create folder structure
mkdir -p .github/ci-shared/{eslint-config,prettier-config}

# Copy config files
cp ../../skilleduplife-ci/ci-structure/ci-shared/eslint-config/eslint.backend.config.js .github/ci-shared/eslint-config/
cp ../../skilleduplife-ci/ci-structure/ci-shared/prettier-config/prettier.shared.config.js .github/ci-shared/prettier-config/
```

---

## ✅ Validation Checklist

- [ ] Folder structure created in production repo
- [ ] Config files copied with correct naming
- [ ] `.eslintrc.js` updated to reference shared configs
- [ ] `.prettierrc` or `prettier.config.js` updated
- [ ] Local overrides added if needed
- [ ] CI pipeline tests pass with new configs
- [ ] Documentation updated to reflect new structure

---

## 🔄 Future Migration Notes

When migrating configs, consider adding this comment to copied files:
```js
// ✅ Confirmed migrated from ci-staging
// Original: skilleduplife-ci/ci-structure/ci-shared/
// Destination: .github/ci-shared/ in production repos
// Migrated: [DATE] by [CONTRIBUTOR]
```

This helps track the source and reduces future repo diff confusion. 