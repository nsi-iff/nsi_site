Feature: User visitor
  As a visitor NSI Site
  I want see home index data

  Scenario: showing News in index home
    Given exist a news:
      | title    | summary |
      | Notícia sobre o NSI Site | Esta é uma noticia sobre o NSI Site | 
      | Notícia sobre o ERP5 Lek | Esta é uma noticia sobre o ERP5 Lek |
      | Notícia sobre o ERP5 e o NSI Site | Esta é uma noticia sobre o ERP5 e o NSI Site |
        
    When I go to "the NSI home page"
    And I should see "Notícia sobre o NSI Site "
    And I should see "Esta é uma noticia sobre o NSI Site"
    And I should see "Notícia sobre o ERP5 Lek"
    And I should see "Esta é uma noticia sobre o ERP5 Lek"
    And I should see "Notícia sobre o ERP5 e o NSI Site"
    And I should see "Esta é uma noticia sobre o ERP5 e o NSI Site"
    
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
