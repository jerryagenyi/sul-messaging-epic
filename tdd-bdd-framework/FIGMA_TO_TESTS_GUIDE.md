# Figma to Visual Tests Guide

This guide shows how to convert your Figma designs into testable visual specifications for the messaging epic.

## 🎨 Your Figma Designs

Based on your repository, you have these Figma designs:
- `Company Dashboard - Message.svg`
- `Company Dashboard - Message-1.svg` 
- `Company Dashboard - Message-2.svg`
- `Volunteer Dashboard - Message.svg`
- `Volunteer Dashboard - Message-1.svg`

## 🔄 Figma to Test Workflow

```
Figma Design → Design Specifications → Visual Tests → Implementation
     ↓                    ↓                  ↓              ↓
   SVG Files      CSS Properties      Automated Tests    Live Code
```

## 📋 Method 1: Design Specifications from Figma

### Step 1: Extract Design Tokens from Figma

Create design specifications that can be tested:

```yaml
# design-specs/messaging-interface.yml
messaging_interface:
  colors:
    primary_button: "#0969da"
    secondary_button: "#f6f8fa"
    text_primary: "#24292f"
    text_secondary: "#656d76"
    background: "#ffffff"
    border: "#d1d9e0"
  
  typography:
    message_text:
      font_family: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto"
      font_size: "14px"
      line_height: "1.5"
    
    button_text:
      font_family: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto"
      font_size: "14px"
      font_weight: "500"
  
  spacing:
    message_padding: "12px 16px"
    button_padding: "8px 16px"
    container_margin: "16px"
    input_height: "40px"
  
  layout:
    max_width: "800px"
    sidebar_width: "300px"
    message_bubble_max_width: "70%"
  
  components:
    message_button:
      width: "auto"
      height: "36px"
      border_radius: "6px"
      border: "1px solid #d1d9e0"
    
    message_input:
      width: "100%"
      height: "40px"
      border_radius: "6px"
      border: "1px solid #d1d9e0"
      padding: "8px 12px"
```

### Step 2: Create Visual Specification Tests

```python
# tests/visual/test_design_specifications.py
import pytest
import yaml
from selenium.webdriver.common.by import By

class TestDesignSpecifications:
    
    @pytest.fixture(scope="class")
    def design_specs(self):
        """Load design specifications from YAML"""
        with open('design-specs/messaging-interface.yml', 'r') as f:
            return yaml.safe_load(f)
    
    def test_message_button_specifications(self, driver, navigate_to_profile, design_specs):
        """Test message button matches Figma specifications"""
        navigate_to_profile('company', 'test_company_001')
        
        message_button = driver.find_element(By.CLASS_NAME, "message-button")
        specs = design_specs['messaging_interface']['components']['message_button']
        
        # Test dimensions
        button_height = message_button.size['height']
        expected_height = int(specs['height'].replace('px', ''))
        assert abs(button_height - expected_height) <= 2, f"Button height should be ~{expected_height}px, got {button_height}px"
        
        # Test styling
        border_radius = message_button.value_of_css_property('border-radius')
        assert border_radius == specs['border_radius'], f"Border radius should be {specs['border_radius']}"
        
        border = message_button.value_of_css_property('border')
        assert specs['border'] in border, f"Border should match {specs['border']}"
    
    def test_color_specifications(self, driver, messaging_interface, design_specs):
        """Test colors match Figma design"""
        messaging_interface('pro_volunteer', 'test_company_001')
        
        colors = design_specs['messaging_interface']['colors']
        
        # Test primary button color
        send_button = driver.find_element(By.CLASS_NAME, "send-button")
        bg_color = send_button.value_of_css_property('background-color')
        
        # Convert hex to rgb for comparison
        expected_rgb = self._hex_to_rgb(colors['primary_button'])
        assert self._normalize_color(bg_color) == expected_rgb, \
               f"Send button should be {colors['primary_button']}"
    
    def test_typography_specifications(self, driver, messaging_interface, design_specs):
        """Test typography matches Figma design"""
        messaging_interface('pro_volunteer', 'test_company_001')
        
        typography = design_specs['messaging_interface']['typography']
        
        # Test message text typography
        message_input = driver.find_element(By.CLASS_NAME, "message-input")
        
        font_size = message_input.value_of_css_property('font-size')
        expected_size = typography['message_text']['font_size']
        assert font_size == expected_size, f"Font size should be {expected_size}"
        
        font_family = message_input.value_of_css_property('font-family')
        expected_family = typography['message_text']['font_family']
        assert expected_family.split(',')[0].strip('"') in font_family, \
               f"Font family should include {expected_family}"
    
    def test_spacing_specifications(self, driver, messaging_interface, design_specs):
        """Test spacing matches Figma design"""
        messaging_interface('pro_volunteer', 'test_company_001')
        
        spacing = design_specs['messaging_interface']['spacing']
        
        # Test message input padding
        message_input = driver.find_element(By.CLASS_NAME, "message-input")
        padding = message_input.value_of_css_property('padding')
        
        # Parse expected padding
        expected_padding = spacing['input_height']  # This would need proper parsing
        
        # Test container margins
        container = driver.find_element(By.CLASS_NAME, "messaging-interface")
        margin = container.value_of_css_property('margin')
        
        # Add assertions based on your specific spacing requirements
    
    def _hex_to_rgb(self, hex_color):
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def _normalize_color(self, css_color):
        """Normalize CSS color to RGB tuple"""
        if css_color.startswith('rgb'):
            # Extract numbers from rgb(r, g, b)
            import re
            numbers = re.findall(r'\d+', css_color)
            return tuple(int(n) for n in numbers[:3])
        return css_color
```

