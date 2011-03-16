Feature: Tool maintenance
  As a NSI site administrator
  I want to handle tools data
  In order to keep tools information up to date

  Scenario: showing all tools
    Given there exist a tool:
      | name     | description | repository | site | highlight |
      | Should DSL| A tool to write should expectations | http://github.com/hugobr/should-dsl | http://www.should-dsl.info | True |
      | Ludibrio | A tool for mock | http://github.com/nsigustavo/ludirbio | http://www.ludibrio.info | True |
      | Ricks | A tool for sunshine | http://github.com/ronaldoamaral/ricks | http://www.ricks.info | True |
    And given there exist a project:
      | name     |
      | NSI Site |
      | BD       |
    And "Should DSL" has related projects:
      | name     |
      | NSI Site |
    And "Ludibrio" has related projects:
      | name     |
      | BD       |
    And "Ricks" has related projects:
      | name     |
      | BD       |
      | NSI Site | 
    
    When I go to "the tools page"
    Then I should see "Should DSL"
    And I should see "A tool to write should expectations"
    And I should see "http://github.com/hugobr/should-dsl"
    And I should see "http://www.should-dsl.info"
    And I should see "Projetos relacionados:"
    And I should see "NSI Site"
    And I should see "Ludibrio"
    And I should see "A tool for mock"
    And I should see "http://github.com/nsigustavo/ludirbio"
    And I should see "http://www.ludibrio.info"
    And I should see "Projetos relacionados:"
    And I should see "BD"
    And I should see "Ricks"
    And I should see "A tool for sunshine"
    And I should see "http://github.com/ronaldoamaral/ricks"
    And I should see "http://www.ricks.info"
    And I should see "Projetos relacionados:"
    And I should see "BD"
    And I should see "NSI Site"
