# Feature 01: Role-Based Messaging Permissions System

## Objective / Purpose
Implement a comprehensive permission system that controls who can message whom based on user roles and subscription levels.

## User Stories (BDD-style)
- As a PRO Volunteer, I want to message companies so I can inquire about opportunities
- As a Company with Plan 2, I want to message volunteers so I can recruit talent
- As a System Administrator, I want to message anyone so I can provide support
- As a Volunteer Applicant, I want to message companies I've applied to so I can follow up

## Acceptance Criteria (Gherkin scenarios)

### Scenario: PRO Volunteer messaging Company
```gherkin
Given I am a PRO Volunteer
And there is a Company with default messaging settings
When I visit the Company's profile
Then I should see a "Message" button
And I should be able to send a message to the Company
```

### Scenario: Regular Volunteer cannot message Company with default settings
```gherkin
Given I am a regular Volunteer (not PRO)
And there is a Company with default messaging settings (Setting 4)
When I visit the Company's profile
Then I should not see a "Message" button
```

### Scenario: System Admin can message anyone
```gherkin
Given I am a System Administrator
When I visit any user's profile
Then I should see a "Message" button
And I should be able to send a message to that user
```

## Functional Requirements
- Permission matrix enforcement for all user types
- Dynamic message button visibility based on permissions
- Role validation before message sending
- Support for 6 different company messaging settings
- Support for volunteer messaging settings

## Edge Cases & Risks
- User role changes during active messaging session
- Company subscription plan changes affecting permissions
- Volunteer status changes (regular to PRO)

## Dependencies / API Contracts
- User role/subscription service
- Profile display components
- Authentication service

## Definition of Done (DoD)
- [ ] Permission matrix implemented and tested
- [ ] Message button visibility works correctly
- [ ] All user role combinations tested
- [ ] API endpoints validate permissions
- [ ] Tests pass in CI