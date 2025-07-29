# ESLint Rules for SkilledUp.Life

This folder contains shared ESLint configurations for frontend modules.  
See `ci_setup_checklist.md` for active rule setup.  
Future improvements will include scoped rules by module type.

## 📁 Contents

_Configuration files will be added here as the foundation evolves._

### Planned Examples

- **Base Configuration** - Standard ESLint setup for all projects
- **Vue.js Specific** - Vue 3 component and template rules
- **Laravel Frontend** - JavaScript rules for Laravel Blade templates
- **TypeScript Support** - TypeScript-specific linting rules
- **Team Customizations** - Project-specific rule modifications

## 🔧 Usage

1. Copy the relevant configuration file to your project
2. Customize rules based on your team's preferences
3. Document any deviations from the foundation standards
4. Share improvements back to the foundation

## 📚 Documentation

- **[Getting Started Guide](../getting-started-ci.md)** - ESLint setup instructions
- **[Setup Checklist](../ci-setup-checklist.md)** - Complete implementation guide
- **[Vue.js Rules](../ci-setup-checklist.md#vue-specific-eslint--prettier-rules)** - Vue-specific configuration

---

## 📐 Configuration Strategy

We may eventually scope ESLint rules by module type:
- Shared base rules will live in this folder
- Module-specific overrides will be imported via `.eslintrc.js` using:

```js
module.exports = {
  ...require('./.github/ci-shared/eslint-config/eslint.vue.config'),
  // Add module-specific overrides here
}
```

Examples include stricter linting for backend APIs, relaxed rules for prototypes, etc.

See `ci_setup_checklist.md` for current rules in use.

---

_This folder is part of the SkilledUp.Life CI/CD Foundation. Contributions welcome!_
