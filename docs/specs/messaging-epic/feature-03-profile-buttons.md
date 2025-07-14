# Feature 03: Profile Message Buttons Integration

## Objective / Purpose
Integrate "Message" buttons into company and volunteer profile displays that respect permission settings and initiate conversations.

## User Stories (BDD-style)
- As a user, I want to see a Message button on profiles I can contact so I can start conversations
- As a user, I want the Message button to open a messaging interface so I can send messages easily
- As a profile owner, I want to control who can message me through my profile

## Acceptance Criteria (Gherkin scenarios)

### Scenario: Message button appears on company profile
```gherkin
Given I am a PRO Volunteer
And I visit a company profile at "/company/ebdex21"
And the company has messaging enabled for PRO Volunteers
When the profile loads
Then I should see a "Message" button
```

### Scenario: Message button opens messaging interface
```gherkin
Given I can see a "Message" button on a profile
When I click the "Message" button
Then a messaging interface should open
And I should be able to compose a message
And the recipient should be pre-selected
```

### Scenario: No message button for unauthorized users
```gherkin
Given I am a regular Volunteer
And I visit a company profile with default settings
When the profile loads
Then I should not see a "Message" button
```

## Functional Requirements
- Message button component integration
- Permission-based button visibility
- Click handler to open messaging interface
- Consistent styling across profile types
- Mobile-responsive design

## Edge Cases & Risks
- Button state during permission changes
- Loading states and error handling
- Profile data inconsistencies

## Dependencies / API Contracts
- Profile display components
- Messaging interface component
- Permission validation service

## Definition of Done (DoD)
- [ ] Message buttons integrated in company profiles
- [ ] Message buttons integrated in volunteer profiles
- [ ] Permission-based visibility working
- [ ] Click handlers open messaging interface
- [ ] Mobile responsive design
- [ ] Tests pass in CI