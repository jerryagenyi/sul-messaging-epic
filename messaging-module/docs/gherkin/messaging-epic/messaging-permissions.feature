Feature: Messaging Permissions
  As a platform user
  I want messaging permissions to be enforced
  So that communication follows business rules

  Background:
    Given the messaging system is configured
    And user roles are properly assigned

  Scenario Outline: User messaging permissions
    Given I am a <user_type>
    And there is a <target_type> with <setting>
    When I visit their profile
    Then I should <visibility> a "Message" button

    Examples:
      | user_type        | target_type | setting    | visibility |
      | PRO Volunteer    | Company     | Setting 4  | see        |
      | Volunteer        | Company     | Setting 4  | not see    |
      | System Admin     | Company     | any        | see        |
      | Volunteer App    | Company     | Setting 4  | see        |

  Scenario: Permission validation on message send
    Given I am a regular Volunteer
    And I somehow access the messaging interface for a Company
    When I attempt to send a message
    Then the system should reject the message
    And I should see an error about insufficient permissions