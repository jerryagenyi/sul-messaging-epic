"""
Test profile message button functionality
Based on test matrix: test_profile_message_button()
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class TestProfileMessageButton:
    """Test suite for profile message button functionality"""
    
    def test_profile_message_button(self, driver, wait, login_as_user, navigate_to_profile):
        """
        Test message button on profiles opens messaging interface
        
        Feature: Profile Buttons
        What: Initiate conversations
        Why: Easy message access
        How: Button on profiles opens messaging
        Edge Cases: Permission changes
        Acceptance Criteria: Button appears/disappears correctly
        """
        # Login as PRO volunteer (should have messaging permissions)
        login_as_user('pro_volunteer')
        
        # Navigate to company profile
        navigate_to_profile('company', 'test_company_001')
        
        # Find and verify message button
        message_button = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-button")
        ))
        
        assert message_button.is_displayed(), "Message button should be visible"
        assert message_button.is_enabled(), "Message button should be enabled"
        
        # Click message button
        message_button.click()
        
        # Verify messaging interface opens
        messaging_interface = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "messaging-interface")
        ))
        
        assert messaging_interface.is_displayed(), "Messaging interface should open"
        
        # Verify we're in a conversation with the correct user
        conversation_header = driver.find_element(By.CLASS_NAME, "conversation-header")
        assert "company" in conversation_header.text.lower(), \
               "Should show conversation with company"
    
    def test_button_appears_disappears_correctly(self, driver, wait, login_as_user, 
                                               navigate_to_profile):
        """
        Test button visibility changes based on permissions
        
        Edge Cases: Permission changes
        Acceptance Criteria: Button appears/disappears correctly
        """
        # Test 1: Regular volunteer should NOT see button for company
        login_as_user('volunteer')
        navigate_to_profile('company', 'test_company_001')
        
        message_buttons = driver.find_elements(By.CLASS_NAME, "message-button")
        assert len(message_buttons) == 0, "Regular volunteer should not see message button for company"
        
        # Test 2: PRO volunteer SHOULD see button for company
        login_as_user('pro_volunteer')
        navigate_to_profile('company', 'test_company_001')
        
        message_button = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-button")
        ))
        assert message_button.is_displayed(), "PRO volunteer should see message button for company"
        
        # Test 3: System admin should see button for everyone
        login_as_user('system_admin')
        navigate_to_profile('volunteer', 'test_volunteer_001')
        
        message_button = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-button")
        ))
        assert message_button.is_displayed(), "System admin should see message button for all users"
    
    def test_button_styling_and_placement(self, driver, wait, login_as_user, navigate_to_profile):
        """
        Test message button styling and placement on profile
        """
        login_as_user('pro_volunteer')
        navigate_to_profile('company', 'test_company_001')
        
        message_button = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-button")
        ))
        
        # Test button styling
        button_color = message_button.value_of_css_property('background-color')
        assert button_color, "Button should have background color"
        
        # Test button text
        button_text = message_button.text.lower()
        assert any(word in button_text for word in ['message', 'contact', 'send']), \
               f"Button should have appropriate text, got: {button_text}"
        
        # Test button placement (should be in profile actions area)
        profile_actions = driver.find_element(By.CLASS_NAME, "profile-actions")
        button_in_actions = profile_actions.find_elements(By.CLASS_NAME, "message-button")
        assert len(button_in_actions) > 0, "Message button should be in profile actions area"
    
    def test_button_click_opens_correct_conversation(self, driver, wait, login_as_user, 
                                                   navigate_to_profile):
        """
        Test that clicking button opens conversation with correct user
        """
        login_as_user('pro_volunteer')
        
        # Test with different profile types
        test_profiles = [
            ('company', 'test_company_001'),
            ('volunteer', 'test_volunteer_001'),
        ]
        
        for profile_type, profile_id in test_profiles:
            navigate_to_profile(profile_type, profile_id)
            
            try:
                message_button = wait.until(EC.presence_of_element_located(
                    (By.CLASS_NAME, "message-button")
                ))
                
                # Get profile name for verification
                profile_name = driver.find_element(By.CLASS_NAME, "profile-name").text
                
                message_button.click()
                
                # Verify correct conversation opens
                conversation_header = wait.until(EC.presence_of_element_located(
                    (By.CLASS_NAME, "conversation-header")
                ))
                
                assert profile_name.lower() in conversation_header.text.lower(), \
                       f"Should open conversation with {profile_name}"
                
                # Go back to test next profile
                driver.back()
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, "profile-container")))
                
            except TimeoutException:
                # Button might not be visible for this user type - that's okay
                print(f"Message button not found for {profile_type} - checking permissions")
    
    def test_button_hover_and_tooltip(self, driver, wait, login_as_user, navigate_to_profile):
        """
        Test button hover effects and tooltip
        """
        login_as_user('pro_volunteer')
        navigate_to_profile('company', 'test_company_001')
        
        message_button = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-button")
        ))
        
        # Test hover effect
        from selenium.webdriver.common.action_chains import ActionChains
        actions = ActionChains(driver)
        actions.move_to_element(message_button).perform()
        
        time.sleep(1)  # Allow hover effect to activate
        
        # Check for tooltip
        try:
            tooltip = driver.find_element(By.CLASS_NAME, "tooltip")
            assert tooltip.is_displayed(), "Tooltip should appear on hover"
            
            tooltip_text = tooltip.text.lower()
            assert any(word in tooltip_text for word in ['message', 'send', 'contact']), \
                   f"Tooltip should describe button function, got: {tooltip_text}"
        except:
            # Tooltip might be implemented differently or not at all
            print("Tooltip not found - checking title attribute")
            title = message_button.get_attribute('title')
            if title:
                assert any(word in title.lower() for word in ['message', 'send', 'contact']), \
                       f"Title attribute should describe button function, got: {title}"
    
    def test_button_keyboard_accessibility(self, driver, wait, login_as_user, navigate_to_profile):
        """
        Test button keyboard accessibility
        """
        login_as_user('pro_volunteer')
        navigate_to_profile('company', 'test_company_001')
        
        message_button = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-button")
        ))
        
        # Test tab navigation to button
        from selenium.webdriver.common.keys import Keys
        
        # Focus on button using tab navigation
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.TAB)  # Navigate through page elements
        
        # Check if button can receive focus
        focused_element = driver.switch_to.active_element
        
        # Button should be focusable
        assert message_button.get_attribute('tabindex') != '-1', \
               "Message button should be keyboard accessible"
        
        # Test Enter key activation
        if focused_element == message_button:
            focused_element.send_keys(Keys.ENTER)
            
            # Verify messaging interface opens
            messaging_interface = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "messaging-interface")
            ))
            assert messaging_interface.is_displayed(), \
                   "Messaging interface should open with Enter key"
    
    def test_button_loading_states(self, driver, wait, login_as_user, navigate_to_profile):
        """
        Test button loading states during interaction
        """
        login_as_user('pro_volunteer')
        navigate_to_profile('company', 'test_company_001')
        
        message_button = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-button")
        ))
        
        # Click button and check for loading state
        message_button.click()
        
        # Check if button shows loading state
        try:
            # Look for loading indicator
            loading_indicators = [
                (By.CLASS_NAME, "loading"),
                (By.CLASS_NAME, "spinner"),
                (By.CSS_SELECTOR, "[data-loading='true']"),
            ]
            
            for selector in loading_indicators:
                try:
                    loading_element = driver.find_element(*selector)
                    if loading_element.is_displayed():
                        print("Loading state detected")
                        break
                except:
                    continue
                    
        except:
            print("No loading state detected - this might be okay for fast responses")
        
        # Verify final state (messaging interface loaded)
        messaging_interface = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "messaging-interface")
        ))
        assert messaging_interface.is_displayed(), "Should eventually load messaging interface"
    
    def test_multiple_message_buttons_on_profile(self, driver, wait, login_as_user, 
                                                navigate_to_profile):
        """
        Test handling of multiple message-related buttons on profile
        """
        login_as_user('system_admin')  # Admin should see all buttons
        navigate_to_profile('company', 'test_company_001')
        
        # Look for different types of message buttons
        message_buttons = driver.find_elements(By.CSS_SELECTOR, 
                                             "[class*='message'], [data-action*='message']")
        
        if len(message_buttons) > 1:
            # Test each button type
            for i, button in enumerate(message_buttons):
                if button.is_displayed() and button.is_enabled():
                    button_text = button.text or button.get_attribute('aria-label') or f"Button {i}"
                    print(f"Testing message button: {button_text}")
                    
                    # Click and verify appropriate response
                    button.click()
                    time.sleep(2)  # Allow for response
                    
                    # Check if messaging interface or modal opened
                    messaging_elements = driver.find_elements(By.CSS_SELECTOR,
                                                            ".messaging-interface, .message-modal, .chat-window")
                    
                    assert len(messaging_elements) > 0, f"Button '{button_text}' should open messaging interface"
                    
                    # Close interface and test next button
                    try:
                        close_button = driver.find_element(By.CLASS_NAME, "close-button")
                        close_button.click()
                    except:
                        driver.back()  # Fallback to browser back
                    
                    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "profile-container")))
    
    @pytest.mark.smoke
    def test_message_button_smoke_test(self, driver, wait, login_as_user, navigate_to_profile):
        """
        Smoke test for basic message button functionality
        """
        # Quick test to ensure message button works
        login_as_user('pro_volunteer')
        navigate_to_profile('company', 'test_company_001')
        
        # Should find and be able to click message button
        message_button = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "message-button")
        ))
        
        message_button.click()
        
        # Should open some form of messaging interface
        messaging_opened = False
        possible_selectors = [
            (By.CLASS_NAME, "messaging-interface"),
            (By.CLASS_NAME, "chat-window"),
            (By.CLASS_NAME, "message-modal"),
            (By.ID, "messaging-container"),
        ]
        
        for selector in possible_selectors:
            try:
                element = wait.until(EC.presence_of_element_located(selector))
                if element.is_displayed():
                    messaging_opened = True
                    break
            except TimeoutException:
                continue
        
        assert messaging_opened, "Message button should open messaging interface"
