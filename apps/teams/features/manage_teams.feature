Feature: Team maintenance
  As a NSI site administrator
  I want to handle team data
  In order to know details about at team

  Scenario: Teams page
    Given exist a team:
      | name          | description                          |
      | Site NSI      | Grupo de desenvolvimento do site NSI |
    When I go to the teams page
    Then I should see "Site NSI"
    And I should see "Grupo de desenvolvimento do site NSI"
