// 🧪 SkilledUp Life Vitest Config – Vue Frontend Unit & Component Tests
// Copy this file to: tests/config/vitest.config.js in frontend repository

import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

export default defineConfig({
  plugins: [vue()],
  
  test: {
    // Test environment
    environment: 'jsdom',
    
    // File patterns
    include: [
      'tests/unit/**/*.{test,spec}.{js,ts}',
      'tests/components/**/*.{test,spec}.{js,ts}'
    ],
    
    // Coverage configuration
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: [
        'node_modules/',
        'tests/',
        '**/*.d.ts',
        'src/main.js',
        'src/router/index.js'
      ],
      thresholds: {
        global: {
          branches: 70,
          functions: 70,
          lines: 70,
          statements: 70
        }
      }
    },
    
    // Test setup
    setupFiles: ['./tests/config/setup.js'],
    
    // Global test timeout
    testTimeout: 10000,
    
    // Hook timeout
    hookTimeout: 10000
  },
  
  resolve: {
    alias: {
      '@': resolve(__dirname, '../src')
    }
  }
})
