Feature: Project maintenance
  As a NSI member
  I want to maintain projects data
  In order to keep the site up to date regarding our projects

  Scenario Outline: Project inclusion
    Given I want to include a new project named <project>
    When I supply a description <description>
    And I supply a situation <situation>
    And I supply a list of partners <partners>
    And I supply a start date <start date>
    And I supply an end date <end date>
    Then the project name should be <project>
    And the project's description should be <description>
    And the project's situation should be <situation>
    And the project's partners should be <partners>
    And the project's start date should be <start date>
    And the project's end date should be <end date>

    Examples:
      | project | description | situation | partners | start date | end date
      | world domination | NSI plans to conquer the world | opened | 03/2002 | -/- |

  Scenario Outline: Project update
    Given I want to update a project named <project>
    When I supply a description <description>
    And I supply a situation <situation>
    And I supply a list of partners <partners>
    And I supply a start date <start date>
    And I supply an end date <end date>
    Then the project name should be <project>
    And the project's description should be <description>
    And the project's situation should be <situation>
    And the project's partners should be <partners>
    And the project's start date should be <start date>
    And the project's end date should be <end date>

    Examples:
      | project | description | situation | partners | start date | end date
      | world domination | NSI plans to conquer the galaxy | opened | 03/2002 | -/- |

  Scenario Outline: Project delete
    Given I want to delete a project named <project>
    When I confirm the exclusion of the project <project>
    Then the project <project> should be deleted

    Examples:
      | project
      | world domination

