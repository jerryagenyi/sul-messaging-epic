# 📦 Package.json Scripts Template

Add these scripts to your `package.json` to work with the new test structure:

## 🧪 Test Scripts

```json
{
  "scripts": {
    // Existing scripts
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "lint": "eslint src/ tests/ *.js --ext .js,.vue",
    "format": "prettier --check src/ tests/ *.js",
    "format:fix": "prettier --write src/ tests/ *.js",
    
    // Test scripts
    "test": "npm run test:unit && npm run test:e2e",
    "test:unit": "vitest --config tests/config/vitest.config.js",
    "test:unit:watch": "vitest --config tests/config/vitest.config.js --watch",
    "test:unit:coverage": "vitest --config tests/config/vitest.config.js --coverage",
    "test:components": "vitest --config tests/config/vitest.config.js tests/components/",
    "test:e2e": "playwright test --config tests/config/playwright.config.js",
    "test:e2e:watch": "playwright test --config tests/config/playwright.config.js --headed",
    "test:e2e:critical": "playwright test --config tests/config/playwright.config.js --grep @critical",
    "test:e2e:debug": "playwright test --config tests/config/playwright.config.js --debug",
    
    // Playwright utilities
    "playwright:install": "playwright install --with-deps",
    "playwright:codegen": "playwright codegen",
    "playwright:show-report": "playwright show-report"
  }
}
```

## 🔧 Development Scripts

```json
{
  "scripts": {
    // Development helpers
    "test:watch": "npm run test:unit:watch",
    "test:quick": "npm run test:unit",
    "test:full": "npm run test",
    "test:ci": "npm run test:unit:coverage && npm run test:e2e:critical"
  }
}
```

## 📊 Coverage Scripts

```json
{
  "scripts": {
    // Coverage reporting
    "coverage": "npm run test:unit:coverage",
    "coverage:report": "npm run test:unit:coverage && open coverage/index.html",
    "coverage:ci": "npm run test:unit:coverage -- --reporter=lcov"
  }
}
```

## 🚀 Complete Example

Here's a complete `package.json` scripts section:

```json
{
  "name": "skilleduplife-frontend",
  "version": "1.0.0",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "lint": "eslint src/ tests/ *.js --ext .js,.vue",
    "lint:fix": "eslint src/ tests/ *.js --ext .js,.vue --fix",
    "format": "prettier --check src/ tests/ *.js",
    "format:fix": "prettier --write src/ tests/ *.js",
    
    "test": "npm run test:unit && npm run test:e2e",
    "test:unit": "vitest --config tests/config/vitest.config.js",
    "test:unit:watch": "vitest --config tests/config/vitest.config.js --watch",
    "test:unit:coverage": "vitest --config tests/config/vitest.config.js --coverage",
    "test:components": "vitest --config tests/config/vitest.config.js tests/components/",
    "test:e2e": "playwright test --config tests/config/playwright.config.js",
    "test:e2e:watch": "playwright test --config tests/config/playwright.config.js --headed",
    "test:e2e:critical": "playwright test --config tests/config/playwright.config.js --grep @critical",
    "test:e2e:debug": "playwright test --config tests/config/playwright.config.js --debug",
    
    "playwright:install": "playwright install --with-deps",
    "playwright:codegen": "playwright codegen",
    "playwright:show-report": "playwright show-report",
    
    "test:watch": "npm run test:unit:watch",
    "test:quick": "npm run test:unit",
    "test:full": "npm run test",
    "test:ci": "npm run test:unit:coverage && npm run test:e2e:critical",
    
    "coverage": "npm run test:unit:coverage",
    "coverage:report": "npm run test:unit:coverage && open coverage/index.html",
    "coverage:ci": "npm run test:unit:coverage -- --reporter=lcov"
  }
}
```

## 📝 Usage Examples

### **Development Workflow**
```bash
# Run unit tests in watch mode
npm run test:watch

# Run quick unit tests
npm run test:quick

# Run all tests
npm run test:full
```

### **CI/CD Workflow**
```bash
# Run tests for CI (coverage + critical E2E)
npm run test:ci

# Run only critical E2E tests
npm run test:e2e:critical
```

### **Debugging**
```bash
# Debug E2E tests
npm run test:e2e:debug

# Generate Playwright tests
npm run playwright:codegen
```

### **Coverage**
```bash
# Generate coverage report
npm run coverage

# Open coverage report in browser
npm run coverage:report
```
