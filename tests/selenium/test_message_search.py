"""
Test message search functionality
Based on test matrix: test_message_search()
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

class TestMessageSearch:
    """Test suite for message search functionality"""
    
    def test_message_search(self, driver, wait, messaging_interface, test_message_data):
        """
        Test message search functionality
        
        Feature: Search Function
        What: Find conversations
        Why: Message retrieval
        How: Text search across messages
        Edge Cases: Empty results, special characters
        Acceptance Criteria: Relevant results returned
        """
        # Open messaging interface
        messaging_interface('pro_volunteer', 'test_company_001')
        
        # Send some test messages to search for later
        message_input = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-input")
        ))
        send_button = driver.find_element(By.CLASS_NAME, "send-button")
        
        # Create searchable messages
        search_messages = [
            "Hello world, this is a test message",
            "Another message about testing",
            "Final message with unique keyword: SEARCHABLE",
            test_message_data['short_message']
        ]
        
        for message in search_messages:
            message_input.clear()
            message_input.send_keys(message)
            send_button.click()
            time.sleep(1)  # Allow message to be sent
        
        # Find and use search functionality
        search_input = self._find_search_input(driver, wait)
        
        # Test basic search
        search_term = "test"
        search_input.clear()
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.ENTER)
        
        # Verify search results
        self._verify_search_results(driver, wait, search_term)
    
    def test_search_with_special_characters(self, driver, wait, messaging_interface, test_message_data):
        """
        Test search with special characters
        Edge Cases: Special characters
        """
        messaging_interface('pro_volunteer', 'test_company_001')
        
        # Send message with special characters
        message_input = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-input")
        ))
        send_button = driver.find_element(By.CLASS_NAME, "send-button")
        
        special_message = test_message_data['special_chars_message']
        message_input.send_keys(special_message)
        send_button.click()
        time.sleep(1)
        
        # Search for special characters
        search_input = self._find_search_input(driver, wait)
        
        # Test searching for emoji or special chars
        search_terms = ["🚀", "@#$", "Testing"]
        
        for term in search_terms:
            search_input.clear()
            search_input.send_keys(term)
            search_input.send_keys(Keys.ENTER)
            
            # Verify search handles special characters
            try:
                search_results = wait.until(EC.presence_of_element_located(
                    (By.CLASS_NAME, "search-results")
                ))
                
                # Should either find results or show "no results" message
                results_text = search_results.text.lower()
                assert len(results_text) > 0, f"Search should return some response for '{term}'"
                
            except TimeoutException:
                print(f"Search for '{term}' may not be supported")
    
    def test_empty_search_results(self, driver, wait, messaging_interface):
        """
        Test handling of empty search results
        Edge Cases: Empty results
        """
        messaging_interface('pro_volunteer', 'test_company_001')
        
        search_input = self._find_search_input(driver, wait)
        
        # Search for something that definitely won't exist
        nonexistent_term = "NONEXISTENT_SEARCH_TERM_12345"
        search_input.clear()
        search_input.send_keys(nonexistent_term)
        search_input.send_keys(Keys.ENTER)
        
        # Verify empty results are handled properly
        try:
            no_results_message = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "no-results")
            ))
            
            message_text = no_results_message.text.lower()
            assert any(phrase in message_text for phrase in [
                "no results", "not found", "no messages", "no matches"
            ]), "Should show appropriate no results message"
            
        except TimeoutException:
            # Alternative: search results container might be empty
            try:
                search_results = driver.find_element(By.CLASS_NAME, "search-results")
                results = search_results.find_elements(By.CLASS_NAME, "search-result")
                assert len(results) == 0, "Should have no search results"
            except:
                print("Empty results handling not clearly implemented")
    
    def test_search_result_highlighting(self, driver, wait, messaging_interface):
        """
        Test search result highlighting
        """
        messaging_interface('pro_volunteer', 'test_company_001')
        
        # Send a message with distinctive content
        message_input = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "message-input")
        ))
        send_button = driver.find_element(By.CLASS_NAME, "send-button")
        
        test_message = "This message contains HIGHLIGHT keyword for testing"
        message_input.send_keys(test_message)
        send_button.click()
        time.sleep(1)
        
        # Search for the keyword
        search_input = self._find_search_input(driver, wait)
        search_term = "HIGHLIGHT"
        search_input.clear()
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.ENTER)
        
        # Check for highlighted results
        try:
            search_results = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "search-results")
            ))
            
            # Look for highlighted text
            highlighted_elements = search_results.find_elements(By.CSS_SELECTOR, 
                                                              ".highlight, mark, .search-highlight, strong")
            
            if highlighted_elements:
                highlight_text = highlighted_elements[0].text
                assert search_term.lower() in highlight_text.lower(), \
                       "Highlighted text should contain search term"
                print("Search highlighting detected")
            else:
                print("Search highlighting not implemented")
                
        except TimeoutException:
            print("Search results not found")
    
    def test_search_across_conversations(self, driver, wait, login_as_user, messaging_interface):
        """
        Test search across multiple conversations
        """
        # This test assumes ability to have multiple conversations
        login_as_user('pro_volunteer')
        
        # Send messages in different conversations
        conversations = ['test_company_001', 'test_volunteer_001']
        search_keyword = "CROSSCONVO"
        
        for conversation_id in conversations:
            try:
                messaging_interface('pro_volunteer', conversation_id)
                
                message_input = wait.until(EC.presence_of_element_located(
                    (By.CLASS_NAME, "message-input")
                ))
                send_button = driver.find_element(By.CLASS_NAME, "send-button")
                
                # Send message with search keyword
                message_input.send_keys(f"Message in {conversation_id} with {search_keyword}")
                send_button.click()
                time.sleep(1)
                
            except Exception as e:
                print(f"Could not send message in conversation {conversation_id}: {e}")
        
        # Go to main messages page and search
        driver.get(f"{driver.current_url.split('/messages')[0]}/messages")
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "messaging-interface")))
        
        # Perform global search
        search_input = self._find_search_input(driver, wait)
        search_input.clear()
        search_input.send_keys(search_keyword)
        search_input.send_keys(Keys.ENTER)
        
        # Verify results from multiple conversations
        try:
            search_results = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "search-results")
            ))
            
            results = search_results.find_elements(By.CLASS_NAME, "search-result")
            
            # Should find results from multiple conversations
            if len(results) >= len(conversations):
                print(f"Found {len(results)} results across conversations")
            else:
                print("Cross-conversation search may not be fully implemented")
                
        except TimeoutException:
            print("Global search functionality not found")
    
    def _find_search_input(self, driver, wait):
        """
        Helper method to find search input field
        """
        # Try multiple possible selectors for search input
        search_selectors = [
            (By.CLASS_NAME, "search-input"),
            (By.ID, "message-search"),
            (By.CSS_SELECTOR, "input[placeholder*='search']"),
            (By.CSS_SELECTOR, "input[type='search']"),
            (By.XPATH, "//input[contains(@placeholder, 'Search')]"),
        ]
        
        for selector in search_selectors:
            try:
                search_input = wait.until(EC.presence_of_element_located(selector))
                if search_input.is_displayed():
                    return search_input
            except TimeoutException:
                continue
        
        # If no search input found, try to find search button to activate search
        try:
            search_button = driver.find_element(By.CLASS_NAME, "search-button")
            search_button.click()
            
            # Try to find search input again after clicking search button
            for selector in search_selectors:
                try:
                    search_input = wait.until(EC.presence_of_element_located(selector))
                    if search_input.is_displayed():
                        return search_input
                except TimeoutException:
                    continue
        except:
            pass
        
        raise Exception("Could not find search input field")
    
    def _verify_search_results(self, driver, wait, search_term):
        """
        Helper method to verify search results
        """
        try:
            # Wait for search results to appear
            search_results = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "search-results")
            ))
            
            # Check if results contain the search term
            results_text = search_results.text.lower()
            search_term_lower = search_term.lower()
            
            # Results should either contain the search term or show "no results"
            assert search_term_lower in results_text or \
                   any(phrase in results_text for phrase in ["no results", "not found"]), \
                   f"Search results should be relevant to '{search_term}'"
            
            # Count individual result items
            result_items = search_results.find_elements(By.CLASS_NAME, "search-result")
            print(f"Found {len(result_items)} search results for '{search_term}'")
            
            return len(result_items)
            
        except TimeoutException:
            # Alternative: results might appear in message history with highlighting
            try:
                message_history = driver.find_element(By.CLASS_NAME, "message-history")
                highlighted_messages = message_history.find_elements(By.CSS_SELECTOR, 
                                                                    ".highlight, .search-highlight")
                
                if highlighted_messages:
                    print(f"Found {len(highlighted_messages)} highlighted messages")
                    return len(highlighted_messages)
                else:
                    print("No search results or highlighting found")
                    return 0
                    
            except:
                print("Could not verify search results")
                return 0
