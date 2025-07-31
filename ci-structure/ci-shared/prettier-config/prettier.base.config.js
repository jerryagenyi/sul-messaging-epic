// 🎨 SkilledUp Life Prettier Config – Base Template
// Copy this file to: .github/ci-shared/prettier-config/prettier.frontend.config.js or prettier.backend.config.js in production repos

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
  arrowParens: 'avoid', // Supports Vue 3 composition API arrow functions; see comment below
  
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
  // Note: arrowParens: 'avoid' aligns with Vue 3's preference for concise arrow functions in the composition API.
}; 