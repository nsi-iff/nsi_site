Feature: Wiki maintenance
  As a visitor NSI Site
  I want see home wiki data
  In order to learn more about Plone


  Scenario: listing all wiki items

    Given exist a wiki item:
      | id | title               | content                        |
      |  1 | Adding a Plone Site | Just click in 'Add Plone Site' |
      |  2 | Installing Plone 4  | Run "install.sh"               |

    When I go to "the NSI home page"
    And I click "Wiki"

    Then I should see a link with text "Adding a Plone Site"
    And I should have a link that ends in "1/editar/"
    And I should have a link that ends in "1/excluir/"
    And I should see a link with text "Installing Plone 4"
    And I should have a link that ends in "2/editar/"
    And I should have a link that ends in "2/excluir/"


  Scenario: adding some item to the wiki

    When I go to "the NSI home page"
    And I click "Wiki"
    And I click "Adicionar um ítem"
    And I fill in "title" with "Teste"
    And I fill in "content" with "Conteúdo do teste"
    And I press "enviar"
    Then I should see "Ítem salvo com sucesso"
    And I should see a link with text "Voltar para a wiki"


  Scenario: viewing a wiki item

    Given exist a wiki item:
      | id | title               | content                        |
      |  1 | Adding a Plone Site | Just click in 'Add Plone Site' |

    When I go to "the NSI home page"
    And I click "Wiki"
    And I click "Adding a Plone Site"

    Then I should see "Adding a Plone Site"
    And I should see "Just click in 'Add Plone Site'"
