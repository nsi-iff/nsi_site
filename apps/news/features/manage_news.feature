Feature: News maintenance
  As a NSI site administrator
  I want to handle news data
  In order to know details about whats happening at NSI
  
  Scenario: showing a new
    Given exist a author "rogerio" with email "rogerio@gmail.com" and password "rogerio"
    And exist a project:
      | name     | description              | logo                    | sponsor | status | start_date | end_date   |
      | NSI Site | The terrific site of NSI | images/projects/nsi.png | NSI     | aberto | 2010-11-10 | 2011-02-01 |
    And exist a new with title "Notícia sobre o NSI Site", summary "O site do NSI está no ar", body "Já está no ar o site do NSI!", image "images/projects/nsi.png", author "rogerio", date and time "15/01/2011 20:00" and project "NSI Site"
    When I go to "the news page"
    Then I should see "Notícia sobre o NSI Site"
    And I should see "O site do NSI está no ar"
    And I should see "Já está no ar o site do NSI!"
    And I should see an image called "nsi.png"
    And I should see "Postado por: rogerio"
    And I should see "Data: 15/01/2011 às 20:00"
    And I should see "Projeto: NSI Site"
