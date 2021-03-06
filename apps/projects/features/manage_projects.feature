Feature: Project maintenance
  As a NSI site administrator
  I want to handle project data
  In order to know what we are doing and what we did

  Scenario: Projects page
    Given exist a project:
      | name     | description              | github           | logo                    	  | sponsor | status     | start_date | end_date   |
      | NSI Site | The terrific site of NSI | nsi-iff/nsi_site | test/images/projects/nsi.png | NSI     | finalizado | 2010-11-10 | 2011-02-01 |
      
    When I go to "the projects page"
    Then I should see "1 projeto"
    And I should see "NSI Site"
    And I should see "The terrific site of NSI"
    And I should see an image called "nsi.png"

    When I go to the "NSI Site" project page

    Then I should see a label "nsi-iff/nsi_site" with the link to "http://github.com/nsi-iff/nsi_site"


  Scenario: Projects page for non-closed projects
    Given exist a project:
      | name     | description              | logo                         | sponsor | status | start_date |
      | NSI Site | The terrific site of NSI | test/images/projects/nsi.png | NSI     | aberto | 2010-11-10 |
    When I go to "the projects page"
    Then I should see "1 projeto"
    And I should see "NSI Site"
    And I should see "The terrific site of NSI"
    And I should see an image called "nsi.png"


  Scenario: Showing a especific project
    Given exist a project:
      | name     | description              | logo                          | sponsor | status     | start_date | end_date   |
      | NSI Site | The terrific site of NSI | test/images/projects/nsi.png  | NSI     | finalizado | 2010-11-10 | 2011-02-01 |
      | ERP5     | ERP5, lek                | test/images/projects/erp5.png | NSI     | finalizado | 2010-11-10 | 2011-02-01 |
      
    And exist a member:
      | name   |
      | Pluck  |
      | Batata |
      | Pedro  |  
      
    And "Pluck" member started participation on "NSI Site" project
    And "Batata" member started participation on "NSI Site" project
    And "Pedro" member started participation on "ERP5" project
    
    When I go to the "NSI Site" project page 
    And I should see "NSI Site"
    And I should see "The terrific site of NSI"
    And I should see "Patrocinador: NSI"
    And I should see "Status: finalizado"
    And I should see "Duração: 10/11/2010 a 01/02/2011"
    And I should see an image called "nsi.png"
    And I should see "Pluck"
    And I should see "Batata"

