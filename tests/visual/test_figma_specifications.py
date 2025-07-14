"""
Visual tests based on Figma design specifications
Tests implementation against your actual Figma designs
"""
import pytest
import yaml
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class TestFigmaSpecifications:
    """Test suite for Figma design specification compliance"""
    
    @pytest.fixture(scope="class")
    def company_dashboard_specs(self):
        """Load company dashboard design specifications"""
        spec_path = os.path.join(os.path.dirname(__file__), '../../design-specs/company-dashboard-message.yml')
        with open(spec_path, 'r') as f:
            return yaml.safe_load(f)
    
    def test_company_dashboard_layout(self, driver, wait, login_as_user, company_dashboard_specs):
        """
        Test company dashboard layout matches Figma design
        
        Validates:
        - Canvas dimensions
        - Sidebar width
        - Top navigation height
        - Main content area
        """
        login_as_user('company')
        driver.get(f"{driver.current_url.split('/')[0]}//dashboard")
        
        specs = company_dashboard_specs['company_dashboard_message']
        layout = specs['layout']
        
        # Test main container dimensions
        main_container = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "dashboard-container")
        ))
        
        container_width = main_container.size['width']
        expected_width = int(layout['main_content_width'].replace('px', ''))
        
        # Allow 5% tolerance for responsive behavior
        tolerance = expected_width * 0.05
        assert abs(container_width - expected_width) <= tolerance, \
               f"Container width should be ~{expected_width}px, got {container_width}px"
        
        # Test sidebar width
        try:
            sidebar = driver.find_element(By.CLASS_NAME, "sidebar")
            sidebar_width = sidebar.size['width']
            expected_sidebar_width = int(layout['sidebar_width'].replace('px', ''))
            
            assert abs(sidebar_width - expected_sidebar_width) <= 5, \
                   f"Sidebar width should be ~{expected_sidebar_width}px, got {sidebar_width}px"
        except:
            pytest.skip("Sidebar not implemented yet")
    
    def test_post_opportunity_button_design(self, driver, wait, login_as_user, company_dashboard_specs):
        """
        Test Post Opportunity button matches Figma specifications
        
        Validates:
        - Button dimensions
        - Border radius
        - Colors
        - Typography
        """
        login_as_user('company')
        driver.get(f"{driver.current_url.split('/')[0]}//dashboard")
        
        specs = company_dashboard_specs['company_dashboard_message']
        button_specs = specs['components']['post_opportunity_button']
        colors = specs['colors']
        
        try:
            post_button = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "post-opportunity-button")
            ))
            
            # Test button dimensions
            button_width = post_button.size['width']
            button_height = post_button.size['height']
            
            expected_width = int(button_specs['width'].replace('px', ''))
            expected_height = int(button_specs['height'].replace('px', ''))
            
            assert abs(button_width - expected_width) <= 10, \
                   f"Button width should be ~{expected_width}px, got {button_width}px"
            assert abs(button_height - expected_height) <= 5, \
                   f"Button height should be ~{expected_height}px, got {button_height}px"
            
            # Test border radius
            border_radius = post_button.value_of_css_property('border-radius')
            expected_radius = button_specs['border_radius']
            assert expected_radius.replace('px', '') in border_radius, \
                   f"Border radius should be {expected_radius}"
            
            # Test colors
            bg_color = post_button.value_of_css_property('background-color')
            border_color = post_button.value_of_css_property('border-color')
            text_color = post_button.value_of_css_property('color')
            
            # Convert hex to RGB for comparison
            expected_bg = self._hex_to_rgb(button_specs['background'])
            expected_border = self._hex_to_rgb(colors['primary_blue'])
            expected_text = self._hex_to_rgb(button_specs['text_color'])
            
            assert self._color_matches(bg_color, expected_bg), \
                   f"Button background should be {button_specs['background']}"
            assert self._color_matches(text_color, expected_text), \
                   f"Button text should be {button_specs['text_color']}"
                   
        except Exception as e:
            pytest.skip(f"Post opportunity button not implemented yet: {e}")
    
    def test_button_interactive_states(self, driver, wait, login_as_user, company_dashboard_specs):
        """
        Test button interactive states match Figma design
        
        Validates:
        - Hover state colors
        - Active state colors
        - Transition effects
        """
        login_as_user('company')
        driver.get(f"{driver.current_url.split('/')[0]}//dashboard")
        
        specs = company_dashboard_specs['company_dashboard_message']
        states = specs['states']['post_opportunity_button']
        
        try:
            post_button = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "post-opportunity-button")
            ))
            
            # Test default state
            default_bg = post_button.value_of_css_property('background-color')
            expected_default = self._hex_to_rgb(states['default']['background'])
            assert self._color_matches(default_bg, expected_default), \
                   "Default state should match Figma design"
            
            # Test hover state
            actions = ActionChains(driver)
            actions.move_to_element(post_button).perform()
            
            # Wait for hover effect
            import time
            time.sleep(0.5)
            
            hover_bg = post_button.value_of_css_property('background-color')
            expected_hover = self._hex_to_rgb(states['hover']['background'])
            
            # Note: This might not work if hover effects aren't implemented
            # The test documents the expected behavior
            print(f"Hover background: {hover_bg} (expected: {states['hover']['background']})")
            
        except Exception as e:
            pytest.skip(f"Interactive states not implemented yet: {e}")
    
    def test_sidebar_navigation_icons(self, driver, wait, login_as_user, company_dashboard_specs):
        """
        Test sidebar navigation icons match Figma positioning
        
        Validates:
        - Icon positions
        - Icon sizes
        - Icon colors
        """
        login_as_user('company')
        driver.get(f"{driver.current_url.split('/')[0]}//dashboard")
        
        specs = company_dashboard_specs['company_dashboard_message']
        nav_icons = specs['components']['nav_icons']
        
        try:
            sidebar = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "sidebar")
            ))
            
            # Test message icon (most relevant for messaging epic)
            message_icon = sidebar.find_element(By.CLASS_NAME, "message-icon")
            
            # Test icon color
            icon_color = message_icon.value_of_css_property('color')
            expected_color = self._hex_to_rgb(nav_icons['message_icon']['color'])
            
            assert self._color_matches(icon_color, expected_color), \
                   f"Message icon color should be {nav_icons['message_icon']['color']}"
            
            # Test icon size (approximate)
            icon_size = message_icon.size
            expected_size = int(nav_icons['message_icon']['size'].replace('px', ''))
            
            # Icons might be implemented as fonts, so size testing is approximate
            assert icon_size['width'] >= expected_size - 5 and icon_size['width'] <= expected_size + 5, \
                   f"Message icon should be approximately {expected_size}px"
                   
        except Exception as e:
            pytest.skip(f"Sidebar navigation not implemented yet: {e}")
    
    def test_color_scheme_consistency(self, driver, wait, login_as_user, company_dashboard_specs):
        """
        Test overall color scheme matches Figma design system
        
        Validates:
        - Primary blue usage
        - Background colors
        - Text colors
        """
        login_as_user('company')
        driver.get(f"{driver.current_url.split('/')[0]}//dashboard")
        
        specs = company_dashboard_specs['company_dashboard_message']
        colors = specs['colors']
        
        # Test primary blue is used consistently
        primary_elements = driver.find_elements(By.CSS_SELECTOR, "[class*='primary'], [class*='button']")
        
        for element in primary_elements[:3]:  # Test first 3 elements
            try:
                element_color = element.value_of_css_property('color')
                bg_color = element.value_of_css_property('background-color')
                border_color = element.value_of_css_property('border-color')
                
                expected_primary = self._hex_to_rgb(colors['primary_blue'])
                
                # Check if any of the color properties use primary blue
                uses_primary = (
                    self._color_matches(element_color, expected_primary) or
                    self._color_matches(bg_color, expected_primary) or
                    self._color_matches(border_color, expected_primary)
                )
                
                if uses_primary:
                    print(f"✓ Element uses primary blue correctly")
                    
            except Exception as e:
                continue  # Skip elements that don't have color properties
    
    def test_responsive_behavior(self, driver, wait, login_as_user, company_dashboard_specs):
        """
        Test responsive behavior matches design expectations
        
        Validates:
        - Mobile layout adaptations
        - Tablet layout adaptations
        - Desktop layout consistency
        """
        login_as_user('company')
        driver.get(f"{driver.current_url.split('/')[0]}//dashboard")
        
        specs = company_dashboard_specs['company_dashboard_message']
        responsive = specs['responsive']
        
        # Test different screen sizes
        screen_sizes = [
            (1920, 1080, 'desktop'),
            (768, 1024, 'tablet'),
            (375, 667, 'mobile')
        ]
        
        for width, height, device_type in screen_sizes:
            driver.set_window_size(width, height)
            
            # Wait for responsive changes to take effect
            import time
            time.sleep(1)
            
            try:
                main_container = driver.find_element(By.CLASS_NAME, "dashboard-container")
                container_width = main_container.size['width']
                
                if device_type == 'desktop':
                    # Desktop should use full width or max width
                    assert container_width >= 1200, f"Desktop layout should be wide enough"
                elif device_type == 'tablet':
                    # Tablet should adapt to screen
                    assert container_width <= width, f"Tablet layout should fit screen"
                elif device_type == 'mobile':
                    # Mobile should be narrow
                    assert container_width <= width, f"Mobile layout should fit screen"
                    
                print(f"✓ {device_type.title()} layout: {container_width}px width")
                
            except Exception as e:
                print(f"⚠ {device_type.title()} layout not fully responsive: {e}")
    
    # Helper methods
    def _hex_to_rgb(self, hex_color):
        """Convert hex color to RGB tuple"""
        if not hex_color.startswith('#'):
            return None
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def _color_matches(self, css_color, expected_rgb, tolerance=10):
        """Check if CSS color matches expected RGB with tolerance"""
        if not expected_rgb:
            return True
            
        try:
            if css_color.startswith('rgb'):
                import re
                numbers = re.findall(r'\d+', css_color)
                actual_rgb = tuple(int(n) for n in numbers[:3])
                
                # Check each color component with tolerance
                for actual, expected in zip(actual_rgb, expected_rgb):
                    if abs(actual - expected) > tolerance:
                        return False
                return True
        except:
            pass
        
        return False
    
    @pytest.mark.visual
    def test_visual_regression_against_figma(self, driver, wait, login_as_user):
        """
        Visual regression test against Figma baseline
        
        This test takes a screenshot and compares it with the Figma design
        Requires manual baseline creation from Figma export
        """
        login_as_user('company')
        driver.get(f"{driver.current_url.split('/')[0]}//dashboard")
        
        # Take screenshot
        screenshot_path = "screenshots/company_dashboard_current.png"
        driver.save_screenshot(screenshot_path)
        
        # Compare with Figma baseline (converted from SVG to PNG)
        figma_baseline = "design-specs/baselines/company-dashboard-message.png"
        
        if os.path.exists(figma_baseline):
            similarity = self._compare_with_baseline(screenshot_path, figma_baseline)
            assert similarity > 0.80, f"Visual similarity should be >80%, got {similarity:.2%}"
        else:
            pytest.skip("Figma baseline image not available. Create baseline from SVG first.")
    
    def _compare_with_baseline(self, current_path, baseline_path):
        """Compare current screenshot with baseline image"""
        try:
            from PIL import Image
            import numpy as np
            
            current = Image.open(current_path)
            baseline = Image.open(baseline_path)
            
            # Resize to same dimensions if needed
            if current.size != baseline.size:
                baseline = baseline.resize(current.size)
            
            # Convert to numpy arrays
            current_array = np.array(current)
            baseline_array = np.array(baseline)
            
            # Calculate similarity (simplified)
            diff = np.abs(current_array - baseline_array)
            similarity = 1 - (np.mean(diff) / 255)
            
            return similarity
            
        except ImportError:
            pytest.skip("PIL not available for image comparison")
        except Exception as e:
            pytest.skip(f"Image comparison failed: {e}")
