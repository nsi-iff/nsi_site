Feature: Wiki maintenance
  As a visitor NSI Site
  I want see home wiki data
  In order to learn more about Plone


  Scenario: listing all wiki items without be logged in

    Given exist a wiki item:
      | id | title               | content                        |
      |  1 | Adding a Plone Site | Just click in 'Add Plone Site' |
      |  2 | Installing Plone 4  | Run "install.sh"               |

    When I go to "the NSI home page"
    And I click "Wiki"

    Then I should see a link with text "Adding a Plone Site"
    And I should see a link with text "Installing Plone 4"


  Scenario: listing all wiki items logged in

    Given exist a wiki item:
      | id | title               | content                        |
      |  1 | Adding a Plone Site | Just click in 'Add Plone Site' |
      |  2 | Installing Plone 4  | Run "install.sh"               |
    And that i'm logged in

    When I go to "the NSI home page"
    And I click "Wiki"

    Then I should see a link with text "Adding a Plone Site"
    And I should have a link that ends in "adding-a-plone-site/editar/"
    And I should have a link that ends in "adding-a-plone-site/excluir/"
    And I should see a link with text "Installing Plone 4"
    And I should have a link that ends in "installing-plone-4/editar/"
    And I should have a link that ends in "installing-plone-4/excluir/"


  Scenario: adding some item to the wiki

    Given that i'm logged in

    When I go to "the NSI home page"
    And I click "Wiki"
    And I click "Adicionar um item"
    And I fill in "title" with "Teste"
    And I fill in "nicEdit-main" with "Conteúdo do teste"
    And I press "send"
    Then I should see "Item salvo com sucesso!"
    And I should see a link with text "Voltar para a wiki"


  Scenario: viewing a wiki item

    Given exist a wiki item:
      | id | title               | content                        |
      |  1 | Adding a Plone Site | Just click in 'Add Plone Site' |

    When I go to "the NSI home page"
    And I click "Wiki"
    And I should have a link that ends in "adding-a-plone-site/"
    And I click "Adding a Plone Site"

    Then I should see "Adding a Plone Site"
    And I should see "Just click in 'Add Plone Site'"


  Scenario: editing some wiki item

    Given exist a wiki item:
      | id | title               | content                        |
      |  1 | Adding a Plone Site | Just click in 'Add Plone Site' |
    And that i'm logged in

    When I go to "the NSI home page"
    And I click "Wiki"
    And I click on link that ends in "adding-a-plone-site/editar/"
    And I fill in "title" with "How to install django"
    And I fill in "nicEdit-main" with "Run: pip install django"
    And I press "send"

    Then I should see "Item editado com sucesso!"
    And I should see a link with text "Voltar para a wiki"


  Scenario: deleting some wiki item

    Given exist a wiki item:
      | id | title               | content                        |
      |  1 | Adding a Plone Site | Just click in 'Add Plone Site' |
    And that i'm logged in

    When I go to "the NSI home page"
    And I click "Wiki"
    And I click on link that ends in "adding-a-plone-site/excluir/"
    And I should see "Deseja excluir o item 'Adding a Plone Site'?"
    And I press "yes"

    Then I should see "Item excluído com sucesso!"
    And I should see a link with text "Voltar para a wiki"


  Scenario: giving up of deleting some wiki item

    Given exist a wiki item:
      | id | title               | content                        |
      |  1 | Adding a Plone Site | Just click in 'Add Plone Site' |
    And that i'm logged in

    When I go to "the NSI home page"
    And I click "Wiki"
    And I click on link that ends in "adding-a-plone-site/excluir/"
    And I should see "Deseja excluir o item 'Adding a Plone Site'?"
    And I press "no"

    Then I should see a link with text "Adding a Plone Site"
    And I should have a link that ends in "adding-a-plone-site/editar/"
    And I should have a link that ends in "adding-a-plone-site/excluir/"
