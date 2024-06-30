Feature: Login functionality
  @login @POM1
    #this 'Scenario Outline: ' is used for parameterizing the values , like here different sets of mailid and password.
Scenario Outline: Login with valid credentials
    Given the login endpoints
    When the valid emailid as "<email>" and password as "<password>" in to the fields
    And clicked on login button
    Then the system should log the user

    Examples:
      | email                   | password   |
      | swetha5.viji@gmail.com  | Swetha53@  |
      | swetha51.viji@gmail.com | Swe17@     |

  @login
  Scenario: Login with in-valid mail id and valid password
      Given the login endpoints
      When the in-valid email and valid password is entered in to the fields
      And clicked on login button
      Then the proper warning message should be shown
  @login
  Scenario: Login with valid email id and invalid password
        Given the login endpoints
        When valid email id and invalid password is entered in to the field
        And clicked on login button
        Then the proper warning message should be shown
  Scenario: Login with invalid credentials
      Given the login endpoints
      When invalid mail id and password is entered in to the fields
      And clicked on login button
      Then the proper warning message should be shown
