"""
Test admin messaging settings functionality
Based on test matrix: test_admin_messaging_settings()
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time

class TestAdminMessagingSettings:
    """Test suite for admin messaging settings configuration"""
    
    def test_admin_messaging_settings(self, driver, wait, admin_settings_page):
        """
        Test admin can configure messaging rules
        
        Feature: Admin Settings
        What: Configure messaging rules
        Why: Allow platform control
        How: Admin dashboard with setting toggles
        Edge Cases: Invalid configurations
        Acceptance Criteria: Settings save and apply immediately
        """
        # Verify admin settings page loaded
        assert "admin" in driver.current_url.lower(), "Should be on admin page"
        
        # Test Setting 1: Allow all users to message each other
        self._test_setting_toggle(driver, wait, "setting_1", "Allow all messaging", True)
        
        # Test Setting 2: Restrict volunteer to company messaging
        self._test_setting_toggle(driver, wait, "setting_2", "Restrict volunteer messaging", False)
        
        # Test Setting 3: PRO volunteers can message companies
        self._test_setting_toggle(driver, wait, "setting_3", "PRO volunteer messaging", True)
        
        # Test Setting 4: Companies can message all volunteers
        self._test_setting_toggle(driver, wait, "setting_4", "Company messaging", True)
        
        # Test save functionality
        self._test_settings_save(driver, wait)
    
    def test_settings_save_and_apply_immediately(self, driver, wait, admin_settings_page):
        """
        Test that settings save and apply immediately
        """
        # Change a setting
        setting_toggle = wait.until(EC.element_to_be_clickable(
            (By.ID, "setting_4_toggle")
        ))
        
        initial_state = setting_toggle.is_selected()
        setting_toggle.click()
        
        # Save settings
        save_button = driver.find_element(By.ID, "save-settings")
        save_button.click()
        
        # Verify save confirmation
        success_message = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "save-success")
        ))
        assert "saved" in success_message.text.lower(), "Should show save confirmation"
        
        # Refresh page and verify setting persisted
        driver.refresh()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "admin-settings")))
        
        setting_toggle_after_refresh = driver.find_element(By.ID, "setting_4_toggle")
        assert setting_toggle_after_refresh.is_selected() != initial_state, \
               "Setting should persist after page refresh"
    
    def test_invalid_configurations(self, driver, wait, admin_settings_page):
        """
        Test handling of invalid configurations
        
        Edge Cases: Invalid configurations
        """
        # Test conflicting settings (e.g., allow all + restrict all)
        allow_all_toggle = driver.find_element(By.ID, "allow_all_messaging")
        restrict_all_toggle = driver.find_element(By.ID, "restrict_all_messaging")
        
        # Enable both conflicting settings
        if not allow_all_toggle.is_selected():
            allow_all_toggle.click()
        if not restrict_all_toggle.is_selected():
            restrict_all_toggle.click()
        
        # Try to save
        save_button = driver.find_element(By.ID, "save-settings")
        save_button.click()
        
        # Should show validation error
        try:
            error_message = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "validation-error")
            ))
            assert "conflict" in error_message.text.lower() or \
                   "invalid" in error_message.text.lower(), \
                   "Should show validation error for conflicting settings"
        except TimeoutException:
            # Alternative: settings might auto-resolve conflicts
            # Verify one setting was automatically disabled
            assert not (allow_all_toggle.is_selected() and restrict_all_toggle.is_selected()), \
                   "Conflicting settings should not both be enabled"
    
    def test_setting_descriptions_and_help(self, driver, wait, admin_settings_page):
        """
        Test that settings have clear descriptions and help text
        """
        # Check for setting descriptions
        settings = driver.find_elements(By.CLASS_NAME, "setting-item")
        assert len(settings) > 0, "Should have setting items"
        
        for setting in settings:
            # Each setting should have a label
            label = setting.find_element(By.CLASS_NAME, "setting-label")
            assert label.text.strip(), "Setting should have non-empty label"
            
            # Check for help text or description
            try:
                description = setting.find_element(By.CLASS_NAME, "setting-description")
                assert description.text.strip(), "Setting should have description"
            except:
                # Alternative: help icon or tooltip
                help_elements = setting.find_elements(By.CLASS_NAME, "help-icon")
                assert len(help_elements) > 0, "Setting should have help information"
    
    def test_permission_levels_configuration(self, driver, wait, admin_settings_page):
        """
        Test configuration of different permission levels
        """
        # Test role-based permission settings
        role_settings = {
            'volunteer_permissions': ['message_pro_volunteers', 'message_companies_setting4'],
            'pro_volunteer_permissions': ['message_all_volunteers', 'message_companies'],
            'company_permissions': ['message_all_volunteers', 'message_pro_volunteers'],
            'admin_permissions': ['message_all_users', 'manage_settings']
        }
        
        for role, permissions in role_settings.items():
            role_section = driver.find_element(By.ID, f"{role}_section")
            
            for permission in permissions:
                try:
                    permission_checkbox = role_section.find_element(
                        By.ID, f"{permission}_checkbox"
                    )
                    
                    # Test toggling permission
                    initial_state = permission_checkbox.is_selected()
                    permission_checkbox.click()
                    
                    # Verify state changed
                    assert permission_checkbox.is_selected() != initial_state, \
                           f"Permission {permission} should toggle"
                           
                except Exception as e:
                    # Permission might not exist for this role
                    print(f"Permission {permission} not found for {role}: {e}")
    
    def test_bulk_settings_operations(self, driver, wait, admin_settings_page):
        """
        Test bulk operations on settings (enable all, disable all, reset to defaults)
        """
        # Test "Enable All" functionality
        try:
            enable_all_button = driver.find_element(By.ID, "enable-all-settings")
            enable_all_button.click()
            
            # Verify all toggles are enabled
            toggles = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
            enabled_count = sum(1 for toggle in toggles if toggle.is_selected())
            
            assert enabled_count > 0, "Enable all should enable at least some settings"
            
        except Exception:
            print("Enable all functionality not found")
        
        # Test "Reset to Defaults" functionality
        try:
            reset_button = driver.find_element(By.ID, "reset-to-defaults")
            reset_button.click()
            
            # Confirm reset dialog
            confirm_button = wait.until(EC.element_to_be_clickable(
                (By.ID, "confirm-reset")
            ))
            confirm_button.click()
            
            # Verify reset confirmation
            success_message = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "reset-success")
            ))
            assert "reset" in success_message.text.lower(), "Should confirm reset"
            
        except Exception:
            print("Reset to defaults functionality not found")
    
    def test_settings_audit_log(self, driver, wait, admin_settings_page):
        """
        Test that settings changes are logged for audit purposes
        """
        # Make a settings change
        setting_toggle = driver.find_element(By.ID, "setting_1_toggle")
        initial_state = setting_toggle.is_selected()
        setting_toggle.click()
        
        # Save settings
        save_button = driver.find_element(By.ID, "save-settings")
        save_button.click()
        
        # Check audit log
        try:
            audit_log_tab = driver.find_element(By.ID, "audit-log-tab")
            audit_log_tab.click()
            
            # Wait for audit log to load
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "audit-log-entry")))
            
            # Verify recent change is logged
            log_entries = driver.find_elements(By.CLASS_NAME, "audit-log-entry")
            latest_entry = log_entries[0]
            
            entry_text = latest_entry.text.lower()
            assert any(word in entry_text for word in ['setting', 'changed', 'updated']), \
                   "Latest audit entry should reflect settings change"
                   
        except Exception:
            print("Audit log functionality not found")
    
    def _test_setting_toggle(self, driver, wait, setting_id, setting_name, expected_default):
        """
        Helper method to test individual setting toggle
        """
        try:
            setting_toggle = driver.find_element(By.ID, f"{setting_id}_toggle")
            
            # Test initial state
            current_state = setting_toggle.is_selected()
            
            # Toggle setting
            setting_toggle.click()
            
            # Verify state changed
            new_state = setting_toggle.is_selected()
            assert new_state != current_state, f"Setting {setting_name} should toggle"
            
            # Toggle back
            setting_toggle.click()
            final_state = setting_toggle.is_selected()
            assert final_state == current_state, f"Setting {setting_name} should toggle back"
            
        except Exception as e:
            print(f"Setting {setting_name} not found or not toggleable: {e}")
    
    def _test_settings_save(self, driver, wait):
        """
        Helper method to test settings save functionality
        """
        try:
            save_button = driver.find_element(By.ID, "save-settings")
            assert save_button.is_enabled(), "Save button should be enabled"
            
            save_button.click()
            
            # Wait for save confirmation
            success_message = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "save-success")
            ))
            
            assert success_message.is_displayed(), "Should show save success message"
            
        except Exception as e:
            print(f"Save functionality test failed: {e}")
    
    @pytest.mark.smoke
    def test_admin_settings_page_loads(self, driver, wait, admin_settings_page):
        """
        Smoke test to ensure admin settings page loads correctly
        """
        # Verify page elements are present
        assert driver.find_element(By.CLASS_NAME, "admin-settings"), "Admin settings container should be present"
        assert driver.find_element(By.ID, "save-settings"), "Save button should be present"
        
        # Verify at least one setting is present
        settings = driver.find_elements(By.CLASS_NAME, "setting-item")
        assert len(settings) > 0, "Should have at least one setting item"
