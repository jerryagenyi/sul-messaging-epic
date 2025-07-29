# TDD Development Guide for Messaging Epic

This guide explains how developers can use the existing test suite to implement the messaging epic functionality following Test-Driven Development (TDD) principles.

## 🔄 TDD Workflow Overview

```
1. 🔴 RED: Run tests (they fail - no implementation yet)
2. 🟢 GREEN: Write minimal code to make tests pass
3. 🔵 REFACTOR: Improve code while keeping tests passing
4. ↻ REPEAT: Move to next failing test
```

## 🚀 Getting Started

### 1. Integration with Main Repositories

This messaging epic will be implemented in the main SkilledUp.Life repositories:
- **Frontend**: https://github.com/skilleduplife/frontend
- **Backend**: https://github.com/skilleduplife/backend

#### For Frontend Developers:

```bash
# In your frontend repository
cd /path/to/skilleduplife/frontend

# Create messaging epic directory
mkdir -p src/features/messaging
mkdir -p tests/messaging

# Copy test suite from specification repository
git clone https://github.com/jerryagenyi/skilleduplife-ci.git temp-specs
cp -r temp-specs/tests/* tests/messaging/
cp temp-specs/requirements.txt tests/messaging/
cp temp-specs/pytest.ini tests/messaging/
rm -rf temp-specs

# Install test dependencies
cd tests/messaging
pip install -r requirements.txt

# Verify test setup
python run_tests.py --smoke
```

#### For Backend Developers:

```bash
# In your backend repository
cd /path/to/skilleduplife/backend

# Create messaging API directory
mkdir -p src/api/messaging
mkdir -p tests/messaging

# Copy relevant test specifications
git clone https://github.com/jerryagenyi/skilleduplife-ci.git temp-specs
cp -r temp-specs/docs/* docs/messaging/
cp temp-specs/TDD_DEVELOPMENT_GUIDE.md docs/
rm -rf temp-specs

# The frontend Selenium tests will validate your API endpoints
```

**Expected Result**: All tests should FAIL (🔴 RED phase) - this is correct!

## 🎨 Test Coverage Scope

### ✅ **What This Test Suite Covers (Functional Testing):**
- **Element Presence**: Buttons, inputs, forms, containers exist
- **User Interactions**: Click, type, navigate, send messages
- **Functionality**: Message sending, search, permissions, settings
- **Content Validation**: Text appears, messages are delivered
- **Accessibility**: Keyboard navigation, screen reader support
- **Error Handling**: Network failures, validation errors
- **Cross-browser Compatibility**: Chrome (extensible to others)

### ❌ **What's NOT Covered (Visual Design Testing):**
- **Visual Appearance**: Colors, fonts, spacing, layouts
- **Design Consistency**: Brand guidelines, style guide compliance
- **Visual Regression**: Screenshot comparison over time
- **Pixel-Perfect Design**: Exact positioning, alignment
- **Animation/Transitions**: Smooth transitions, loading states
- **Responsive Design Details**: Exact breakpoint behavior

### 🔧 **To Add Visual Design Testing:**
Consider extending with:
- **Percy** or **Applitools** for visual regression testing
- **Storybook** integration for component visual testing
- **Chromatic** for UI component testing
- **Screenshot comparison** tests in CI/CD pipeline

### 2. Understanding Test Structure

Each test file corresponds to a feature from the test matrix:

| Feature | Test File | What to Implement |
|---------|-----------|-------------------|
| Role Permissions | `test_messaging_permissions.py` | User role checking, permission validation |
| Admin Settings | `test_admin_messaging_settings.py` | Admin dashboard, settings management |
| Profile Buttons | `test_profile_message_button.py` | Message buttons on user profiles |
| Messaging Interface | `test_messaging_interface.py` | Core chat functionality |
| Message Search | `test_message_search.py` | Search across messages |
| Conversation Grouping | `test_conversation_grouping.py` | Message organization |

