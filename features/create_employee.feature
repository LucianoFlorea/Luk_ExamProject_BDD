Feature: Create Employee
#  In order to create a new employee
#  As a user
#  I want to be able to fill out a form with the employee's information

  Scenario: Create employee with valid information
    Given I am on the employee creation page
    When I fill out the form with the employee's information:
      | employee_id | 12345 |
      | first_name  | John   |
      | last_name   | Doe    |
    And I click on the Save button
    Then the employee should be created and I should be taken to the employee's profile page

  Scenario: Create employee with duplicate information
    Given I am on the employee creation page
    When I fill out the form with the employee's information:
      | employee_id | 12345 |
      | first_name  | John   |
      | last_name   | Doe    |
    And I click on the "Save" button
    Then I should see an error message that says "Employee Id already exists"