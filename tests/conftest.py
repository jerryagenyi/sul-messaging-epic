"""
Pytest configuration and fixtures for messaging epic tests
"""
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from faker import Faker

# Test configuration
TEST_CONFIG = {
    'base_url': os.getenv('BASE_URL', 'https://skilledup.life'),
    'timeout': int(os.getenv('TIMEOUT', '10')),
    'headless': os.getenv('HEADLESS', 'true').lower() == 'true',
    'window_size': os.getenv('WINDOW_SIZE', '1920,1080'),
}

# User roles for testing
USER_ROLES = {
    'system_admin': {
        'username': 'admin@skilledup.life',
        'password': 'admin_password',
        'role': 'System Admin'
    },
    'pro_volunteer': {
        'username': 'pro@skilledup.life', 
        'password': 'pro_password',
        'role': 'PRO Volunteer'
    },
    'volunteer': {
        'username': 'volunteer@skilledup.life',
        'password': 'volunteer_password', 
        'role': 'Volunteer'
    },
    'volunteer_app': {
        'username': 'app@skilledup.life',
        'password': 'app_password',
        'role': 'Volunteer App'
    },
    'company': {
        'username': 'company@skilledup.life',
        'password': 'company_password',
        'role': 'Company'
    }
}

@pytest.fixture(scope="session")
def faker_instance():
    """Faker instance for generating test data"""
    return Faker()

@pytest.fixture(scope="function")
def driver():
    """WebDriver fixture with Chrome configuration"""
    chrome_options = Options()
    
    if TEST_CONFIG['headless']:
        chrome_options.add_argument('--headless')
    
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=' + TEST_CONFIG['window_size'])
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-plugins')
    chrome_options.add_argument('--disable-images')
    
    # Install and setup ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Set implicit wait
    driver.implicitly_wait(TEST_CONFIG['timeout'])
    
    yield driver
    
    # Cleanup
    driver.quit()

@pytest.fixture(scope="function")
def wait(driver):
    """WebDriverWait fixture"""
    return WebDriverWait(driver, TEST_CONFIG['timeout'])

@pytest.fixture(scope="function")
def login_as_user(driver, wait):
    """Factory fixture for logging in as different user types"""
    def _login(user_type):
        if user_type not in USER_ROLES:
            raise ValueError(f"Unknown user type: {user_type}")
        
        user = USER_ROLES[user_type]
        
        # Navigate to login page
        driver.get(f"{TEST_CONFIG['base_url']}/login")
        
        # Fill login form
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        
        username_field.clear()
        username_field.send_keys(user['username'])
        password_field.clear()
        password_field.send_keys(user['password'])
        login_button.click()
        
        # Wait for successful login
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dashboard")))
        
        return user
    
    return _login

@pytest.fixture(scope="function")
def navigate_to_profile(driver, wait):
    """Factory fixture for navigating to user profiles"""
    def _navigate(profile_type, profile_id=None):
        if profile_id:
            url = f"{TEST_CONFIG['base_url']}/profile/{profile_type}/{profile_id}"
        else:
            url = f"{TEST_CONFIG['base_url']}/profiles/{profile_type}"
        
        driver.get(url)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "profile-container")))
        
    return _navigate

@pytest.fixture(scope="function") 
def admin_settings_page(driver, wait, login_as_user):
    """Navigate to admin settings page"""
    login_as_user('system_admin')
    driver.get(f"{TEST_CONFIG['base_url']}/admin/messaging-settings")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "admin-settings")))
    return driver

@pytest.fixture(scope="function")
def messaging_interface(driver, wait, login_as_user):
    """Navigate to messaging interface"""
    def _open_messaging(user_type='pro_volunteer', target_user_id=None):
        login_as_user(user_type)
        
        if target_user_id:
            driver.get(f"{TEST_CONFIG['base_url']}/messages/{target_user_id}")
        else:
            driver.get(f"{TEST_CONFIG['base_url']}/messages")
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "messaging-interface")))
        
    return _open_messaging

# Test data fixtures
@pytest.fixture(scope="function")
def test_message_data(faker_instance):
    """Generate test message data"""
    return {
        'short_message': faker_instance.sentence(nb_words=5),
        'long_message': faker_instance.text(max_nb_chars=500),
        'special_chars_message': "Hello! @#$%^&*()_+ Testing 123 🚀",
        'empty_message': "",
        'html_message': "<script>alert('test')</script>Hello World",
        'search_term': faker_instance.word(),
    }

@pytest.fixture(scope="function")
def test_user_data(faker_instance):
    """Generate test user data"""
    return {
        'company_name': faker_instance.company(),
        'volunteer_name': faker_instance.name(),
        'email': faker_instance.email(),
        'phone': faker_instance.phone_number(),
    }

# Utility functions
def take_screenshot(driver, test_name):
    """Take screenshot for failed tests"""
    timestamp = int(time.time())
    screenshot_path = f"screenshots/{test_name}_{timestamp}.png"
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(screenshot_path)
    return screenshot_path

def wait_for_element_text(wait, locator, expected_text, timeout=10):
    """Wait for element to contain specific text"""
    return wait.until(
        EC.text_to_be_present_in_element(locator, expected_text),
        message=f"Expected text '{expected_text}' not found in element {locator}"
    )

def wait_for_element_clickable(wait, locator, timeout=10):
    """Wait for element to be clickable"""
    return wait.until(
        EC.element_to_be_clickable(locator),
        message=f"Element {locator} not clickable within {timeout} seconds"
    )

# Pytest hooks
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failure"""
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs.get('driver')
        if driver:
            take_screenshot(driver, item.name)

@pytest.fixture(autouse=True)
def setup_test_environment():
    """Setup test environment before each test"""
    # Create necessary directories
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    
    yield
    
    # Cleanup after test
    pass
