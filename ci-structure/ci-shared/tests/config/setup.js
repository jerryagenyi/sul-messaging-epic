// 🧪 Test Setup File – Global Mocks & Configurations
// Copy this file to: tests/config/setup.js in frontend repository

import { vi } from 'vitest'

// Mock browser APIs that aren't available in jsdom
global.ResizeObserver = vi.fn().mockImplementation(() => ({
  observe: vi.fn(),
  unobserve: vi.fn(),
  disconnect: vi.fn(),
}))

global.IntersectionObserver = vi.fn().mockImplementation(() => ({
  observe: vi.fn(),
  unobserve: vi.fn(),
  disconnect: vi.fn(),
}))

// Mock localStorage
const localStorageMock = {
  getItem: vi.fn(),
  setItem: vi.fn(),
  removeItem: vi.fn(),
  clear: vi.fn(),
}
global.localStorage = localStorageMock

// Mock sessionStorage
const sessionStorageMock = {
  getItem: vi.fn(),
  setItem: vi.fn(),
  removeItem: vi.fn(),
  clear: vi.fn(),
}
global.sessionStorage = sessionStorageMock

// Mock fetch
global.fetch = vi.fn()

// Mock console methods in tests (optional - remove if you want to see console output)
// global.console = {
//   ...console,
//   log: vi.fn(),
//   debug: vi.fn(),
//   info: vi.fn(),
//   warn: vi.fn(),
//   error: vi.fn(),
// }

// Global test utilities
global.testUtils = {
  // Helper to wait for next tick
  nextTick: () => new Promise(resolve => setTimeout(resolve, 0)),
  
  // Helper to wait for a specific time
  waitFor: (ms) => new Promise(resolve => setTimeout(resolve, ms)),
  
  // Helper to create mock user data
  createMockUser: (overrides = {}) => ({
    id: 1,
    name: 'Test User',
    email: 'test@example.com',
    role: 'volunteer',
    ...overrides
  })
}
