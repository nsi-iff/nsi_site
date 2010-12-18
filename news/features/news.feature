Feature: News maintenance
  As a NSI member
  I want to maintain news data
  In order to keep the site up to date regarding our news


  Scenario Outline: News inclusion
    Given I am on the new news page
    When I fill in "title" with "<title>"
    And I fill in "summary" with "<summary>"
    And I fill in "body" with "<body>"
    And I attach to "image" the "<image>"
    And I fill in "publication_date" with "<publication_date>"
    And I press "Save"
    Then I should see "Title": "<title>"
    And I should see "Summary": "<summary>"
    And I should see "Body": "<body>"
    And I should see "Image": "images/news/<image>"
    And I should see "Publication Date": "<publication_date>"

  Examples:
    | title            | summary                         | body                                             | image       | publication_date |
    | world domination | NSI plans to conquer the galaxy | NSI plans to conquer the galaxy in the next year | milkway.jpg | 15/12/2010       |
    | ERP5Br was born  | many things ready, lek          | ERP5Br was born                                  | erp5br.png  | 11/12/2010       |


  Scenario Outline: News update
    Given I have the following news:
     | title             | summary                             | body                                                    | image         | publication_date |
     | general agreement | NSI plans to be loved by all people | NSI plans to do some software to be loved by all people | obemamado.jpg | 2010-12-16       |
    And I am on the "general agreement" news edit page
    When I fill in "title" with "<title>"
    And I fill in "summary" with "<summary>"
    And I fill in "body" with "<body>"
    And I attach to "image" the "<image>"
    And I fill in "publication_date" with "<publication_date>"
    And I press "Save"
    Then I should see "Title": "<title>"
    And I should see "Summary": "<summary>"
    And I should see "Body": "<body>"
    And I should see "Image": "images/news/<image>"
    And I should see "Publication Date": "<publication_date>"

  Examples:
    | title            | summary                             | body                                                    | image         | publication_date |
    | world domination | NSI plans to be loved by all people | NSI plans to do some software to be loved by all people | obemamado.jpg | 16/12/2010       |


  Scenario Outline: News delete
   Given I have the following news:
     | title            | summary                             | body                                                    | image         | publication_date |
     | world domination | NSI plans to be loved by all people | NSI plans to do some software to be loved by all people | obemamado.jpg | 2010-12-16       |
   And I am on the "<news>" news delete page
   When I press "Delete"
   Then I should see the message "News successfully deleted"
   And the "<news>" news does not exist

  Examples:
   | news             |
   | world domination |

