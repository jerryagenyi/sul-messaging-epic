# ✅ Test Coverage Tracker – SkilledUp.Life Modules

> 📝 **CHANGELOG**
>| Date       | Change Description                | Author         |
>|------------|-----------------------------------|----------------|
>| 2024-06-07 | Initial template created          | Jeremiah Agenyi    |
>| YYYY-MM-DD | [Describe change]                 | [Your Name]    |

> **Note:** This tracker is best managed in Google Sheets for cross-repo visibility. Use the 'Module > Feature > User Story > Task' structure. Where possible, link the 'Location (Path)' to the actual GitHub file.

# 🧪 Unit Tests

| Module         | Feature         | Test Name               | Description                                 | Location (Path)                                   | Status   | Last Updated |
|---------------|-----------------|------------------------|---------------------------------------------|---------------------------------------------------|----------|--------------|
| Authentication | Login           | User Login              | Valid/invalid login attempts                | [frontend/tests/unit/Login.spec.js](https://github.com/skilleduplife/frontend/blob/main/tests/unit/Login.spec.js) | ✅ Done  | 2024-06-07   |
| Registration   | Form Validation | Register Form Validation| Checks required fields                      | [frontend/tests/unit/Register.spec.js](https://github.com/skilleduplife/frontend/blob/main/tests/unit/Register.spec.js) | 🟡 WIP   | 2024-06-06   |
| API            | Error Handling  | API Error Handling      | Laravel service layer error cases           | [backend/tests/UserServiceTest.php](https://github.com/skilleduplife/backend/blob/main/tests/UserServiceTest.php) | 🔴 Missing| 2024-06-01   |

---

## 🚀 E2E Tests

| Module         | Feature         | Test Scenario          | Flow Description                            | Tool       | Status   | Last Updated | Location (Path)                                   |
|---------------|-----------------|------------------------|----------------------------------------------|------------|----------|--------------|---------------------------------------------------|
| Authentication | Login           | User login → dashboard | From login screen to dashboard success      | Playwright | ✅ Done  | 2024-06-07   | [frontend/tests/e2e/login.spec.js](https://github.com/skilleduplife/frontend/blob/main/tests/e2e/login.spec.js) |
| Authentication | Password Reset  | Forgot password        | Flow from "Forgot password" to reset        | Playwright | 🔴 Missing| 2024-06-01   | [frontend/tests/e2e/forgot-password.spec.js](https://github.com/skilleduplife/frontend/blob/main/tests/e2e/forgot-password.spec.js) |
| User Management| Admin Actions   | Admin adds a user      | Admin logs in and adds a user via form      | Selenium   | 🟡 WIP   | 2024-06-06   | [frontend/tests/e2e/admin-add-user.spec.js](https://github.com/skilleduplife/frontend/blob/main/tests/e2e/admin-add-user.spec.js) |

---

## 📌 Notes
- ✅ Done: Ready and reliable
- 🟡 WIP: Exists but unstable or incomplete
- 🔴 Missing: Needs to be written

> Please update after each sprint or feature release.
