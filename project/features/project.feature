Feature: Project maintenance
  As a NSI member
  I want to maintain projects data
  In order to keep the site up to date regarding our projects


  Scenario Outline: Project inclusion
    Given I am on the new project page
    When I fill in "name" with "<name>"
    And I fill in "description" with "<description>"
    And I fill in "situation" with "<situation>"
    And I fill in "start_date" with "<start date>"
    And I fill in "end_date" with "<end date>"
    And I press "Save"
    Then I should see "Project": "<name>"
    And I should see "Description": "<description>"
    And I should see "Situation": "<situation>"
    And I should see "Start date": "<start date>"
    And I should see "End date": "<end date>"

  Examples:
    | name             | description                     | situation | start date | end date   |
    | world domination | NSI plans to conquer the galaxy | opened    | 01/03/2002 | 02/03/2002 |
    | ERP5             | many things ready, lek          | opened    | 01/03/2002 | 02/03/2002 |


  Scenario Outline: Project update
    Given I have the following project:
     | name              | description                         | situation | start_date | end_date   |
     | general agreement | NSI plans to be loved by all people | opened    | 2002-02-01 | 2002-02-02 |
    And I am on the "general agreement" project edit page
    When I fill in "name" with "<name>"
    And I fill in "description" with "<description>"
    And I fill in "situation" with "<situation>"
    And I fill in "start_date" with "<start_date>"
    And I fill in "end_date" with "<end_date>"
    And I press "Save"
    Then I should see "Project": "<name>"
    And I should see "Description": "<description>"
    And I should see "Situation": "<situation>"
    And I should see "Start date": "<start_date>"
    And I should see "End date": "<end_date>"

  Examples:
    | name             | description                     | situation | start_date | end_date   |
    | world domination | NSI plans to conquer the galaxy | opened    | 01/03/2002 | 02/03/2002 |


  Scenario Outline: Project delete
   Given I have the following project:
     | name             | description                     | situation | start_date | end_date   |
     | world domination | NSI plans to conquer the galaxy | opened    | 2002-03-01 | 2002-03-02 |
   And I am on the "<project>" project delete page
   When I press "Delete"
   Then I should see the message "Project successfully deleted"
   And the "<project>" project does not exist

  Examples:
   | project          |
   | world domination |

