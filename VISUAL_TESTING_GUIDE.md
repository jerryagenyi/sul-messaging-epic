# Visual Testing Guide for Messaging Epic

This guide explains how to add visual design testing to complement the functional test suite.

## 🎨 Visual Testing Overview

The current test suite covers **functional behavior** but not **visual appearance**. This guide shows how to add visual regression testing for design consistency.

## 🔍 What Visual Testing Covers

### ✅ **Visual Elements:**
- **Colors & Themes**: Brand colors, dark/light mode
- **Typography**: Fonts, sizes, line heights, spacing
- **Layout & Positioning**: Element alignment, responsive breakpoints
- **Spacing & Margins**: Consistent padding, margins, gaps
- **Component States**: Hover, focus, active, disabled states
- **Animations**: Transitions, loading states, micro-interactions

### ✅ **Design Consistency:**
- **Brand Guidelines**: Logo placement, color usage
- **Component Library**: Consistent button styles, form elements
- **Responsive Design**: Mobile, tablet, desktop layouts
- **Accessibility**: Color contrast, focus indicators

## 🛠️ Implementation Options

### Option 1: Percy Visual Testing (Recommended)

#### Setup:
```bash
# Install Percy
npm install --save-dev @percy/selenium-js @percy/cli

# Add to requirements.txt
echo "percy-selenium==1.0.4" >> requirements.txt
pip install percy-selenium
```

#### Integration with Existing Tests:
```python
# In tests/conftest.py
import percy
from percy import percy_screenshot

@pytest.fixture(scope="session")
def percy_driver(driver):
    """Percy-enabled WebDriver"""
    return percy.percy_selenium(driver)

# In test files
def test_messaging_interface_visual(driver, wait, messaging_interface, percy_driver):
    """Visual test for messaging interface"""
    messaging_interface('pro_volunteer', 'test_company_001')
    
    # Take Percy screenshot
    percy_screenshot(driver, 'Messaging Interface - Default State')
    
    # Test different states
    message_input = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "message-input")
    ))
    message_input.send_keys("Test message")
    percy_screenshot(driver, 'Messaging Interface - With Text Input')
```

#### CI/CD Integration:
```yaml
# Add to .github/workflows/ci.yml
- name: Run Visual Tests
  env:
    PERCY_TOKEN: ${{ secrets.PERCY_TOKEN }}
  run: |
    npx percy exec -- python run_tests.py --marker visual
```

### Option 2: Applitools Eyes

#### Setup:
```bash
pip install eyes-selenium
```

#### Implementation:
```python
from applitools.selenium import Eyes, Target

@pytest.fixture(scope="session")
def eyes():
    eyes = Eyes()
    eyes.api_key = os.environ['APPLITOOLS_API_KEY']
    yield eyes
    eyes.close()

def test_messaging_visual_applitools(driver, eyes, messaging_interface):
    eyes.open(driver, "Messaging Epic", "Messaging Interface")
    
    messaging_interface('pro_volunteer', 'test_company_001')
    eyes.check("Messaging Interface", Target.window())
    
    eyes.close()
```

### Option 3: Custom Screenshot Testing

#### Implementation:
```python
# In tests/visual/test_visual_regression.py
import pytest
from PIL import Image, ImageChops
import os

class TestVisualRegression:
    
    def test_messaging_interface_screenshot(self, driver, messaging_interface):
        """Custom screenshot comparison test"""
        messaging_interface('pro_volunteer', 'test_company_001')
        
        # Take screenshot
        screenshot_path = "screenshots/messaging_interface_current.png"
        driver.save_screenshot(screenshot_path)
        
        # Compare with baseline (if exists)
        baseline_path = "screenshots/baselines/messaging_interface_baseline.png"
        if os.path.exists(baseline_path):
            self._compare_screenshots(baseline_path, screenshot_path)
    
    def _compare_screenshots(self, baseline_path, current_path):
        """Compare two screenshots"""
        baseline = Image.open(baseline_path)
        current = Image.open(current_path)
        
        diff = ImageChops.difference(baseline, current)
        
        if diff.getbbox():
            diff.save("screenshots/diff.png")
            pytest.fail("Visual regression detected. Check diff.png")
```

## 📋 Visual Test Cases for Messaging Epic

### 1. **Messaging Interface Visual Tests**
```python
def test_messaging_interface_visual_states(driver, percy_driver, messaging_interface):
    """Test all visual states of messaging interface"""
    messaging_interface('pro_volunteer', 'test_company_001')
    
    # Default state
    percy_screenshot(driver, 'Messaging - Default')
    
    # With messages
    # ... send some messages ...
    percy_screenshot(driver, 'Messaging - With Messages')
    
    # Search active
    search_input = driver.find_element(By.CLASS_NAME, "search-input")
    search_input.send_keys("test")
    percy_screenshot(driver, 'Messaging - Search Active')
    
    # Mobile view
    driver.set_window_size(375, 667)  # iPhone size
    percy_screenshot(driver, 'Messaging - Mobile View')
```

