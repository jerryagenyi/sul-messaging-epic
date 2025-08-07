// 🧪 Critical E2E Test: Login Functionality
// Copy this file to: tests/e2e/critical/login.spec.js in frontend repository

import { test, expect } from '@playwright/test'

test.describe('Critical User Flows - Login', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login')
  })

  test('should allow valid user to login', async ({ page }) => {
    // Fill in login form
    await page.fill('[data-testid="email-input"]', 'test@example.com')
    await page.fill('[data-testid="password-input"]', 'password123')
    
    // Submit form
    await page.click('[data-testid="login-button"]')
    
    // Verify redirect to dashboard
    await expect(page).toHaveURL('/dashboard')
    
    // Verify user is logged in
    await expect(page.locator('[data-testid="user-menu"]')).toBeVisible()
  })

  test('should show error for invalid credentials', async ({ page }) => {
    // Fill in invalid credentials
    await page.fill('[data-testid="email-input"]', 'invalid@example.com')
    await page.fill('[data-testid="password-input"]', 'wrongpassword')
    
    // Submit form
    await page.click('[data-testid="login-button"]')
    
    // Verify error message
    await expect(page.locator('[data-testid="error-message"]')).toBeVisible()
    await expect(page.locator('[data-testid="error-message"]')).toContainText('Invalid credentials')
    
    // Verify still on login page
    await expect(page).toHaveURL('/login')
  })

  test('should validate required fields', async ({ page }) => {
    // Try to submit empty form
    await page.click('[data-testid="login-button"]')
    
    // Verify validation messages
    await expect(page.locator('[data-testid="email-error"]')).toBeVisible()
    await expect(page.locator('[data-testid="password-error"]')).toBeVisible()
  })

  test('should handle network errors gracefully', async ({ page }) => {
    // Mock network failure
    await page.route('**/api/login', route => route.abort())
    
    // Fill in form
    await page.fill('[data-testid="email-input"]', 'test@example.com')
    await page.fill('[data-testid="password-input"]', 'password123')
    
    // Submit form
    await page.click('[data-testid="login-button"]')
    
    // Verify error handling
    await expect(page.locator('[data-testid="error-message"]')).toBeVisible()
    await expect(page.locator('[data-testid="error-message"]')).toContainText('Network error')
  })
})
