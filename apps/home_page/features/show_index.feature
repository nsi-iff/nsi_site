Feature: User visitor
  As a visitor NSI Site
  I want see home index data

  Scenario: showing News in index home
    Given exist a author:
      | name |
      | herman |
      | ronaldo |
    Given exist a news:
      | title    | image | author | date_and_time |
      | Notícia sobre o NSI Site | test/images/news/nsi.png | herman | 15/01/2011 20:00 |
      | Notícia sobre o ERP5 Lek | test/images/news/erp5.png | herman | 05/04/2011 20:00 |
      | Notícia sobre o ERP5 e o NSI Site | test/images/news/x.png | ronaldo | 01/01/2010 20:00 |
        
    When I go to "the NSI home page"
    And I should see "Notícia sobre o NSI Site"
    And I should see an image called "nsi.png"
    And I should see "Postado por: herman"
    And I should see "15/01/2011"

    And I should see "Notícia sobre o ERP5 Lek"
    And I should see an image called "erp5.png"
    And I should see "Postado por: herman"
    And I should see "05/04/2011"

    And I should see "Notícia sobre o ERP5 e o NSI Site"
    And I should see an image called "x.png"
    And I should see "Postado por: ronaldo"
    And I should see "01/01/2010"
    
  Scenario: showing a open Projects in index home
    Given exist a project:
      | name      | status | 
      | NSI Site  | aberto |
      | ERP5 Lek  | aberto |
      | Abodorock | aberto |
      | Batata Ricks | finalizado |
        
    When I go to "the NSI home page"
    And I should see "NSI Site"
    And I should see "ERP5 Lek"
    And I should see "Abodorock"
    
  Scenario: showing a highlight Tools in index home
    Given exist a tool:
      | name        | highlight | 
      | Should-dsl  | True      |
      | Ludibrio    | True      |
      | rock-py     | False     |
      | Restful-py  | True      |
        
    When I go to "the NSI home page"
    And I should see "Should-dsl"
    And I should see "Ludibrio"
    And I should see "Restful-py"
