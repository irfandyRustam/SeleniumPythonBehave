Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch chrome browser
    When I open Orange HRM homepage
    And Enter username "admin" and password "admin123"
    And Click on Login button
    Then User must successfully login to the Dashboard page