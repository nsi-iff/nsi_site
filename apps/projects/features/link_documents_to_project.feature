Feature: Link documents to project
  As a NSI site administrator
  I want to link documents to projects
  In order to provide additional information on our projects

  Scenario: Show documents related to a project
    Given exist a project:
      | name     | description              | logo                    | sponsor | status | start_date | end_date   |
      | NSI Site | The terrific site of NSI | images/projects/nsi.png | NSI     | aberto | 2010-11-10 | 2011-02-01 |
    And "NSI Site" project has attached the following documents:
      | title     | description                                     | file                   |
      | UML model | UML detailed diagrams for project documentation | files/projects/nsi.png |
    When I go to "the projects page"
    And I click "NSI Site"
    Then I should see "UML model"
    And I should see "UML detailed diagrams for project documentation"
    And I should see a link to "nsi.png" with label "Download"

