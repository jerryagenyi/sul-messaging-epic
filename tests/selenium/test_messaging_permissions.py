"""
Test messaging permissions enforcement
Based on test matrix: test_messaging_permissions_enforced()
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class TestMessagingPermissions:
    """Test suite for messaging permissions enforcement"""
    
    @pytest.mark.parametrize("user_type,target_type,setting,should_see_button", [
        ("pro_volunteer", "company", "Setting 4", True),
        ("volunteer", "company", "Setting 4", False), 
        ("system_admin", "company", "any", True),
        ("volunteer_app", "company", "Setting 4", True),
        ("volunteer", "pro_volunteer", "default", True),
        ("company", "volunteer", "default", True),
    ])
    def test_messaging_permissions_enforced(self, driver, wait, login_as_user, 
                                          navigate_to_profile, user_type, 
                                          target_type, setting, should_see_button):
        """
        Test that messaging permissions are properly enforced
        
        Scenario: User messaging permissions based on role and settings
        Given I am a <user_type>
        And there is a <target_type> with <setting>
        When I visit their profile
        Then I should <visibility> a "Message" button
        """
        # Login as the specified user type
        user = login_as_user(user_type)
        
        # Navigate to target profile (using mock profile ID)
        target_profile_id = f"test_{target_type}_001"
        navigate_to_profile(target_type, target_profile_id)
        
        # Check for message button visibility
        message_button_found = self._check_message_button_visibility(driver, wait)
        
        if should_see_button:
            assert message_button_found, f"{user_type} should see message button for {target_type} with {setting}"
            
            # Verify button is clickable
            message_button = driver.find_element(By.CLASS_NAME, "message-button")
            assert message_button.is_enabled(), "Message button should be enabled"
            
        else:
            assert not message_button_found, f"{user_type} should NOT see message button for {target_type} with {setting}"
    
    def test_permission_validation_on_message_send(self, driver, wait, login_as_user, 
                                                 messaging_interface):
        """
        Test permission validation when attempting to send message
        
        Scenario: Permission validation on message send
        Given I am a regular Volunteer
        And I somehow access the messaging interface for a Company
        When I attempt to send a message
        Then the system should reject the message
        And I should see an error about insufficient permissions
        """
        # Login as regular volunteer
        login_as_user('volunteer')
        
        # Try to access messaging interface for a company (direct URL manipulation)
        company_id = "test_company_001"
        messaging_interface('volunteer', company_id)
        
        # Attempt to send a message
        try:
            message_input = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "message-input")
            ))
            send_button = driver.find_element(By.CLASS_NAME, "send-button")
            
            message_input.send_keys("This message should be rejected")
            send_button.click()
            
            # Check for error message
            error_message = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "permission-error")
            ))
            
            assert "insufficient permissions" in error_message.text.lower() or \
                   "not authorized" in error_message.text.lower(), \
                   "Should show permission error message"
                   
        except TimeoutException:
            # If messaging interface is not accessible at all, that's also valid
            # Check if we're redirected or shown an access denied page
            page_source = driver.page_source.lower()
            assert any(phrase in page_source for phrase in [
                "access denied", "not authorized", "insufficient permissions"
            ]), "Should show access restriction"
    
    def test_role_change_mid_session(self, driver, wait, login_as_user, 
                                   navigate_to_profile, admin_settings_page):
        """
        Test edge case: Role changes during active session
        
        Given I am logged in as a Volunteer
        And I can see a message button for a PRO Volunteer
        When my role is changed by an admin (simulate)
        And I refresh the page
        Then the message button visibility should update accordingly
        """
        # Login as volunteer
        login_as_user('volunteer')
        
        # Navigate to PRO volunteer profile
        navigate_to_profile('pro_volunteer', 'test_pro_001')
        
        # Check initial button visibility
        initial_button_visible = self._check_message_button_visibility(driver, wait)
        
        # Simulate role change (in real app, this would be done by admin)
        # For testing, we'll simulate by changing user session/cookies
        self._simulate_role_change(driver, 'pro_volunteer')
        
        # Refresh page
        driver.refresh()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "profile-container")))
        
        # Check updated button visibility
        updated_button_visible = self._check_message_button_visibility(driver, wait)
        
        # Verify the change (PRO volunteer should have more permissions)
        if not initial_button_visible:
            assert updated_button_visible, "Button should appear after role upgrade"
    
    def test_messaging_button_states(self, driver, wait, login_as_user, navigate_to_profile):
        """
        Test different states of messaging button (enabled/disabled/hidden)
        """
        # Test as PRO volunteer (should see enabled button)
        login_as_user('pro_volunteer')
        navigate_to_profile('company', 'test_company_001')
        
        message_button = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-button")
        ))
        
        assert message_button.is_displayed(), "Message button should be visible"
        assert message_button.is_enabled(), "Message button should be enabled"
        
        # Check button text/label
        button_text = message_button.text.lower()
        assert any(word in button_text for word in ['message', 'contact', 'send']), \
               f"Button should have appropriate text, got: {button_text}"
    
    def test_permission_error_handling(self, driver, wait, login_as_user):
        """
        Test proper error handling for permission violations
        """
        # Login as volunteer
        login_as_user('volunteer')
        
        # Try to access admin messaging settings (should fail)
        driver.get(f"{driver.current_url.split('/')[0]}//admin/messaging-settings")
        
        # Should be redirected or show error
        time.sleep(2)  # Allow for redirect
        
        page_source = driver.page_source.lower()
        current_url = driver.current_url.lower()
        
        # Check if access is properly denied
        assert any([
            'access denied' in page_source,
            'unauthorized' in page_source,
            'login' in current_url,
            '403' in page_source,
            'forbidden' in page_source
        ]), "Should properly handle unauthorized access"
    
    def _check_message_button_visibility(self, driver, wait, timeout=5):
        """
        Helper method to check if message button is visible
        Returns True if button is found and visible, False otherwise
        """
        try:
            # Try multiple possible selectors for message button
            selectors = [
                (By.CLASS_NAME, "message-button"),
                (By.ID, "message-btn"),
                (By.XPATH, "//button[contains(text(), 'Message')]"),
                (By.XPATH, "//a[contains(text(), 'Message')]"),
                (By.CSS_SELECTOR, "[data-action='message']"),
            ]
            
            for selector in selectors:
                try:
                    element = WebDriverWait(driver, 2).until(
                        EC.presence_of_element_located(selector)
                    )
                    if element.is_displayed():
                        return True
                except TimeoutException:
                    continue
                    
            return False
            
        except Exception:
            return False
    
    def _simulate_role_change(self, driver, new_role):
        """
        Helper method to simulate role change
        In a real application, this would involve admin actions
        """
        # This is a mock implementation
        # In real testing, you might:
        # 1. Use admin API to change user role
        # 2. Modify session cookies/tokens
        # 3. Use database direct manipulation in test environment
        
        # For now, we'll simulate by executing JavaScript to modify session
        driver.execute_script(f"""
            if (window.sessionStorage) {{
                window.sessionStorage.setItem('userRole', '{new_role}');
            }}
            if (window.localStorage) {{
                window.localStorage.setItem('userRole', '{new_role}');
            }}
        """)
    
    @pytest.mark.smoke
    def test_basic_permission_smoke_test(self, driver, wait, login_as_user, navigate_to_profile):
        """
        Smoke test for basic permission functionality
        """
        # Quick test to ensure basic permission system is working
        login_as_user('system_admin')
        navigate_to_profile('company', 'test_company_001')
        
        # Admin should always see message button
        message_button_found = self._check_message_button_visibility(driver, wait)
        assert message_button_found, "System admin should always see message button"
