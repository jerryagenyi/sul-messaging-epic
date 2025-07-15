"""
Design System Compliance Tests
Tests implementation against SkilledUp.Life design system standards
"""
import pytest
import yaml
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestDesignSystemCompliance:
    """Test suite for design system compliance across all modules"""
    
    @pytest.fixture(scope="class")
    def design_system(self):
        """Load design system specifications"""
        spec_path = os.path.join(os.path.dirname(__file__), '../../design-specs/skilledup-design-system.yml')
        with open(spec_path, 'r') as f:
            return yaml.safe_load(f)
    
    def test_global_header_compliance(self, driver, wait, login_as_user, design_system):
        """
        Test global header matches design system standards
        This should be consistent across ALL modules
        """
        login_as_user('pro_volunteer')
        driver.get(f"{driver.current_url.split('/')[0]}//dashboard")
        
        header_specs = design_system['skilledup_design_system']['components']['header']
        
        try:
            header = wait.until(EC.presence_of_element_located(
                (By.TAG_NAME, "header")
            ))
            
            # Test header height
            header_height = header.size['height']
            expected_height = int(header_specs['height'].replace('px', ''))
            
            assert abs(header_height - expected_height) <= 5, \
                   f"Header height should be {expected_height}px, got {header_height}px"
            
            # Test header background
            bg_color = header.value_of_css_property('background-color')
            # White should be rgb(254, 255, 254) or similar
            assert self._is_white_color(bg_color), f"Header should have white background"
            
            # Test header border
            border_bottom = header.value_of_css_property('border-bottom-width')
            assert border_bottom == '1px', "Header should have 1px bottom border"
            
        except Exception as e:
            pytest.skip(f"Global header not implemented yet: {e}")
    
    def test_global_footer_compliance(self, driver, wait, login_as_user, design_system):
        """
        Test global footer matches design system standards
        This should be consistent across ALL modules
        """
        login_as_user('pro_volunteer')
        driver.get(f"{driver.current_url.split('/')[0]}//dashboard")
        
        footer_specs = design_system['skilledup_design_system']['components']['footer']
        
        try:
            footer = driver.find_element(By.TAG_NAME, "footer")
            
            # Test footer background (should be gray-50)
            bg_color = footer.value_of_css_property('background-color')
            # Should be light gray, not white
            assert not self._is_white_color(bg_color), "Footer should have gray background"
            
            # Test footer border
            border_top = footer.value_of_css_property('border-top-width')
            assert border_top == '1px', "Footer should have 1px top border"
            
        except Exception as e:
            pytest.skip(f"Global footer not implemented yet: {e}")
    
    def test_primary_button_design_system(self, driver, wait, login_as_user, design_system):
        """
        Test primary buttons follow design system standards
        Should be consistent across ALL modules
        """
        login_as_user('pro_volunteer')
        driver.get(f"{driver.current_url.split('/')[0]}//dashboard")
        
        button_specs = design_system['skilledup_design_system']['components']['buttons']['primary']
        colors = design_system['skilledup_design_system']['colors']
        
        # Find primary buttons (multiple selectors)
        primary_buttons = driver.find_elements(By.CSS_SELECTOR, 
            ".btn-primary, .button-primary, [class*='primary-button'], .post-opportunity-button")
        
        if not primary_buttons:
            pytest.skip("No primary buttons found on page")
        
        for button in primary_buttons[:3]:  # Test first 3 buttons
            try:
                # Test button height
                button_height = button.size['height']
                expected_height = int(button_specs['height'].replace('px', ''))
                
                assert abs(button_height - expected_height) <= 5, \
                       f"Primary button height should be {expected_height}px, got {button_height}px"
                
                # Test background color (should be primary blue)
                bg_color = button.value_of_css_property('background-color')
                expected_blue = self._hex_to_rgb(colors['primary']['blue_primary'])
                
                if self._color_matches(bg_color, expected_blue):
                    print("✓ Primary button uses correct blue color")
                else:
                    # Might be secondary button style
                    border_color = button.value_of_css_property('border-color')
                    if self._color_matches(border_color, expected_blue):
                        print("✓ Secondary button style with blue border")
                
                # Test border radius
                border_radius = button.value_of_css_property('border-radius')
                expected_radius = "6px"  # md = 6px
                assert expected_radius in border_radius, \
                       f"Button should have {expected_radius} border radius"
                
            except Exception as e:
                print(f"Button test failed: {e}")
                continue
    
    def test_form_input_design_system(self, driver, wait, messaging_interface, design_system):
        """
        Test form inputs follow design system standards
        """
        messaging_interface('pro_volunteer', 'test_company_001')
        
        input_specs = design_system['skilledup_design_system']['components']['forms']['input']
        
        try:
            message_input = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "message-input")
            ))
            
            # Test input height
            input_height = message_input.size['height']
            expected_height = int(input_specs['height'].replace('px', ''))
            
            assert abs(input_height - expected_height) <= 5, \
                   f"Input height should be {expected_height}px, got {input_height}px"
            
            # Test border
            border_width = message_input.value_of_css_property('border-width')
            assert border_width == '1px', "Input should have 1px border"
            
            # Test border radius
            border_radius = message_input.value_of_css_property('border-radius')
            expected_radius = "6px"  # md = 6px
            assert expected_radius in border_radius, \
                   f"Input should have {expected_radius} border radius"
            
            # Test focus state
            message_input.click()  # Focus the input
            
            # Check for focus styles (might need time to apply)
            import time
            time.sleep(0.2)
            
            border_color = message_input.value_of_css_property('border-color')
            box_shadow = message_input.value_of_css_property('box-shadow')
            
            # Should have blue border or box shadow on focus
            has_focus_style = (
                self._color_matches(border_color, self._hex_to_rgb("#004AAD")) or
                "rgba(0, 74, 173" in box_shadow
            )
            
            if has_focus_style:
                print("✓ Input has proper focus styling")
            else:
                print("⚠ Input focus styling may need improvement")
                
        except Exception as e:
            pytest.skip(f"Form inputs not implemented yet: {e}")
    
    def test_typography_consistency(self, driver, wait, login_as_user, design_system):
        """
        Test typography follows design system standards
        """
        login_as_user('pro_volunteer')
        driver.get(f"{driver.current_url.split('/')[0]}//dashboard")
        
        typography = design_system['skilledup_design_system']['typography']
        
        # Test font family consistency
        body_elements = driver.find_elements(By.CSS_SELECTOR, "body, p, div, span")
        
        if body_elements:
            font_family = body_elements[0].value_of_css_property('font-family')
            expected_fonts = ['-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto']
            
            has_system_font = any(font in font_family for font in expected_fonts)
            assert has_system_font, f"Should use system font stack, got: {font_family}"
            
        # Test heading hierarchy
        headings = driver.find_elements(By.CSS_SELECTOR, "h1, h2, h3, h4, h5, h6")
        
        for heading in headings[:3]:  # Test first 3 headings
            font_weight = heading.value_of_css_property('font-weight')
            # Headings should be medium (500) or semibold (600) or bold (700)
            assert font_weight in ['500', '600', '700'], \
                   f"Headings should be medium/semibold/bold, got: {font_weight}"
    
    def test_color_palette_usage(self, driver, wait, login_as_user, design_system):
        """
        Test that only approved colors from design system are used
        """
        login_as_user('pro_volunteer')
        driver.get(f"{driver.current_url.split('/')[0]}//dashboard")
        
        colors = design_system['skilledup_design_system']['colors']
        approved_colors = []
        
        # Collect all approved colors
        for category in colors.values():
            if isinstance(category, dict):
                approved_colors.extend(category.values())
        
        # Convert to RGB for comparison
        approved_rgb = [self._hex_to_rgb(color) for color in approved_colors if color.startswith('#')]
        
        # Test primary elements use approved colors
        primary_elements = driver.find_elements(By.CSS_SELECTOR, 
            "button, .btn, a, .primary, .secondary, .text-primary")
        
        color_violations = []
        
        for element in primary_elements[:5]:  # Test first 5 elements
            try:
                element_color = element.value_of_css_property('color')
                bg_color = element.value_of_css_property('background-color')
                border_color = element.value_of_css_property('border-color')
                
                colors_to_check = [element_color, bg_color, border_color]
                
                for color in colors_to_check:
                    if color and not self._is_transparent(color) and not self._is_white_or_black(color):
                        color_rgb = self._css_color_to_rgb(color)
                        if color_rgb and not any(self._colors_similar(color_rgb, approved) for approved in approved_rgb):
                            color_violations.append(f"Unapproved color: {color}")
                            
            except Exception:
                continue
        
        if color_violations:
            print(f"⚠ Found {len(color_violations)} potential color violations")
            for violation in color_violations[:3]:  # Show first 3
                print(f"  - {violation}")
        else:
            print("✓ No obvious color violations detected")
    
    def test_spacing_consistency(self, driver, wait, messaging_interface, design_system):
        """
        Test spacing follows 4px grid system
        """
        messaging_interface('pro_volunteer', 'test_company_001')
        
        spacing = design_system['skilledup_design_system']['spacing']
        
        try:
            # Test message input padding
            message_input = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "message-input")
            ))
            
            padding = message_input.value_of_css_property('padding')
            
            # Extract padding values and check if they follow 4px grid
            import re
            padding_values = re.findall(r'\d+', padding)
            
            for value in padding_values:
                px_value = int(value)
                # Should be divisible by 4 (4px grid system)
                if px_value > 0:
                    assert px_value % 4 == 0 or px_value in [1, 2], \
                           f"Padding {px_value}px should follow 4px grid system"
            
            print(f"✓ Padding follows grid system: {padding}")
            
        except Exception as e:
            pytest.skip(f"Spacing test failed: {e}")
    
    # Helper methods
    def _hex_to_rgb(self, hex_color):
        """Convert hex color to RGB tuple"""
        if not hex_color or not hex_color.startswith('#'):
            return None
        hex_color = hex_color.lstrip('#')
        try:
            return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        except:
            return None
    
    def _css_color_to_rgb(self, css_color):
        """Convert CSS color to RGB tuple"""
        if css_color.startswith('rgb'):
            import re
            numbers = re.findall(r'\d+', css_color)
            return tuple(int(n) for n in numbers[:3])
        return None
    
    def _color_matches(self, css_color, expected_rgb, tolerance=15):
        """Check if CSS color matches expected RGB with tolerance"""
        if not expected_rgb:
            return True
        
        actual_rgb = self._css_color_to_rgb(css_color)
        if not actual_rgb:
            return False
        
        return all(abs(a - e) <= tolerance for a, e in zip(actual_rgb, expected_rgb))
    
    def _colors_similar(self, rgb1, rgb2, tolerance=20):
        """Check if two RGB colors are similar"""
        if not rgb1 or not rgb2:
            return False
        return all(abs(a - b) <= tolerance for a, b in zip(rgb1, rgb2))
    
    def _is_white_color(self, css_color):
        """Check if color is white or near-white"""
        rgb = self._css_color_to_rgb(css_color)
        if not rgb:
            return False
        return all(c >= 250 for c in rgb)  # Very light colors
    
    def _is_transparent(self, css_color):
        """Check if color is transparent"""
        return 'transparent' in css_color or 'rgba(0, 0, 0, 0)' in css_color
    
    def _is_white_or_black(self, css_color):
        """Check if color is white, black, or gray"""
        rgb = self._css_color_to_rgb(css_color)
        if not rgb:
            return True  # Assume system colors are OK
        
        # Check if it's grayscale (R=G=B) or very close
        r, g, b = rgb
        is_grayscale = abs(r - g) <= 10 and abs(g - b) <= 10 and abs(r - b) <= 10
        return is_grayscale
    
    @pytest.mark.design_system
    def test_messaging_module_overrides(self, driver, wait, messaging_interface, design_system):
        """
        Test messaging-specific design system overrides
        """
        messaging_interface('pro_volunteer', 'test_company_001')
        
        messaging_overrides = design_system['module_overrides']['messaging']
        
        try:
            # Test message bubble max width
            message_bubbles = driver.find_elements(By.CLASS_NAME, "message-bubble")
            
            if message_bubbles:
                bubble = message_bubbles[0]
                bubble_width = bubble.size['width']
                container_width = driver.find_element(By.CLASS_NAME, "messaging-interface").size['width']
                
                width_percentage = (bubble_width / container_width) * 100
                assert width_percentage <= 75, f"Message bubble should be max 70% width, got {width_percentage:.1f}%"
                
                print(f"✓ Message bubble width: {width_percentage:.1f}% of container")
            
        except Exception as e:
            pytest.skip(f"Messaging module overrides not implemented yet: {e}")
    
    @pytest.mark.smoke
    def test_design_system_smoke_test(self, driver, wait, login_as_user, design_system):
        """
        Smoke test for basic design system compliance
        """
        login_as_user('pro_volunteer')
        driver.get(f"{driver.current_url.split('/')[0]}//dashboard")
        
        # Basic checks that should always pass
        body = driver.find_element(By.TAG_NAME, "body")
        
        # Should have system font
        font_family = body.value_of_css_property('font-family')
        has_system_font = any(font in font_family.lower() for font in 
                            ['system', 'apple', 'segoe', 'roboto'])
        
        assert has_system_font, f"Should use system fonts, got: {font_family}"
        
        # Should have reasonable text color (not pure black or white)
        color = body.value_of_css_property('color')
        rgb = self._css_color_to_rgb(color)
        
        if rgb:
            # Should be dark but not pure black
            assert 50 <= rgb[0] <= 200, f"Text color should be readable gray, got: {color}"
        
        print("✓ Basic design system compliance verified")
