Feature: Search
  @customName
  Scenario: Search with valid products
     Given the login endpoint1
     When the valid products is entered
     And clicked on Search button
     Then the system should display the products matching the keyword
  @customName
  Scenario: Search with  in-valid  products
     Given the login endpoint1
     When the in-valid product is entered
     And clicked on Search button
     Then the system should display the appropriate message
   @customName
  Scenario:  Search with blank keyword
        Given the login endpoint1
        When search button is left as blank
        And clicked on Search button
        Then the system should display the appropriate message
