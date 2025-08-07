// 🧪 User Journey E2E Test: Volunteer Onboarding
// Copy this file to: tests/e2e/user-journeys/volunteer-onboarding.spec.js in frontend repository

import { test, expect } from '@playwright/test'

test.describe('User Journey - Volunteer Onboarding', () => {
  test('complete volunteer onboarding flow', async ({ page }) => {
    // Step 1: Visit homepage
    await page.goto('/')
    await expect(page).toHaveTitle(/SkilledUp\.Life/)
    
    // Step 2: Click "Join as Volunteer"
    await page.click('[data-testid="join-volunteer-button"]')
    await expect(page).toHaveURL('/register/volunteer')
    
    // Step 3: Fill registration form
    await page.fill('[data-testid="first-name"]', 'John')
    await page.fill('[data-testid="last-name"]', 'Doe')
    await page.fill('[data-testid="email"]', 'john.doe@example.com')
    await page.fill('[data-testid="password"]', 'SecurePass123!')
    await page.fill('[data-testid="confirm-password"]', 'SecurePass123!')
    
    // Step 4: Submit registration
    await page.click('[data-testid="register-button"]')
    
    // Step 5: Verify email confirmation page
    await expect(page).toHaveURL('/verify-email')
    await expect(page.locator('[data-testid="verification-message"]')).toBeVisible()
    
    // Step 6: Complete profile setup (simulate email verification)
    await page.goto('/profile/setup')
    
    // Step 7: Fill profile information
    await page.fill('[data-testid="bio"]', 'Passionate about helping others learn and grow')
    await page.selectOption('[data-testid="location"]', 'London')
    await page.fill('[data-testid="phone"]', '+44 123 456 7890')
    
    // Step 8: Add skills
    await page.click('[data-testid="add-skill-button"]')
    await page.fill('[data-testid="skill-name"]', 'JavaScript')
    await page.selectOption('[data-testid="skill-level"]', 'intermediate')
    await page.click('[data-testid="save-skill-button"]')
    
    // Step 9: Upload profile picture
    await page.setInputFiles('[data-testid="profile-picture"]', 'tests/regression/fixtures/avatar.png')
    
    // Step 10: Complete onboarding
    await page.click('[data-testid="complete-profile-button"]')
    
    // Step 11: Verify redirect to dashboard
    await expect(page).toHaveURL('/dashboard')
    await expect(page.locator('[data-testid="welcome-message"]')).toBeVisible()
    
    // Step 12: Verify profile is complete
    await page.click('[data-testid="profile-menu"]')
    await page.click('[data-testid="view-profile"]')
    await expect(page.locator('[data-testid="profile-complete-badge"]')).toBeVisible()
  })

  test('should handle onboarding interruptions gracefully', async ({ page }) => {
    // Start onboarding
    await page.goto('/register/volunteer')
    await page.fill('[data-testid="first-name"]', 'Jane')
    await page.fill('[data-testid="last-name"]', 'Smith')
    await page.fill('[data-testid="email"]', 'jane.smith@example.com')
    await page.fill('[data-testid="password"]', 'SecurePass123!')
    await page.fill('[data-testid="confirm-password"]', 'SecurePass123!')
    
    // Navigate away (simulate interruption)
    await page.goto('/')
    
    // Return to onboarding - should resume where left off
    await page.goto('/register/volunteer')
    await expect(page.locator('[data-testid="first-name"]')).toHaveValue('Jane')
    await expect(page.locator('[data-testid="last-name"]')).toHaveValue('Smith')
  })
})