## 📋 Development Roadmap

### Phase 1: Permission System & UI Foundation

#### Step 1: Role-Based Access Control (Frontend Focus)
```bash
# Run permission tests to see what's needed
python run_tests.py --test test_messaging_permissions.py
```

**Frontend Implementation:**
- Role-based UI component rendering
- Permission checking before showing message buttons
- Integration with existing authentication system
- User role context management

**Backend Implementation:**
- API endpoints for permission validation
- Role-based middleware for messaging routes
- Permission checking service

**Key Test:** `test_messaging_permissions_enforced()`

**🔐 Authentication Note:** This epic assumes authentication is already handled by the main SkilledUp.Life system. We're implementing permission checks for messaging features based on the current authenticated user's role (System Admin, PRO Volunteer, Volunteer, Company). The tests validate that the correct messaging permissions are enforced for each role.

#### Step 2: Profile Integration & Message Buttons
```bash
# Run profile button tests
python run_tests.py --test test_profile_message_button.py
```

**Frontend Implementation:**
- Add message buttons to existing profile components
- Button visibility based on user permissions
- Navigation to messaging interface
- Integration with existing profile pages

**Key Test:** `test_profile_message_button()`

### Phase 2: Core Messaging Functionality

#### Step 3: Messaging Interface & Real-time Communication
```bash
# Run messaging interface tests
python run_tests.py --test test_messaging_interface.py
```

**Frontend Implementation:**
- Message input/output components
- Real-time message updates (WebSocket/SSE)
- Message history display
- Send/receive functionality

**Backend Implementation:**
- Message API endpoints (POST /api/messages, GET /api/messages/:conversationId)
- Real-time message broadcasting
- Message persistence and retrieval

**Key Test:** `test_messaging_interface()`

#### Step 4: Admin Settings Management
```bash
# Run admin settings tests
python run_tests.py --test test_admin_messaging_settings.py
```

**Frontend Implementation:**
- Admin settings dashboard component
- Settings form with toggles and validation
- Real-time settings updates

**Backend Implementation:**
- Admin settings API endpoints
- Settings persistence and validation
- Permission enforcement based on settings

**Key Test:** `test_admin_messaging_settings()`

### Phase 3: Advanced Features

#### Step 5: Message Search & Filtering
```bash
# Run search tests
python run_tests.py --test test_message_search.py
```

**Frontend Implementation:**
- Search input component
- Search results display with highlighting
- Filter and sort functionality

**Backend Implementation:**
- Search API with full-text search capabilities
- Search indexing and optimization
- Advanced search filters

**Key Test:** `test_message_search()`

#### Step 6: Conversation Organization & Grouping
```bash
# Run grouping tests
python run_tests.py --test test_conversation_grouping.py
```

**Frontend Implementation:**
- Conversation list component
- Message grouping by participant
- Sorting and organization UI

**Backend Implementation:**
- Conversation management API
- Message grouping logic
- Conversation metadata handling

**Key Test:** `test_conversation_grouping()`

## 🛠️ TDD Implementation Process

### For Each Feature:

#### 1. Analyze Failing Tests
```bash
# Run specific test to see failures
python run_tests.py --test test_messaging_permissions.py -v

# Look at test code to understand requirements
# File: tests/selenium/test_messaging_permissions.py
```

#### 2. Implement Minimal Solution
Focus on making ONE test pass at a time:

```python
# Example: Making test_messaging_permissions_enforced pass
# The test expects:
# - Login functionality
# - Role-based button visibility
# - Permission validation

# Minimal implementation:
def check_message_button_visibility(user_role, target_type):
    if user_role == 'pro_volunteer' and target_type == 'company':
        return True
    elif user_role == 'system_admin':
        return True
    # ... etc
```

#### 3. Run Tests Again
```bash
# Verify your implementation
python run_tests.py --test test_messaging_permissions.py::TestMessagingPermissions::test_messaging_permissions_enforced
```

