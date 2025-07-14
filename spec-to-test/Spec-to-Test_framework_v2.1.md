# Spec-to-Test Framework (Unified)

---

## 📚 Table of Contents
1. Background & Purpose
2. Team Development Standards
3. Unified Spec-to-Test Workflow
4. 📊 Summary Table: Artefacts & Locations
5. Feature Specification Template
6. Step-by-Step Implementation Guidance
7. Onboarding & Workflow Tips

---

## 1. Background & Purpose

- Make development seamless and unified for a distributed, volunteer-driven team.
- Reduce bugs and broken code after merges.
- Ensure everyone works from the same clear, testable specifications.
- Minimise onboarding friction and “works on my machine” problems.
- Enable fast, reliable delivery of new features with confidence.

---

## 2. Team Development Standards

- **GitHub Actions is the main gatekeeper for code quality.**
  - All tests and checks run in CI before merging.
  - Multiple workflow YAML files can exist in the `.github/workflows/` folder per repo (frontend and backend). Each YAML file represents a separate workflow (e.g., `run-tests.yml`, `lint.yml`, `deploy.yml`).
- **Documentation, specs, and tests must be clearly organised and accessible in each repo.**

---

## 3. Unified Spec-to-Test Workflow

1. **Write a Clear Feature Specification**
   - Use the provided template (see section 5).
   - Include: feature title, objective, user stories, requirements, edge cases, dependencies, and definition of done.
   - **Location:** `/docs/specs/` or similar in the relevant repo (frontend or backend).

2. **Write Gherkin Scenarios (BDD)**
   - For each user story/acceptance criterion, write a Gherkin scenario in plain language.
   - These scenarios are the single source of truth for expected behaviour.
   - **Location:** `/docs/gherkin/` or `/tests/features/` in the relevant repo.

3. **Feature Test Table**
   - Map Gherkin scenarios to specific tests (unit, integration, E2E) and track coverage/ownership.
   - **Location:** `/docs/specs/` or `/docs/testing/` in the relevant repo.

4. **Implement Automated Tests (TDD)**
   - Write automated tests (unit/integration/E2E) before or alongside feature development, guided by the Gherkin scenarios.
   - Tests must pass in CI (GitHub Actions) before merging.
   - **Location:** `/tests/` or `/src/__tests__/` in the relevant repo.

5. **Develop the Feature**
   - Implement the feature, aiming to pass all the tests.
   - **Location:** `/src/` in the relevant repo.

6. **Review & Merge**
   - PRs are only merged if all tests pass in CI.
   - QA and PO review against the Gherkin scenarios and acceptance criteria.

---

## 4. 📊 Summary Table: Artefacts & Locations

| Artefact/Step             | Who         | Output                        | Tool/Format         | Repo(s)         | Folder/Path                  | File Type         |
|---------------------------|-------------|-------------------------------|---------------------|-----------------|------------------------------|-------------------|
| 1. Write spec             | PO/Lead     | Feature spec                  | Markdown/Template   | Frontend/Backend| `/docs/specs/`               | `.md`             |
| 2. Write Gherkin          | PO/QA/Lead  | Gherkin scenarios             | `.feature` files    | Frontend/Backend| `/docs/gherkin/` or `/tests/features/` | `.feature`        |
| 3. Map to Test Table      | QA/Lead     | Test matrix                   | Table/Sheet         | Frontend/Backend| `/docs/specs/` or `/docs/testing/` | `.md`/spreadsheet |
| 4. Write tests            | Dev/QA      | Automated tests               | Code                | Frontend/Backend| `/tests/` or `/src/__tests__/`| `.js`/`.py`/etc.  |
| 5. Implement feature      | Dev         | Code                          | Code                | Frontend/Backend| `/src/`                      | `.js`/`.vue`/etc. |
| 6. Run tests in CI        | GitHub      | Test results                  | GitHub Actions      | Frontend/Backend| `.github/workflows/`          | `.yml`            |
| 7. Review & merge         | Lead/QA     | PR review                     | GitHub              | Frontend/Backend| PRs                          | -                 |

---

## 5. Feature Specification Template

1. **Feature Title**
2. **Objective / Purpose**
3. **User Stories (BDD-style)**
4. **Acceptance Criteria (Gherkin scenarios)**
5. **Functional Requirements**
6. **Edge Cases & Risks**
7. **Dependencies / API Contracts**
8. **Definition of Done (DoD)**

---

## 6. Step-by-Step Implementation Guidance

1. **Create the Feature Specification Document**
   - Define the feature name, objective, and user stories.
   - List functional requirements and expected user flows.
   - Include edge cases, system dependencies, and risks.
   - Use the full Feature Specification Template for consistency.

2. **Develop the Spec-to-Test Matrix**
   - For each feature, extract: what it does, why it matters, how it behaves, acceptance criteria, suggested unit/component test names.
   - Use one matrix per module or epic, depending on scale.
   - Make the matrix shareable with devs and QA (Google Sheet, Notion table, or Airtable).

3. **Generate Test Cases or Test File Stubs**
   - Draft test case titles from the matrix (e.g., `test_user_can_save_opportunity()`).
   - Work with QA and devs to create placeholder test files:
     - **Frontend:** `ComponentName.test.js` or `.test.jsx`
     - **Backend:** `test_routes.py` or `test_api_save_profile.py`

4. **Create GitHub Issues for Tracking**
   - For each test row: open a GitHub issue, label it as `test-case`, `qa`, or `tdd`, tag the dev or QA responsible, and paste the corresponding row from the table into the issue body.

5. **Draft Dev Workflow Recommendations**
   - Suggest file naming standards (`ComponentName.test.js`)
   - Recommend test placement (next to component or in a `__tests__` folder)
   - Propose a GitHub Actions file to run tests on every PR

6. **Kick Off a Mini Test Alignment Session**
   - Share your document and test table with the team.
   - Run a 15–30 minute sync to assign ownership for each test, confirm spec understanding, and ensure everyone agrees on “definition of done” for the feature.

---

## 7. Onboarding & Workflow Tips

- Gherkin scenarios and the Feature Test Table are required for all new features. Use them as the basis for tests and QA.
- Automated tests must pass in GitHub Actions before merging any PR.
- Keep documentation concise and up to date for easy onboarding.
- Use the summary table above to know exactly where to place each artefact in the repo.

---

*This framework is designed to keep things simple, unified, and robust for a volunteer-driven, distributed team. Focus on clarity, automation, and shared understanding to reduce bugs and speed up delivery.*