### 2. **Profile Button Visual Tests**
```python
def test_profile_button_visual_states(driver, percy_driver, navigate_to_profile):
    """Test message button visual states"""
    navigate_to_profile('company', 'test_company_001')
    
    # Default button state
    percy_screenshot(driver, 'Profile - Message Button Default')
    
    # Hover state
    message_button = driver.find_element(By.CLASS_NAME, "message-button")
    ActionChains(driver).move_to_element(message_button).perform()
    percy_screenshot(driver, 'Profile - Message Button Hover')
    
    # Focus state
    message_button.send_keys(Keys.TAB)
    percy_screenshot(driver, 'Profile - Message Button Focus')
```

### 3. **Admin Settings Visual Tests**
```python
def test_admin_settings_visual(driver, percy_driver, admin_settings_page):
    """Test admin settings visual appearance"""
    percy_screenshot(driver, 'Admin Settings - Default')
    
    # Toggle some settings
    setting_toggle = driver.find_element(By.ID, "setting_4_toggle")
    setting_toggle.click()
    percy_screenshot(driver, 'Admin Settings - Setting Changed')
    
    # Error state
    # ... trigger validation error ...
    percy_screenshot(driver, 'Admin Settings - Error State')
```

## 🚀 Integration with Main Repositories

### Frontend Repository Integration:
```bash
# In skilleduplife/frontend
mkdir -p tests/visual
cp sul-messaging-epic/VISUAL_TESTING_GUIDE.md tests/visual/

# Add visual testing dependencies
npm install --save-dev @percy/selenium-js @percy/cli
# or
pip install percy-selenium applitools-selenium
```

### CI/CD Pipeline Addition:
```yaml
# Add to frontend CI/CD pipeline
visual-tests:
  runs-on: ubuntu-latest
  name: Visual Regression Tests
  needs: [functional-tests]
  
  steps:
  - uses: actions/checkout@v4
  
  - name: Setup Visual Testing
    run: |
      pip install percy-selenium
      npm install -g @percy/cli
  
  - name: Run Visual Tests
    env:
      PERCY_TOKEN: ${{ secrets.PERCY_TOKEN }}
    run: |
      npx percy exec -- python run_tests.py --marker visual
```

## 📊 Visual Testing Best Practices

### 1. **Baseline Management**
- Create baselines for all key UI states
- Update baselines when design changes are intentional
- Review visual diffs carefully before approving

### 2. **Test Organization**
```python
# Organize visual tests by component
tests/visual/
├── test_messaging_interface_visual.py
├── test_profile_buttons_visual.py
├── test_admin_settings_visual.py
└── test_conversation_grouping_visual.py
```

### 3. **Responsive Testing**
```python
SCREEN_SIZES = [
    (1920, 1080),  # Desktop
    (1366, 768),   # Laptop
    (768, 1024),   # Tablet
    (375, 667),    # Mobile
]

@pytest.mark.parametrize("width,height", SCREEN_SIZES)
def test_responsive_design(driver, percy_driver, width, height):
    driver.set_window_size(width, height)
    # ... test visual appearance ...
    percy_screenshot(driver, f'Messaging - {width}x{height}')
```

### 4. **Component State Testing**
```python
def test_button_states_visual(driver, percy_driver):
    """Test all button visual states"""
    button = driver.find_element(By.CLASS_NAME, "message-button")
    
    # Default
    percy_screenshot(driver, 'Button - Default')
    
    # Hover
    ActionChains(driver).move_to_element(button).perform()
    percy_screenshot(driver, 'Button - Hover')
    
    # Active
    ActionChains(driver).click_and_hold(button).perform()
    percy_screenshot(driver, 'Button - Active')
    
    # Disabled
    driver.execute_script("arguments[0].disabled = true;", button)
    percy_screenshot(driver, 'Button - Disabled')
```

## 🎯 Implementation Priority

### Phase 1: Core Components
1. Messaging interface main states
2. Message buttons on profiles
3. Admin settings dashboard

### Phase 2: Interactive States
1. Hover, focus, active states
2. Error and validation states
3. Loading and transition states

### Phase 3: Responsive & Accessibility
1. Mobile/tablet layouts
2. Dark/light theme variations
3. High contrast mode
4. Focus indicators

## 🔧 Tools Comparison

| Tool | Pros | Cons | Best For |
|------|------|------|----------|
| **Percy** | Easy integration, good CI/CD support | Paid service | Teams wanting full-service solution |
| **Applitools** | AI-powered, cross-browser | Expensive | Enterprise applications |
| **Custom Screenshots** | Free, full control | More maintenance | Simple regression testing |
| **Chromatic** | Storybook integration | Requires Storybook setup | Component-driven development |

## 📈 Success Metrics

- **Visual Regression Detection**: Catch unintended design changes
- **Design Consistency**: Ensure brand guidelines compliance
- **Cross-browser Compatibility**: Consistent appearance across browsers
- **Responsive Design Validation**: Proper mobile/desktop layouts
- **Accessibility Compliance**: Visual accessibility standards

---

**Ready to add visual testing?** Start with Percy integration for the messaging interface component! 🎨
