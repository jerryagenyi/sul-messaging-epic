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
                'no-debugger': 'error', // Prevents server crashes
                'prefer-const': 'error',
                'no-var': 'error',
                'eqeqeq': 'error',

                // Vue-specific rules
                'vue/no-mutating-props': 'error',
                'vue/require-default-prop': 'warn',
                'vue/component-name-in-template-casing': ['error', 'PascalCase'],
                'vue/multi-word-component-names': 'off',
                'vue/valid-template-root': 'error',
                'vue/no-unused-components': 'warn', // Catches unused components
                'vue/require-explicit-emits': 'error', // Vue 3 composition API support
                'vue/no-v-html': 'warn' // Prevents XSS risks
              },
  parserOptions: {
    ecmaVersion: 2021,
    sourceType: 'module'
  }
  // No specific Tailwind rule needed; classes are CSS and ignored by ESLint
}; 