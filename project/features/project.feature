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
    | name             | description                     | situation | start date | end date |
    | world domination | NSI plans to conquer the galaxy | opened    | 03/2002    |    -     |
    | ERP5             | many things ready, lek          | opened    | 03/2002    |    -     |


  Scenario Outline: Project update
    Given I have the following project:
      | project           | description                         | situation | start date | end date |
      | general agreement | NSI plans to be loved by all people | opened    | 01/2002    | 02/2002  |
    And I am on the "<project>" project edit page
    When I fill in "Name" with "<name>"
    And I fill in "Description" with "<description>"
    And I select "<situation>" from "Situation"
    And I fill in "Start date" with "<start date>"
    And I fill in "End date" with "<end date>"
    And I press "Save"
    Then I should see "Project: <name>"
    And I should see "Description: <description>"
    And I should see "Situation: <situation>"
    And I should see "Start date: <start date>"
    And I should see "End date: <end date>"

  Examples:
    | project          | description                     | situation | start date | end date |
    | world domination | NSI plans to conquer the galaxy | opened    | 03/2002    |    -     |


  Scenario Outline: Project delete
    Given I have the following project:
      | project           | description                         | situation | start date | end date |
      | general agreement | NSI plans to be loved by all people | opened    | 01/2002    | 02/2002  |
    And I am on the "<project>" page
    When press "Delete"
    Then I should see "Project successfully deleted"
    And the "<project>" project does not exist

  Examples:
    | project          |
    | world domination |

