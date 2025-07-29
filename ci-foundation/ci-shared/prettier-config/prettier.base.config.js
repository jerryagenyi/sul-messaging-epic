// 🎨 SkilledUp Life Prettier Config – Shared Format Rules
// Copy this file to: .github/ci-shared/prettier-config/ in frontend/backend repos

module.exports = {
  // Basic formatting rules
  semi: false,
  singleQuote: true,
  printWidth: 100,
  trailingComma: 'es5',
  tabWidth: 2,
  useTabs: false,
  bracketSpacing: true,
  arrowParens: 'avoid',
  
  // File-specific overrides
  overrides: [
    {
      files: '*.vue',
      options: {
        parser: 'vue',
        htmlWhitespaceSensitivity: 'ignore'
      }
    },
    {
      files: '*.json',
      options: {
        parser: 'json'
      }
    }
  ]
}; 