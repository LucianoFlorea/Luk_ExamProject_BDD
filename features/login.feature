Feature: Login

Background:
    Given I am on the login page

  @success
  Scenario: Login with valid credentials
    When I enter my username "Admin" and password "admin123"
    And I click on the login button
    Then I should be logged in

  @fail
  Scenario Outline: Login with invalid credentials
    When I enter an invalid username "<username>" and the password "<password>"
    When I click on the login button
    Then I should receive the error message "<error_message>"

    Examples:
      |username             |password   |error_message|
      |Admin                |wrong_pass |Datele de autentificare sunt gresite sau contul este dezactivat. Te rugam sa reincerci.
      |wrong_user@google.com|admin123   |Datele de autentificare sunt gresite sau contul este dezactivat. Te rugam sa reincerci.
      |wrong_user@google.com|wrong_pass |Datele de autentificare sunt gresite sau contul este dezactivat. Te rugam sa reincerci.