#### 4. Refactor and Improve
Once test passes, improve the code:
- Add error handling
- Optimize performance
- Improve code structure
- Add logging

#### 5. Move to Next Test
Repeat process for next failing test.

## 🎯 Key Implementation Areas

### 1. HTML/CSS Selectors
Tests expect specific CSS classes and IDs:

```html
<!-- Message button (test_profile_message_button.py) -->
<button class="message-button">Message</button>

<!-- Messaging interface (test_messaging_interface.py) -->
<div class="messaging-interface">
  <div class="message-history"></div>
  <input class="message-input" />
  <button class="send-button">Send</button>
</div>

<!-- Admin settings (test_admin_messaging_settings.py) -->
<div class="admin-settings">
  <input id="setting_4_toggle" type="checkbox" />
  <button id="save-settings">Save</button>
</div>
```

### 2. User Roles Implementation
```javascript
// Expected user roles from conftest.py
const USER_ROLES = {
  'system_admin': { permissions: ['all'] },
  'pro_volunteer': { permissions: ['message_companies'] },
  'volunteer': { permissions: ['message_volunteers'] },
  'company': { permissions: ['message_volunteers'] }
};
```

### 3. API Endpoints (Suggested)
```
POST /api/auth/login
GET  /api/user/profile/:id
POST /api/messages/send
GET  /api/messages/conversation/:id
GET  /api/messages/search?q=term
POST /api/admin/settings
```

## 🧪 Testing During Development

### Continuous Testing
```bash
# Run tests after each change
python run_tests.py --smoke

# Run specific feature tests
python run_tests.py --marker permissions

# Debug with visible browser
HEADLESS=false python run_tests.py --test test_messaging_interface.py
```

### Test-First Development
1. Read test requirements
2. Write minimal implementation
3. Run test to verify
4. Refactor and improve
5. Commit working code

### CI/CD Integration
Every push triggers:
- Linting and validation
- Full test suite
- Security scanning
- Test result reporting

## 📊 Progress Tracking

### Test Status Dashboard
```bash
# Check overall progress
python run_tests.py

# Generate detailed report
python run_tests.py --html=reports/progress-report.html
```

### Feature Completion Checklist
- [ ] **Permissions**: Role-based access control
- [ ] **Admin Settings**: Configuration management
- [ ] **Profile Buttons**: Message initiation
- [ ] **Messaging Interface**: Core chat functionality
- [ ] **Search**: Message search and filtering
- [ ] **Grouping**: Conversation organization

## 🔧 Development Tips

### 1. Start Simple
- Implement basic functionality first
- Add complexity gradually
- Focus on making tests pass

### 2. Use Test Feedback
- Test failures guide implementation
- Error messages show what's missing
- Screenshots help debug UI issues

### 3. Incremental Development
- One test at a time
- Commit frequently
- Keep tests passing

### 4. Mock External Dependencies
- Use test data from `conftest.py`
- Mock API calls during development
- Focus on UI/UX implementation

## 🚨 Common Pitfalls

1. **Don't implement everything at once** - TDD is incremental
2. **Don't skip the refactor phase** - Clean code is important
3. **Don't change tests to fit implementation** - Tests define requirements
4. **Don't ignore failing tests** - Each failure is a requirement

## 🎉 Success Metrics

### Definition of Done
A feature is complete when:
- ✅ All related tests pass
- ✅ Code is refactored and clean
- ✅ No regressions in other tests
- ✅ CI/CD pipeline passes

### Quality Gates
- All smoke tests pass
- No security vulnerabilities
- Code follows established patterns
- Documentation is updated

---

**Ready to start?** Run `python run_tests.py --smoke` and begin with the first failing test! 🚀

The tests are your specification - implement exactly what they expect, nothing more, nothing less. This is the essence of TDD! 💪
