# 🧪 Testing Strategy & Migration Guide

> **Complete guide for implementing comprehensive testing in SkilledUp.Life frontend**

---

## 🎯 **Testing Strategy & Priorities**

### **Recommended Testing Priority (Starters)**

#### **1. E2E Tests FIRST** (Critical Paths)
**Why start with E2E?**
- ✅ **Immediate value** - catches real user problems
- ✅ **Stakeholder confidence** - shows working features
- ✅ **Regression protection** - prevents breaking critical flows
- ✅ **Easier to write** - just simulate user actions

**Start with these critical flows:**
```typescript
// tests/e2e/critical/
├── auth-login.spec.ts        // Login → Dashboard
├── registration.spec.ts      // Sign up flow
├── profile-update.spec.ts    // Profile editing
└── dashboard-access.spec.ts  // Main dashboard
```

#### **2. Component Tests SECOND** (High-Impact Components)
**Why component tests next?**
- ✅ **Faster feedback** than E2E
- ✅ **Isolated testing** - easier to debug
- ✅ **Prevents component-level bugs**

#### **3. Unit Tests LAST** (Utilities & Composables)
**Why unit tests last?**
- ✅ **Most granular** - requires deep code understanding
- ✅ **Best for refactoring** - but you're building, not refactoring
- ✅ **Developers can write as they code** - perfect for ongoing development

### **Component Testing Strategy**

#### **How to Identify Components to Test**

**Step 1: Audit Your Components Folder**
```bash
# Look at your components structure
src/components/
├── forms/           # High priority - user input
│   ├── LoginForm.vue
│   ├── RegisterForm.vue
│   └── ProfileForm.vue
├── navigation/      # Medium priority - routing
│   ├── NavBar.vue
│   └── Sidebar.vue
├── layout/          # Low priority - mostly static
│   ├── Header.vue
│   └── Footer.vue
└── ui/              # Medium priority - reusable
    ├── Button.vue
    ├── Modal.vue
    └── Card.vue
```

**Step 2: Prioritize by User Impact**
```typescript
// HIGH PRIORITY (Test First)
- LoginForm.vue      // User can't access app if broken
- RegisterForm.vue   // User can't sign up if broken
- ProfileForm.vue    // User can't update profile if broken

// MEDIUM PRIORITY (Test Second)  
- NavBar.vue         // Navigation affects user experience
- Button.vue         // Reusable, used everywhere
- Modal.vue          // Common interaction pattern

// LOW PRIORITY (Test Last)
- Header.vue         // Mostly static content
- Footer.vue         // Mostly static content
```

### **E2E Testing Strategy**

#### **Test by User Stories, Not Technical Modules**

**Instead of testing by "Epic" (technical), test by "User Journey" (business):**

```typescript
// tests/e2e/user-journeys/
├── volunteer-onboarding.spec.ts    // Registration → Profile → Dashboard
├── company-dashboard.spec.ts       // Company user workflows
├── skill-matching.spec.ts          // Skill search and matching
├── messaging.spec.ts               // Communication flows
└── admin-management.spec.ts        // Admin user workflows
```

---

## 🔄 **Migration Implementation**

### **📋 Migration Checklist**

#### **✅ 1. Create New Directory Structure**

```bash
# In your frontend repository root
mkdir -p tests/{config,e2e/{critical,user-journeys},components,unit,regression/fixtures}
```

#### **✅ 2. Copy Configuration Files**

```bash
# Copy config files from staging repo to your frontend repo
cp ci-structure/ci-shared/tests/config/vitest.config.js tests/config/
cp ci-structure/ci-shared/tests/config/playwright.config.js tests/config/
cp ci-structure/ci-shared/tests/config/setup.js tests/config/
```

#### **✅ 3. Move Existing Test Files**

```bash
# Move existing unit tests
mv tests/unit/* tests/unit/ 2>/dev/null || echo "No existing unit tests"

# Move existing component tests
mv tests/components/* tests/components/ 2>/dev/null || echo "No existing component tests"

# Move existing E2E tests
mv tests/e2e/* tests/e2e/ 2>/dev/null || echo "No existing E2E tests"
```

#### **✅ 4. Update Package.json Scripts**

Replace your existing test scripts with the new ones:

```json
{
  "scripts": {
    "test": "npm run test:unit && npm run test:e2e",
    "test:unit": "vitest --config tests/config/vitest.config.js",
    "test:unit:watch": "vitest --config tests/config/vitest.config.js --watch",
    "test:unit:coverage": "vitest --config tests/config/vitest.config.js --coverage",
    "test:components": "vitest --config tests/config/vitest.config.js tests/components/",
    "test:e2e": "playwright test --config tests/config/playwright.config.js",
    "test:e2e:watch": "playwright test --config tests/config/playwright.config.js --headed",
    "test:e2e:critical": "playwright test --config tests/config/playwright.config.js --grep @critical",
    "test:e2e:debug": "playwright test --config tests/config/playwright.config.js --debug"
  }
}
```

