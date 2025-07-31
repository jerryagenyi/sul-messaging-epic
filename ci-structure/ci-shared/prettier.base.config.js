// 🎨 SkilledUp Life Prettier Config – Shared Format Rules
// Copy this file to: .github/ci-shared/prettier.base.config.js in frontend/backend repos

module.exports = {
  // Schema reference for IDE support
  $schema: 'https://json.schemastore.org/prettierrc',
  
  // Basic formatting rules (aligned with your current config)
  semi: false,
  singleQuote: true,
  printWidth: 120,
  tabWidth: 4,
  trailingComma: 'none',
  useTabs: false,
  bracketSpacing: true,
  arrowParens: 'avoid',
  
  // HTML/Vue specific settings
  htmlWhitespaceSensitivity: 'ignore',
  
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
    },
    {
      files: '*.php',
      options: {
        parser: 'php'
      }
    }
  ]
}; 