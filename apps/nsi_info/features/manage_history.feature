Feature: NSI info maintenance
  As a NSI site administrator
  I want to maintain NSI-related data
  In order to keep people informed about the glorious NSI

  Scenario Outline: Info page
    Given current <field> is "Hello, we are the glorious NSI."
    When I go to "the <field> page"
    Then I should see "Hello, we are the glorious NSI."

    Examples:
      | field   |
      | about   |

  Scenario Outline: Accepts restructuredText format input
    Given current <field> is "*NSI* rules!"
    When I go to "the <field> page"
    Then I should have "<em>NSI</em> rules!" as HTML

    Examples:
      | field   |
      | about   |
