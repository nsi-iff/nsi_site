Feature: Member maintenance
  As a NSI site administrator
  I want to handle member data
  In order to know details about at member

  Scenario: member page that just have only one team
    Given exist a member:
      | name | current_team | currently_does | life_and_work | site | github | twitter | slideshare | lattes | photo | project_memberships | started_nsi_date |

      | Pluck | Renapi | Phd em Desenvolvimento de software, bolsista do NSI desde das trevas | Atualmente trabalha como suporte de madeira | http://www.pluck.com | http://github.com/pluck | http://twitter.com/pluck | http://slideshare.com/pluck | http://lattes.cnpq.br/pluck | pluck_photo.png | Biblioteca Digital | 2000-01-01  |  
    When I go to the "Pluck" member page 
    Then I should see "Pluck"
    And I should see "Phd em Desenvolvimento de software, bolsista do NSI desde das trevas"
    And I should see "Atualmente trabalha como suporte de madeira"
    And I should see "Site: http://www.pluck.com"
    And I should see "Github: http://github.com/pluck"
    And I should see "Twitter: http://twitter.com/pluck"
    And I should see "SlideShare: http://slideshare.com/pluck"
    And I should see "Curriculo Lattes: http://lattes.cnpq.br/pluck"
    And I should see an image called "pluck_photo.png"
    And I should see "Biblioteca Digital"
    And I should see "01/01/2000"
