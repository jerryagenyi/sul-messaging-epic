// 🧪 SkilledUp Life Jest Config – Vue Frontend Unit Tests
// Copy this file to: .github/ci-shared/jest.vue.config.js in frontend repository

module.exports = {
  // Jest presets for Vue component testing
  preset: '@vue/cli-plugin-unit-jest',
  
  // Test environment
  testEnvironment: 'jsdom',
  
  // File patterns
  testMatch: [
    '**/tests/unit/**/*.spec.[jt]s?(x)',
    '**/__tests__/*.[jt]s?(x)',
    '**/*.(test|spec).[jt]s?(x)'
  ],
  
  // Coverage configuration
  collectCoverageFrom: [
    'src/**/*.{js,vue}',
    '!src/main.js',
    '!src/router/index.js',
    '!**/node_modules/**'
  ],
  
  // Coverage thresholds
  coverageThreshold: {
    global: {
      branches: 70,
      functions: 70,
      lines: 70,
      statements: 70
    }
  },
  
  // Module name mapping
  moduleNameMapping: {
    '^@/(.*)$': '<rootDir>/src/$1'
  },
  
  // Transform configuration
  transform: {
    '^.+\\.vue$': '@vue/vue3-jest',
    '^.+\\js$': 'babel-jest'
  }
}; 