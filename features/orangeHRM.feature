Feature: OrangeHRM Logo
  Scenario: Logo presence on OrangeHRM Home Page
    Given launch chrome browser
    When open Orange HRM homepage
    Then verify that the logo present on page
    And close browser