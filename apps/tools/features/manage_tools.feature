Feature: Tool maintenance
  As a NSI site administrator
  I want to handle tools data
  In order to keep tools information up to date
  
  Scenario: showing a tool
    Given exist a tool:
      | name     | description | repository | site | logo | status | highlight | 
      | Should DSL| A tool to write should expectations | http://github.com/hugobr/should-dsl | http://www.should-dsl.info | test/images/tools/should-dsl.png | ativo | True |
      
    And given there exist a project:
      | name     |
      | NSI Site |
      
    And "Should DSL" has related projects:
      | name     |
      | NSI Site |
      
    When I go to the "Should DSL" tool page 
    Then I should see an image called "should-dsl.png"
    And I should see "Should DSL"
    And I should see "A tool to write should expectations"
    And I should see "http://github.com/hugobr/should-dsl"
    And I should see "http://www.should-dsl.info"
    And I should see "Status: ativo"
    And I should see "Projetos relacionados:"
    And I should see "NSI Site"

  Scenario: showing all tools
    Given exist a tool:
      | name        | short_description                   | logo                             | status        |
      | Should DSL  | A tool to write should expectations | test/images/tools/should-dsl.png | ativo         |
      | Ludibrio    | A tool for mock                     | test/images/tools/ludibrio.png   | descontinuado |
      | Ricks       | A tool for sunshine                 | test/images/tools/ricks.png      | ativo         |
    
    When I go to "the tools page"
    Then I should see an image called "should-dsl.png"
    And I should see "Should DSL"
    And I should see "A tool to write should expectations"
    And I should see "Status: ativo"
    And I should see an image called "ludibrio.png"
    And I should see "Ludibrio"
    And I should see "A tool for mock"
    And I should see "Status: descontinuado"
    And I should see an image called "ricks.png"
    And I should see "Ricks"
    And I should see "A tool for sunshine"
    And I should see "Status: ativo"
