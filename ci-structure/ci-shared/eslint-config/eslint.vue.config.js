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
                // Code quality rules
                'no-console': 'warn',
                'no-unused-vars': 'warn',
                'no-undef': 'error',
                'no-debugger': 'error', // Prevent server crashes

                // Vue-specific rules
                'vue/no-mutating-props': 'error',
                'vue/require-default-prop': 'warn',
                'vue/component-name-in-template-casing': ['error', 'PascalCase'],
                'vue/multi-word-component-names': 'off',
                'vue/valid-template-root': 'error',
                'vue/no-unused-components': 'warn', // Vue 3 best practice
                'vue/require-explicit-emits': 'warn', // Vue 3 composition API

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