Feature: Wiki maintenance
  As a visitor NSI Site
  I want see home wiki data
  In order to learn more about Plone

  Scenario: adding some item to the wiki

    When I go to "the NSI home page"
    And I click "Wiki"
    And I click "Adicionar um ítem"
    And I fill in "title" with "Teste"
    And I fill in "content" with "Conteúdo do teste"
    And I press "enviar"
    Then I should see "Ítem salvo com sucesso"
    And I should see a link with text "Voltar para a wiki"
