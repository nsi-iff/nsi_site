Feature: Funding maintenance
  As a NSI member
  I want to maintain funding data
  In order to keep the site up to date regarding our funding


  Scenario Outline: Funding inclusion
    Given I am on the new funding page
    When I fill in "title" with "<title>"
    And I fill in "source" with "<source>"
    And I fill in "description" with "<description>"
    And I fill in "year" with "<year>"
    And I fill in "student grants" with "<student grants>"
    And I fill in "researchers grants" with "<researchers grants>"
    And I fill in "materials" with "<researchers grants>"
    And I fill in "others" with "<others>"
    And I press "Save"
    Then I should see "Funding": "<title>"
    And I should see "Source": "<source>"
    And I should see "Description": "<description>"
    And I should see "Year of Release" with "<year>"
    And I should see "Total in Student Grants" with "<student grants>"
    And I should see "Total in Researchers Grants" with "<researchers grants>"
    And I should see "Total in Materials" with "<researchers grants>"
    And I should see "Total in others items" with "<others>"

  Examples:
    | title             | source    | description                                        | year | student grants | researchers grants | materials |
    | Setec budget 2011 | Setec/MEC | Digital library and other projects budget for 2011 | 2011 | 100,000        | 100,000            | 10,000    |

  Scenario Outline: Funding update
    Given I am on the update funding page
    And I select "Setec budget 2011" funding for editing
    When I fill in "title" with "<title>"
    And I fill in "source" with "<source>"
    And I fill in "description" with "<description>"
    And I fill in "year" with "<year>"
    And I fill in "student grants" with "<student grants>"
    And I fill in "researchers grants" with "<researchers grants>"
    And I fill in "materials" with "<researchers grants>"
    And I fill in "others" with "<others>"
    And I press "Save"
    Then I should see "Funding": "<title>"
    And I should see "Source": "<source>"
    And I should see "Description": "<description>"
    And I should see "Year of Release" with "<year>"
    And I should see "Total in Student Grants" with "<student grants>"
    And I should see "Total in Researchers Grants" with "<researchers grants>"
    And I should see "Total in Materials" with "<researchers grants>"
    And I should see "Total in others items" with "<others>"

  Examples:
    | title        | source    | description                                      | year | student grants | researchers grants | materials |
    | Setec budget | Setec/MEC | Digital library and sub-projects budget for 2011 | 2011 | 100,000        | 50,000             | 1,000     |

  Scenario Outline: Funding delete
   Given I am on the delete funding page
   And I select "<funding name>", "<funding source>", "<funding year>" funding for deleting
   When I press "Delete"
   Then I should see the message "Funding successfully deleted"
   And the "<funding name>", "<funding source>", "<funding year>" funding does not exist anymore

  Examples:
    | title        | source    | year |
    | Setec budget | Setec/MEC | 2011 |

