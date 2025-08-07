# 🧪 Test Structure & Guidelines

This directory contains all tests for the SkilledUp.Life frontend application, organized for clarity and maintainability.

## 📁 Directory Structure

```
tests/
├── config/               # All test configurations
│   ├── vitest.config.js  # Unit & component testing
│   ├── playwright.config.js # E2E testing
│   └── setup.js         # Test setup and mocks
├── e2e/                  # End-to-end tests
│   ├── critical/        # Critical user flows (block PRs if failed)
│   └── user-journeys/   # Complete user journeys
├── components/           # Component tests
├── unit/                 # Utility & composable tests
└── regression/           # Regression snapshots & fixtures
    └── fixtures/        # Test data and files
```

## 🎯 Test Types

### **Unit Tests** (`tests/unit/`)
- **Purpose**: Test individual functions, utilities, and composables
- **Framework**: Vitest
- **Coverage**: Business logic, data transformations, API calls
- **Examples**: Auth utilities, form validation, data formatting

### **Component Tests** (`tests/components/`)
- **Purpose**: Test Vue components in isolation
- **Framework**: Vitest + Vue Test Utils
- **Coverage**: Component rendering, props, events, user interactions
- **Examples**: Button clicks, form submissions, conditional rendering

### **E2E Tests** (`tests/e2e/`)
- **Purpose**: Test complete user workflows
- **Framework**: Playwright
- **Coverage**: Full user journeys, critical paths, cross-browser compatibility

#### **Critical Tests** (`tests/e2e/critical/`)
- **Purpose**: Block PRs if failed
- **Examples**: Login, registration, payment flows
- **Tags**: `@critical`

#### **User Journeys** (`tests/e2e/user-journeys/`)
- **Purpose**: Test complete user workflows
- **Examples**: Volunteer onboarding, company registration
- **Tags**: `@user-journey`

## 🚀 Running Tests

### **Unit & Component Tests**
```bash
npm run test:unit
```

### **E2E Tests**
```bash
npm run test:e2e
```

### **Critical Tests Only**
```bash
npm run test:e2e:critical
```

### **All Tests**
```bash
npm run test
```

## 📝 Writing Tests

### **Unit Test Example**
```javascript
import { describe, it, expect } from 'vitest'
import { validateEmail } from '@/utils/auth'

describe('Auth Utilities', () => {
  it('should validate correct email formats', () => {
    expect(validateEmail('test@example.com')).toBe(true)
  })
})
```

### **Component Test Example**
```javascript
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import Button from '@/components/Button.vue'

describe('Button Component', () => {
  it('emits click event when clicked', async () => {
    const wrapper = mount(Button, {
      slots: { default: 'Click me' }
    })
    
    await wrapper.trigger('click')
    expect(wrapper.emitted('click')).toBeTruthy()
  })
})
```

### **E2E Test Example**
```javascript
import { test, expect } from '@playwright/test'

test('should allow valid user to login', async ({ page }) => {
  await page.goto('/login')
  await page.fill('[data-testid="email"]', 'test@example.com')
  await page.fill('[data-testid="password"]', 'password123')
  await page.click('[data-testid="login-button"]')
  
  await expect(page).toHaveURL('/dashboard')
})
```

## 🏷️ Test Tagging

Use tags to organize and filter tests:

- `@critical` - Must pass to merge PR
- `@unit` - Unit tests
- `@component` - Component tests
- `@e2e` - End-to-end tests
- `@user-journey` - Complete user workflows
- `@regression` - Regression tests

## 🔧 Configuration

### **Vitest Config** (`config/vitest.config.js`)
- Unit and component test configuration
- Coverage settings
- Path aliases
- Test environment setup

### **Playwright Config** (`config/playwright.config.js`)
- E2E test configuration
- Browser configurations
- Test timeouts
- Screenshot and video settings

### **Test Setup** (`config/setup.js`)
- Global mocks
- Browser API mocks
- Test utilities
- Environment setup

## 📊 Coverage

- **Unit Tests**: 70% minimum coverage
- **Component Tests**: Focus on critical components
- **E2E Tests**: Cover all critical user flows

## 🚨 Best Practices

1. **Use data-testid attributes** for reliable element selection
2. **Write descriptive test names** that explain the behavior
3. **Keep tests independent** - no shared state between tests
4. **Mock external dependencies** in unit tests
5. **Use page objects** for complex E2E tests
6. **Tag tests appropriately** for filtering and CI
7. **Write tests before fixing bugs** (TDD approach)

## 🔄 CI Integration

Tests run automatically on:
- **Pull Requests**: All tests
- **Main Branch**: Full test suite
- **Critical Tests**: Block PR merges if failed

## 📚 Resources

- [Vitest Documentation](https://vitest.dev/)
- [Vue Test Utils](https://test-utils.vuejs.org/)
- [Playwright Documentation](https://playwright.dev/)
- [Testing Best Practices](https://testing-library.com/docs/guiding-principles)
