# ✅ Test Coverage Tracker – SkilledUp.Life Modules

> **Live Tracker:** The most up-to-date version of this test coverage tracker is maintained in Google Sheets: [Test Coverage Tracker – SkilledUp.Life Modules (Live)](https://docs.google.com/spreadsheets/d/1q2xA4L0VjMm7GEi-NSbk-X55E4FXBHt9O2PLc0jlqhk/edit?usp=sharing)

---

## ℹ️ How to Use This Tracker
- **Purpose:** This tracker helps everyone see which features and modules are covered by tests (unit and E2E) across both frontend and backend.
- **How to update:** After each sprint or feature release, add new tests, update statuses, and keep the 'Last Updated' column current.
- **Where to find live updates:** Always use the [Google Sheets version](https://docs.google.com/spreadsheets/d/1q2xA4L0VjMm7GEi-NSbk-X55E4FXBHt9O2PLc0jlqhk/edit?usp=sharing) for the latest info.

## 🗂️ Quick Glossary
- **Module (Epic):** A major area or section of the app (e.g. Authentication, Messaging)
- **Feature:** A specific function or capability within a module
- **Test Name / Scenario:** The name of the test (unit or E2E)
- **Location (Path):** Where the test file lives in the repo (with a link if possible)
- **Status:**
  - ✅ Done: Test is complete and reliable
  - 🟡 WIP: Test exists but is incomplete or unstable
  - 🔴 Missing: Test needs to be written
- **Regression Test:** A test that confirms previously working features still function correctly after code changes

---

> 📝 **CHANGELOG**
>| Date (DD-MM-YYYY) | Change Description                | Author         |
>|------------|-----------------------------------|----------------|
>| 20-07-2025 | Initial setup                     | Jeremiah Agenyi    |
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

---

## 🧪 Regression Tests

| Module        | Feature         | Regression Scenario         | Description                                           | Tool       | Status     | Last Updated | Location (Path)                       |
|---------------|-----------------|-----------------------------|--------------------------------------------------------|------------|------------|---------------|--------------------------------------|
| Authentication| Login           | Post-refactor login flow    | Ensure dashboard redirect still works after code changes | Playwright | ✅ Done     | 2025-07-29    | frontend/tests/e2e/login-regression.spec.js |
| Profiles       | Email Update    | Persistence after UI overhaul| Confirm updates are saved correctly                   | Selenium   | 🟡 WIP      | 2025-07-29    | frontend/tests/e2e/profile-email.spec.js    |
| Notifications  | Settings Toggle | Silent mode re-trigger test | Verify notification toggle still silences alerts      | Jest       | 🔴 Missing  | 2025-07-29    | backend/tests/NotificationTest.php         |

📌 Notes

- Regression tests protect stable features from unintended breakage.
- Prioritize flows that users rely on or that have broken before.
- Trigger regressions after major refactors, dependency updates, or layout/UI changes.
- Recommended frequency: post-sprint and pre-release.
