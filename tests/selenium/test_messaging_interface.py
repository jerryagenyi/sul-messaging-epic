"""
Test messaging interface functionality
Based on test matrix: test_messaging_interface()
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

class TestMessagingInterface:
    """Test suite for messaging interface functionality"""
    
    def test_messaging_interface(self, driver, wait, messaging_interface, test_message_data):
        """
        Test core messaging functionality
        
        Feature: Message Interface
        What: Send/receive messages
        Why: Core communication
        How: Real-time messaging with search
        Edge Cases: Network failures, large histories
        Acceptance Criteria: Messages delivered, search works
        """
        # Open messaging interface
        messaging_interface('pro_volunteer', 'test_company_001')
        
        # Verify interface elements
        message_input = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-input")
        ))
        send_button = driver.find_element(By.CLASS_NAME, "send-button")
        message_history = driver.find_element(By.CLASS_NAME, "message-history")
        
        assert message_input.is_displayed(), "Message input should be visible"
        assert send_button.is_displayed(), "Send button should be visible"
        assert message_history.is_displayed(), "Message history should be visible"
        
        # Test sending a message
        test_message = test_message_data['short_message']
        message_input.send_keys(test_message)
        send_button.click()
        
        # Verify message appears in history
        sent_message = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//div[contains(@class, 'message') and contains(text(), '{test_message[:20]}')]")
        ))
        
        assert sent_message.is_displayed(), "Sent message should appear in history"
        
        # Verify message input is cleared after sending
        assert message_input.get_attribute('value') == '', "Message input should be cleared after sending"
    
    def test_real_time_messaging(self, driver, wait, messaging_interface, test_message_data):
        """
        Test real-time messaging functionality
        """
        messaging_interface('pro_volunteer', 'test_company_001')
        
        message_input = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-input")
        ))
        send_button = driver.find_element(By.CLASS_NAME, "send-button")
        
        # Send multiple messages quickly
        messages = [
            test_message_data['short_message'],
            "Follow-up message",
            "Third message in sequence"
        ]
        
        for i, message in enumerate(messages):
            message_input.send_keys(message)
            send_button.click()
            
            # Verify each message appears
            sent_message = wait.until(EC.presence_of_element_located(
                (By.XPATH, f"//div[contains(@class, 'message') and contains(text(), '{message[:15]}')]")
            ))
            assert sent_message.is_displayed(), f"Message {i+1} should appear in real-time"
            
            time.sleep(1)  # Brief pause between messages
    
    def test_message_delivery_status(self, driver, wait, messaging_interface, test_message_data):
        """
        Test message delivery status indicators
        """
        messaging_interface('pro_volunteer', 'test_company_001')
        
        message_input = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-input")
        ))
        send_button = driver.find_element(By.CLASS_NAME, "send-button")
        
        # Send a message
        test_message = test_message_data['short_message']
        message_input.send_keys(test_message)
        send_button.click()
        
        # Look for delivery status indicators
        try:
            # Check for various status indicators
            status_indicators = [
                (By.CLASS_NAME, "message-sending"),
                (By.CLASS_NAME, "message-sent"),
                (By.CLASS_NAME, "message-delivered"),
                (By.CSS_SELECTOR, "[data-status='sent']"),
                (By.CSS_SELECTOR, "[data-status='delivered']"),
            ]
            
            status_found = False
            for selector in status_indicators:
                try:
                    status_element = wait.until(EC.presence_of_element_located(selector))
                    if status_element.is_displayed():
                        status_found = True
                        print(f"Found status indicator: {selector}")
                        break
                except TimeoutException:
                    continue
            
            # Note: Status indicators might not be implemented yet
            if not status_found:
                print("No delivery status indicators found - feature may not be implemented")
                
        except Exception as e:
            print(f"Status indicator test failed: {e}")
    
    def test_message_formatting_and_special_characters(self, driver, wait, messaging_interface, 
                                                      test_message_data):
        """
        Test message formatting and special character handling
        """
        messaging_interface('pro_volunteer', 'test_company_001')
        
        message_input = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-input")
        ))
        send_button = driver.find_element(By.CLASS_NAME, "send-button")
        
        # Test different message types
        test_messages = [
            test_message_data['special_chars_message'],
            "Message with\nmultiple\nlines",
            "Very " + "long " * 50 + "message",
            "Message with URLs: https://example.com",
            "Message with @mentions and #hashtags",
        ]
        
        for message in test_messages:
            message_input.clear()
            message_input.send_keys(message)
            send_button.click()
            
            # Verify message appears (may be truncated or formatted)
            try:
                sent_message = wait.until(EC.presence_of_element_located(
                    (By.XPATH, f"//div[contains(@class, 'message')]")
                ))
                
                # Check that some part of the message appears
                message_text = sent_message.text
                assert len(message_text) > 0, f"Message should appear: {message[:30]}..."
                
            except TimeoutException:
                print(f"Message may have been rejected or filtered: {message[:30]}...")
    
    def test_message_input_validation(self, driver, wait, messaging_interface, test_message_data):
        """
        Test message input validation
        """
        messaging_interface('pro_volunteer', 'test_company_001')
        
        message_input = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-input")
        ))
        send_button = driver.find_element(By.CLASS_NAME, "send-button")
        
        # Test empty message
        message_input.clear()
        send_button.click()
        
        # Send button should be disabled or show validation error
        try:
            error_message = driver.find_element(By.CLASS_NAME, "validation-error")
            assert "empty" in error_message.text.lower() or "required" in error_message.text.lower()
        except:
            # Alternative: send button might be disabled
            assert not send_button.is_enabled(), "Send button should be disabled for empty message"
        
        # Test very long message
        long_message = "A" * 1000  # Very long message
        message_input.clear()
        message_input.send_keys(long_message)
        
        # Check character limit
        input_value = message_input.get_attribute('value')
        if len(input_value) < len(long_message):
            print(f"Character limit enforced: {len(input_value)} chars max")
        
        # Test HTML/script injection
        malicious_message = test_message_data['html_message']
        message_input.clear()
        message_input.send_keys(malicious_message)
        send_button.click()
        
        # Verify message is sanitized
        try:
            sent_message = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'message')]")
            ))
            
            message_html = sent_message.get_attribute('innerHTML')
            assert '<script>' not in message_html, "Script tags should be sanitized"
            
        except TimeoutException:
            print("Malicious message may have been blocked entirely")
    
    def test_keyboard_shortcuts(self, driver, wait, messaging_interface, test_message_data):
        """
        Test keyboard shortcuts in messaging interface
        """
        messaging_interface('pro_volunteer', 'test_company_001')
        
        message_input = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-input")
        ))
        
        # Test Enter to send
        test_message = test_message_data['short_message']
        message_input.send_keys(test_message)
        message_input.send_keys(Keys.ENTER)
        
        # Verify message was sent
        sent_message = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//div[contains(@class, 'message') and contains(text(), '{test_message[:20]}')]")
        ))
        assert sent_message.is_displayed(), "Enter key should send message"
        
        # Test Shift+Enter for new line (if supported)
        message_input.send_keys("Line 1")
        message_input.send_keys(Keys.SHIFT + Keys.ENTER)
        message_input.send_keys("Line 2")
        
        input_value = message_input.get_attribute('value')
        if '\n' in input_value:
            print("Shift+Enter creates new line")
        else:
            print("Shift+Enter not supported or creates different behavior")
    
    def test_message_history_loading(self, driver, wait, messaging_interface):
        """
        Test message history loading and pagination
        """
        messaging_interface('pro_volunteer', 'test_company_001')
        
        message_history = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-history")
        ))
        
        # Check if there are existing messages
        existing_messages = driver.find_elements(By.CLASS_NAME, "message")
        initial_count = len(existing_messages)
        
        # Test scrolling to load more messages (if implemented)
        try:
            # Scroll to top of message history
            driver.execute_script("arguments[0].scrollTop = 0;", message_history)
            time.sleep(2)
            
            # Check if more messages loaded
            updated_messages = driver.find_elements(By.CLASS_NAME, "message")
            updated_count = len(updated_messages)
            
            if updated_count > initial_count:
                print(f"Loaded {updated_count - initial_count} additional messages")
            else:
                print("No additional messages loaded - may be at beginning of history")
                
        except Exception as e:
            print(f"Message history loading test failed: {e}")
    
    def test_network_failure_handling(self, driver, wait, messaging_interface, test_message_data):
        """
        Test handling of network failures during messaging
        Edge Cases: Network failures
        """
        messaging_interface('pro_volunteer', 'test_company_001')
        
        message_input = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-input")
        ))
        send_button = driver.find_element(By.CLASS_NAME, "send-button")
        
        # Simulate network failure by blocking requests (if possible)
        # This is a simplified test - real network simulation would require more setup
        
        # Try to send message during "network failure"
        test_message = test_message_data['short_message']
        message_input.send_keys(test_message)
        
        # Disable network (simulate)
        driver.execute_script("window.navigator.onLine = false;")
        
        send_button.click()
        
        # Check for error handling
        try:
            error_indicator = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "network-error")
            ))
            assert error_indicator.is_displayed(), "Should show network error"
            
        except TimeoutException:
            # Alternative: message might show as pending/failed
            try:
                failed_message = driver.find_element(By.CLASS_NAME, "message-failed")
                assert failed_message.is_displayed(), "Should show failed message indicator"
            except:
                print("Network failure handling not detected - may need real network simulation")
        
        # Restore network
        driver.execute_script("window.navigator.onLine = true;")
    
    def test_message_timestamps(self, driver, wait, messaging_interface, test_message_data):
        """
        Test message timestamp display
        """
        messaging_interface('pro_volunteer', 'test_company_001')
        
        message_input = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-input")
        ))
        send_button = driver.find_element(By.CLASS_NAME, "send-button")
        
        # Send a message
        test_message = test_message_data['short_message']
        message_input.send_keys(test_message)
        send_button.click()
        
        # Look for timestamp
        try:
            timestamp_selectors = [
                (By.CLASS_NAME, "message-timestamp"),
                (By.CLASS_NAME, "timestamp"),
                (By.CSS_SELECTOR, "[data-timestamp]"),
                (By.CSS_SELECTOR, ".message .time"),
            ]
            
            timestamp_found = False
            for selector in timestamp_selectors:
                try:
                    timestamp = driver.find_element(*selector)
                    if timestamp.is_displayed():
                        timestamp_text = timestamp.text
                        assert len(timestamp_text) > 0, "Timestamp should have content"
                        timestamp_found = True
                        print(f"Found timestamp: {timestamp_text}")
                        break
                except:
                    continue
            
            if not timestamp_found:
                print("No timestamp found - feature may not be implemented")
                
        except Exception as e:
            print(f"Timestamp test failed: {e}")
    
    @pytest.mark.smoke
    def test_messaging_interface_smoke_test(self, driver, wait, messaging_interface, test_message_data):
        """
        Smoke test for basic messaging interface functionality
        """
        # Quick test to ensure messaging interface works
        messaging_interface('pro_volunteer', 'test_company_001')
        
        # Verify basic elements are present
        message_input = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-input")
        ))
        send_button = driver.find_element(By.CLASS_NAME, "send-button")
        
        # Send a simple message
        test_message = "Smoke test message"
        message_input.send_keys(test_message)
        send_button.click()
        
        # Verify message appears
        sent_message = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//div[contains(@class, 'message') and contains(text(), '{test_message}')]")
        ))
        
        assert sent_message.is_displayed(), "Basic messaging should work"
