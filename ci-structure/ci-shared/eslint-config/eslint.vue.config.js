// 🔧 SkilledUp Life ESLint Config – Vue Frontend
// Copy this file to: skilleduplife/frontend/.github/ci-shared/eslint-config/

module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
    es2021: true
  },
  extends: [
    'eslint:recommended',
    'plugin:vue/vue3-recommended',
    'prettier'
  ],
  rules: {
    // Code quality rules
    'no-console': 'warn',
    'no-unused-vars': 'warn',
    'no-undef': 'error',
    
    // Vue-specific rules
    'vue/no-mutating-props': 'error',
    'vue/require-default-prop': 'warn',
    'vue/component-name-in-template-casing': ['error', 'PascalCase'],
    'vue/multi-word-component-names': 'off',
    'vue/valid-template-root': 'error',
    
    // Best practices
    'prefer-const': 'error',
    'no-var': 'error',
    'eqeqeq': 'error'
  },
  parserOptions: {
    ecmaVersion: 2021,
    sourceType: 'module'
  }
}; 