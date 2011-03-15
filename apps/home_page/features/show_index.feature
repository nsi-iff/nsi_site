Feature: User visitor
  As a visitor NSI Site
  I want see home index data

  Scenario: showing News in index home
    Given exist a news:
      | title    |
      | Notícia sobre o NSI Site | 
      | Notícia sobre o ERP5 Lek | 
      | Notícia sobre o ERP5 e o NSI Site |
        
    When I go to "the NSI home page"
