Feature: OrangeHRM Login

  Background: common steps
    Given I launch browser
    When I open application
    And Enter valid username and password
    And Click on Login

  Scenario: Login to HRM Application
    Then User must login to the Dashboard page

  Scenario: Search user
    When Navigate to search page
    Then Search page should display

  Scenario: Advanced search user
    When Navigate to advanced search page
    Then Advanced search page should display