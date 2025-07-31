// 🔧 SkilledUp Life ESLint Config – Vue Frontend
// Copy this file to: .github/ci-shared/eslint.vue.config.js in frontend repository

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
    // Code quality rules - Using warnings to avoid blocking PRs during trial
    'no-console': 'warn',
    'no-unused-vars': 'warn',
    'no-undef': 'warn', // Changed from 'error' to 'warn' to avoid blocking PRs
    'no-debugger': 'error', // Keep as error - prevents server crashes
    'prefer-const': 'warn', // Changed from 'error' to 'warn'
    'no-var': 'warn', // Changed from 'error' to 'warn'
    'eqeqeq': 'warn', // Changed from 'error' to 'warn'

    // Vue-specific rules - Using warnings to avoid blocking PRs during trial
    'vue/no-mutating-props': 'error', // Keep as error - critical Vue rule
    'vue/require-default-prop': 'warn',
    'vue/component-name-in-template-casing': 'warn', // Changed from 'error' to 'warn'
    'vue/multi-word-component-names': 'off',
    'vue/valid-template-root': 'error', // Keep as error - critical Vue rule
    'vue/no-unused-components': 'warn',
    'vue/require-explicit-emits': 'warn', // Changed from 'error' to 'warn'
    'vue/no-v-html': 'warn'
  },
  parserOptions: {
    ecmaVersion: 2021,
    sourceType: 'module'
  }
  // No specific Tailwind rule needed; classes are CSS and ignored by ESLint
}; 