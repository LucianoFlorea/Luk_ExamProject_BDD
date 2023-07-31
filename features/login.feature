Feature: Login

Background:
    Given I am on the login page

  @success
  Scenario: Login with valid credentials
    When I enter my username "Admin" and password "admin123"
    When I click on the login button
    Then I should be logged in

  Scenario: Logout from website
    When I click on logout button
    Then I should be logged out

  @fail
  Scenario Outline: Login with invalid credentials
    When I enter my username "<username>" and password "<password>"
    When I click on the login button
    Then I should receive the error message "<error_message>"

    Examples:
      |username             |password   |error_message      |
      |Admin                |wrong_pass |Invalid credentials|
      |wrong_user@google.com|admin123   |Invalid credentials|
      |wrong_user@google.com|wrong_pass |Invalid credentials|