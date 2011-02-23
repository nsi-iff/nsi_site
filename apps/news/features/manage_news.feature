Feature: News maintenance
  As a NSI site administrator
  I want to handle news data
  In order to know details about whats happening at NSI
  
  Scenario: showing a news
    Given exist a author "rogerio" with email "rogerio@gmail.com" and password "rogerio"
    And exist a project:
      | name     | description              | logo                    | sponsor | status | start_date | end_date   |
      | NSI Site | The terrific site of NSI | images/projects/nsi.png | NSI     | aberto | 2010-11-10 | 2011-02-01 |    
    And exist a news:
      | title    |  summary | body | image | author | datetime | 
      | Notícia sobre o NSI Site | O site do NSI está no ar | Já está no ar o site do NSI! | images/projects/nsi.png | rogerio | 15/01/2011 20:00 
    And the news "Notícia sobre o NSI Site" is related with project "NSI Site"
    When I go to "the news page"
    Then I should see "Notícia sobre o NSI Site"
    And I should see "O site do NSI está no ar"
    And I should see "Já está no ar o site do NSI!"
    And I should see an image called "nsi.png"
    And I should see "Postado por: rogerio"
    And I should see "Data: 15/01/2011 às 20:00"
    And I should have "<li>NSI Site</li>" as HTML
    
    Scenario: showing many news 
    Given exist a author "rogerio" with email "rogerio@gmail.com" and password "rogerio"
    And exist a author "ronaldo" with email "ronaldo@gmail.com" and password "ronaldo"
    And exist a author "herman" with email "rosa@gmail.com" and password "caldara"
    And exist a project:
      | name     | description              | logo                     | sponsor | status | start_date | end_date   |
      | NSI Site | The terrific site of NSI | images/projects/nsi.png  | NSI     | aberto | 2010-11-10 | 2011-02-01 |
      | ERP5     | Free ERP                 | images/projects/erp5.png | NSI     | aberto | 2007-01-01 | 2011-02-01 |
      
    And exist a news:
      | title    |  summary | body | image | author | datetime | 
      | Notícia sobre o NSI Site | O site do NSI está no ar | Já está no ar o site do NSI! | images/projects/nsi.png | rogerio | 15/01/2011 20:00 | NSI Site 
      | Notícia sobre o ERP5 Lek | Rick Rock Sunshine Project | ERP5 Lek, muita coisa pronta | images/projects/erp5.png | ronaldo | 16/01/2011 20:00 | ERP5 
      | Notícia sobre o ERP5 e o NSI Site | Rick Rock Sunshine Project NSI e ERP5 | NSI power site e ERP5 Lek, muita coisa pronta | images/projects/nsi.png | herman | 16/01/2011 23:00 | ERP5 NSI Site 
      
    And the news "Notícia sobre o NSI Site" is related with project "NSI Site"
    And the news "Notícia sobre o ERP5 Lek" is related with project "ERP5"
    And the news "Notícia sobre o ERP5 e o NSI Site" is related with project "ERP5" 
    And the news "Notícia sobre o ERP5 e o NSI Site" is related with project "NSI Site"
    When I go to "the news page"
    Then I should see "Notícia sobre o NSI Site"
    And I should see "O site do NSI está no ar"
    And I should see "Já está no ar o site do NSI!"
    And I should see an image called "nsi.png"
    And I should see "Postado por: rogerio"
    And I should see "Data: 15/01/2011 às 20:00"
    And I should see "NSI Site"
    
    And I should see "Notícia sobre o ERP5 Lek"
    And I should see "Rick Rock Sunshine Project"
    And I should see "ERP5 Lek, muita coisa pronta"
    And I should see an image called "erp5.png"
    And I should see "Postado por: ronaldo"
    And I should see "Data: 16/01/2011 às 20:00"
    And I should see "ERP5"
    
    And I should see "Notícia sobre o ERP5 e o NSI Site"
    And I should see "Rick Rock Sunshine Project NSI e ERP5"
    And I should see "NSI power site e ERP5 Lek, muita coisa pronta"
    And I should see an image called "nsi.png"
    And I should see "Postado por: herman"
    And I should see "Data: 16/01/2011 às 23:00"
    And I should have "<li>ERP5</li>" as HTML
    And I should have "<li>NSI Site</li>" as HTML
