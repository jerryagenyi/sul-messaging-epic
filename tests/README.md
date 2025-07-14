# Messaging Epic Test Suite

This directory contains comprehensive Selenium-based tests for the messaging epic functionality, based on the test matrix defined in `docs/testing/messaging-epic/test-matrix.md`.

## Test Structure

```
tests/
├── conftest.py                           # Pytest configuration and fixtures
├── selenium/                             # Selenium test files
│   ├── test_messaging_permissions.py     # Role-based permission tests
│   ├── test_admin_messaging_settings.py  # Admin settings configuration tests
│   ├── test_profile_message_button.py    # Profile button functionality tests
│   ├── test_messaging_interface.py       # Core messaging interface tests
│   ├── test_message_search.py           # Message search functionality tests
│   └── test_conversation_grouping.py    # Conversation organization tests
└── unit/                                 # Unit tests (placeholder)
```

## Test Coverage

Based on the test matrix, the following features are covered:

| Feature | Test File | Test Function | Status |
|---------|-----------|---------------|--------|
| Role Permissions | `test_messaging_permissions.py` | `test_messaging_permissions_enforced()` | ✅ |
| Admin Settings | `test_admin_messaging_settings.py` | `test_admin_messaging_settings()` | ✅ |
| Profile Buttons | `test_profile_message_button.py` | `test_profile_message_button()` | ✅ |
| Message Interface | `test_messaging_interface.py` | `test_messaging_interface()` | ✅ |
| Search Function | `test_message_search.py` | `test_message_search()` | ✅ |
| Conversation Grouping | `test_conversation_grouping.py` | `test_conversation_grouping()` | ✅ |

## Prerequisites

1. **Python 3.11+**
2. **Chrome Browser** (latest version)
3. **ChromeDriver** (automatically managed by webdriver-manager)

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Verify installation:
```bash
python -c "import selenium; print('Selenium version:', selenium.__version__)"
```

## Running Tests

### Quick Start

```bash
# Run all tests
python run_tests.py

# Run smoke tests only
python run_tests.py --smoke

# Run specific test file
python run_tests.py --test test_messaging_permissions.py

# Run tests with specific marker
python run_tests.py --marker permissions
```

### Using pytest directly

```bash
# Run all Selenium tests
pytest tests/selenium/ -v

# Run smoke tests
pytest tests/selenium/ -m smoke

# Run specific test
pytest tests/selenium/test_messaging_permissions.py::TestMessagingPermissions::test_messaging_permissions_enforced

# Generate HTML report
pytest tests/selenium/ --html=reports/test-report.html --self-contained-html
```

### Parallel Execution

```bash
# Run tests in parallel (requires pytest-xdist)
pip install pytest-xdist
python run_tests.py --parallel 4
```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `BASE_URL` | `https://skilledup.life` | Base URL for testing |
| `HEADLESS` | `true` | Run browser in headless mode |
| `TIMEOUT` | `10` | Default timeout for web elements (seconds) |
| `WINDOW_SIZE` | `1920,1080` | Browser window size |

### Test Configuration

Edit `pytest.ini` to modify test behavior:

```ini
[tool:pytest]
addopts = -v --tb=short --html=reports/test-report.html
markers =
    smoke: Quick smoke tests
    integration: Full integration tests
    permissions: Permission-related tests
```

## Test Data

Tests use the following user roles (defined in `conftest.py`):

- **System Admin**: Full access to all features
- **PRO Volunteer**: Enhanced messaging permissions
- **Volunteer**: Basic messaging permissions
- **Volunteer App**: App-specific permissions
- **Company**: Company user permissions

## Test Markers

Use markers to run specific test categories:

```bash
# Run smoke tests
pytest -m smoke

# Run permission tests
pytest -m permissions

# Run messaging tests
pytest -m messaging

# Run admin tests
pytest -m admin
```

## Reports

Test reports are generated in the `reports/` directory:

- **HTML Reports**: `test-report.html` (human-readable)
- **JUnit XML**: `junit.xml` (CI/CD integration)
- **Screenshots**: `screenshots/` (on test failures)

## Debugging

### Running Tests in Non-Headless Mode

```bash
# See browser during test execution
HEADLESS=false python run_tests.py

# Or using pytest directly
HEADLESS=false pytest tests/selenium/test_messaging_permissions.py -v
```

### Taking Screenshots

Screenshots are automatically taken on test failures and saved to `screenshots/`.

### Verbose Logging

```bash
# Enable verbose logging
pytest tests/selenium/ -v -s --log-cli-level=DEBUG
```

## CI/CD Integration

The test suite is integrated with GitHub Actions (`.github/workflows/ci.yml`):

1. **Lint and Validate**: Markdown and Gherkin syntax checking
2. **Setup Environment**: Python, Chrome, ChromeDriver installation
3. **Unit Tests**: Run unit tests (when available)
4. **Integration Tests**: Run Selenium tests
5. **Security Scan**: Vulnerability scanning
6. **Deploy Docs**: Documentation deployment

## Test Development Guidelines

### Adding New Tests

1. Create test file in `tests/selenium/`
2. Follow naming convention: `test_feature_name.py`
3. Use class-based organization: `class TestFeatureName:`
4. Add appropriate markers: `@pytest.mark.smoke`
5. Update this README with new test information

### Test Structure

```python
class TestFeatureName:
    def test_main_functionality(self, driver, wait, fixtures):
        """
        Test description based on test matrix
        
        Feature: Feature Name
        What: What it does
        Why: Why it's needed
        How: How it works
        Edge Cases: Edge cases to test
        Acceptance Criteria: Success criteria
        """
        # Test implementation
        pass
    
    @pytest.mark.smoke
    def test_smoke_functionality(self, driver, wait):
        """Quick smoke test"""
        pass
```

### Best Practices

1. **Use Page Object Model** for complex pages
2. **Explicit waits** over implicit waits
3. **Descriptive test names** and docstrings
4. **Independent tests** (no test dependencies)
5. **Cleanup** after tests (handled by fixtures)
6. **Error handling** for flaky elements
7. **Screenshots** on failures (automatic)

## Troubleshooting

### Common Issues

1. **ChromeDriver version mismatch**:
   ```bash
   pip install --upgrade webdriver-manager
   ```

2. **Element not found**:
   - Check selectors in test files
   - Verify application is running
   - Increase timeout values

3. **Tests timing out**:
   - Increase `TIMEOUT` environment variable
   - Check network connectivity
   - Verify application performance

4. **Permission errors**:
   - Verify user credentials in `conftest.py`
   - Check application user roles
   - Ensure test data is properly set up

### Getting Help

1. Check test logs in `reports/`
2. Review screenshots in `screenshots/`
3. Run tests in non-headless mode for debugging
4. Check GitHub Actions logs for CI/CD issues

## Contributing

1. Follow existing test patterns
2. Add appropriate markers and documentation
3. Update test matrix when adding new tests
4. Ensure tests pass in CI/CD pipeline
5. Update this README for significant changes