## 📋 Method 2: Figma API Integration (Advanced)

### Step 1: Extract Design Tokens via Figma API

```python
# scripts/extract_figma_specs.py
import requests
import json

class FigmaSpecExtractor:
    def __init__(self, figma_token, file_key):
        self.token = figma_token
        self.file_key = file_key
        self.base_url = "https://api.figma.com/v1"
    
    def extract_design_tokens(self):
        """Extract design tokens from Figma file"""
        headers = {'X-Figma-Token': self.token}
        
        # Get file data
        response = requests.get(
            f"{self.base_url}/files/{self.file_key}",
            headers=headers
        )
        
        figma_data = response.json()
        
        # Extract styles
        styles = self._extract_styles(figma_data)
        
        # Save as test specifications
        with open('design-specs/figma-extracted.yml', 'w') as f:
            yaml.dump(styles, f)
        
        return styles
    
    def _extract_styles(self, figma_data):
        """Extract styles from Figma data"""
        styles = {
            'colors': {},
            'typography': {},
            'spacing': {},
            'components': {}
        }
        
        # Process Figma nodes to extract design tokens
        # This would need to be customized based on your Figma structure
        
        return styles

# Usage
extractor = FigmaSpecExtractor(
    figma_token="your-figma-token",
    file_key="your-figma-file-key"
)
specs = extractor.extract_design_tokens()
```

## 📋 Method 3: SVG-Based Visual Testing

Since you have SVG exports, we can use them as visual baselines:

```python
# tests/visual/test_svg_comparison.py
import pytest
from selenium.webdriver.common.by import By
import cv2
import numpy as np

class TestSVGComparison:
    
    def test_company_dashboard_matches_figma(self, driver, login_as_user, navigate_to_profile):
        """Test company dashboard matches Figma SVG"""
        login_as_user('company')
        navigate_to_profile('volunteer', 'test_volunteer_001')
        
        # Take screenshot of implemented design
        screenshot_path = "screenshots/company_dashboard_current.png"
        driver.save_screenshot(screenshot_path)
        
        # Compare with Figma SVG (converted to PNG)
        figma_baseline = "messaging-epic-figma-svg/Company Dashboard - Message.png"
        
        similarity = self._compare_images(screenshot_path, figma_baseline)
        
        # Allow some tolerance for minor differences
        assert similarity > 0.85, f"Design should be at least 85% similar to Figma, got {similarity:.2%}"
    
    def test_volunteer_dashboard_matches_figma(self, driver, login_as_user):
        """Test volunteer dashboard matches Figma SVG"""
        login_as_user('volunteer')
        driver.get(f"{driver.current_url.split('/')[0]}//dashboard")
        
        screenshot_path = "screenshots/volunteer_dashboard_current.png"
        driver.save_screenshot(screenshot_path)
        
        figma_baseline = "messaging-epic-figma-svg/Volunteer Dashboard - Message.png"
        
        similarity = self._compare_images(screenshot_path, figma_baseline)
        assert similarity > 0.85, f"Design should match Figma design"
    
    def _compare_images(self, img1_path, img2_path):
        """Compare two images and return similarity score"""
        try:
            img1 = cv2.imread(img1_path)
            img2 = cv2.imread(img2_path)
            
            # Resize images to same size if needed
            if img1.shape != img2.shape:
                img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
            
            # Calculate structural similarity
            from skimage.metrics import structural_similarity as ssim
            similarity = ssim(img1, img2, multichannel=True)
            
            return similarity
            
        except Exception as e:
            print(f"Image comparison failed: {e}")
            return 0.0
```

## 🛠️ Implementation Steps

### Step 1: Create Design Specifications
1. **Manual Method**: Inspect your Figma designs and create YAML specs
2. **API Method**: Use Figma API to extract design tokens
3. **SVG Method**: Use your existing SVG files as baselines

### Step 2: Add to Test Suite
```bash
# Add visual specification tests
mkdir -p tests/visual/specifications
mkdir -p design-specs

# Add dependencies
echo "PyYAML==6.0.1" >> requirements.txt
echo "opencv-python==4.8.1.78" >> requirements.txt
echo "scikit-image==0.21.0" >> requirements.txt
```

### Step 3: Integration with CI/CD
```yaml
# Add to .github/workflows/ci.yml
- name: Run Visual Specification Tests
  run: |
    python run_tests.py --marker visual-specs
```

## 🎯 Recommended Approach for Your Team

1. **Start with Method 1**: Create manual design specifications from your Figma designs
2. **Use your SVG files**: Convert them to PNG baselines for comparison
3. **Focus on key components**: Message buttons, input fields, layouts
4. **Iterate gradually**: Add more specifications as you implement features

This way, your visual tests will validate that the implementation matches your Figma designs! 🎨