#### **✅ 5. Install New Dependencies**

```bash
# Install Vitest (replaces Jest)
npm install --save-dev vitest @vitejs/plugin-vue jsdom

# Install Playwright (if not already installed)
npm install --save-dev @playwright/test

# Install Vue Test Utils (for component testing)
npm install --save-dev @vue/test-utils
```

#### **✅ 6. Update CI Workflow**

Update your `.github/workflows/ci-frontend.yml` to use the new paths:

```yaml
# Unit tests
- name: Run unit tests
  run: npm run test:unit

# E2E tests
- name: Run E2E tests
  run: npm run test:e2e
```

#### **✅ 7. Remove Old Files**

```bash
# Remove old Jest config (if exists)
rm -f jest.config.js
rm -f .github/ci-shared/test-config/jest.vue.config.js

# Remove old test directories (if empty)
rmdir tests/old-unit 2>/dev/null || echo "Directory not empty or doesn't exist"
rmdir tests/old-e2e 2>/dev/null || echo "Directory not empty or doesn't exist"
```

---

## 🛠️ **Implementation Timeline**

### **Week 1–2: E2E Foundation**
```bash
npm install -D @playwright/test
tests/e2e/critical/
├── auth-login.spec.ts
├── registration.spec.ts
└── dashboard-access.spec.ts
```

### **Week 3–4: Component Testing**
```bash
npm install -D @vue/test-utils @testing-library/vue
tests/components/forms/
├── LoginForm.spec.ts
├── RegisterForm.spec.ts
tests/components/ui/
└── Button.spec.ts
```

### **Week 5+: Unit Tests (Ongoing)**
```bash
tests/unit/composables/
├── useAuth.spec.ts
├── useProfile.spec.ts
tests/unit/utils/
├── validation.spec.ts
└── formatting.spec.ts
```

---

## 🔧 **Configuration Updates**

### **Vitest Configuration**

The new `tests/config/vitest.config.js` includes:
- Vue plugin for component testing
- JSDOM environment
- Path aliases (`@` points to `src/`)
- Coverage configuration
- Test file patterns

### **Playwright Configuration**

The new `tests/config/playwright.config.js` includes:
- Updated test directory path (`../e2e`)
- Browser configurations
- Screenshot and video settings
- Test timeouts

### **Test Setup**

The new `tests/config/setup.js` includes:
- Browser API mocks (ResizeObserver, IntersectionObserver)
- Storage mocks (localStorage, sessionStorage)
- Fetch mock
- Global test utilities

---

## 📝 **Test Writing Guidelines**

### **Unit Test Example**
```javascript
// tests/unit/auth.spec.js
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
// tests/components/Button.spec.js
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
// tests/e2e/critical/login.spec.js
import { test, expect } from '@playwright/test'

test('should allow valid user to login', async ({ page }) => {
  await page.goto('/login')
  await page.fill('[data-testid="email"]', 'test@example.com')
  await page.fill('[data-testid="password"]', 'password123')
  await page.click('[data-testid="login-button"]')
  
  await expect(page).toHaveURL('/dashboard')
})
```

---

## 🚨 **Common Issues & Solutions**

### **Issue: Tests not found**
**Solution**: Ensure test files match the patterns in `vitest.config.js`:
- Unit tests: `tests/unit/**/*.{test,spec}.{js,ts}`
- Component tests: `tests/components/**/*.{test,spec}.{js,ts}`

### **Issue: Path aliases not working**
**Solution**: Check that `@` alias is configured in both Vite and Vitest configs.

### **Issue: Playwright tests not running**
**Solution**: Ensure Playwright is installed and browsers are downloaded:
```bash
npm run playwright:install
```

### **Issue: Component tests failing**
**Solution**: Ensure Vue Test Utils is installed and Vue plugin is configured in Vitest.

---

## ✅ **Verification Steps**

1. **Run unit tests**: `npm run test:unit`
2. **Run component tests**: `npm run test:components`
3. **Run E2E tests**: `npm run test:e2e`
4. **Check coverage**: `npm run test:unit:coverage`
5. **Verify CI**: Push changes and check GitHub Actions

---

## 📚 **Additional Resources**

- [Vitest Documentation](https://vitest.dev/)
- [Vue Test Utils](https://test-utils.vuejs.org/)
- [Playwright Documentation](https://playwright.dev/)
- [Test Structure README](./tests/README.md)
