Feature: Register a new user
  @register
  Scenario: Register with mandatory fields
    Given the login endpoint-1
    When i navigate to register page
    And provide all the fields
    And click on agree button
    And click on Continue button
    Then the user should be registered
  @register
  Scenario: Register without mail-id
      Given the login endpoint-1
      When i navigate to register page
      And provide all the fields except  mail id
      And click on agree button
      And click on Continue button
      Then the warning E-Mail Address does not appear to be valid!should appear
  @register
  Scenario: Register with existing mail id
     Given the login endpoint-1
     When i navigate to register page
     And provide all the fields with exisitng mail id
     And click on agree button
     And click on Continue button
     Then the proper existing mail id warning message should be displayed
  @register
  Scenario: Register without providing any details
        Given the login endpoint-1
        When i navigate to register page
        And click on agree button
        And click on Continue button
        Then the proper warning message should be displayed
