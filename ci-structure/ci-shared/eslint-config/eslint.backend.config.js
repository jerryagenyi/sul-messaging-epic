// 🔧 SkilledUp Life ESLint Config – Backend
// Copy this file to: .github/ci-shared/eslint.backend.config.js in backend repository

module.exports = {
  root: true,
  env: {
    node: true,
    es2021: true
  },
  extends: [
    'eslint:recommended',
    'prettier'
  ],
  rules: {
    // Code quality rules
    'no-console': 'warn',
    'no-unused-vars': 'warn',
    'no-undef': 'error',
    
    // Best practices
    'prefer-const': 'error',
    'no-var': 'error',
    'eqeqeq': 'error',
    
    // Laravel-specific considerations
    'no-global-assign': 'error',
    'no-implied-eval': 'error'
  },
  parserOptions: {
    ecmaVersion: 2021,
    sourceType: 'module'
  },
  // Ignore Laravel-specific patterns
  ignorePatterns: [
    'vendor/**/*',
    'storage/**/*',
    'bootstrap/cache/**/*'
  ]
}; 