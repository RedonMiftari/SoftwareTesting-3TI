Feature: Testen van navigeren tussen de verschillende pages

  Scenario: Ik kan van de homepage naar de blog page gaan
    Given Ik ben op de homepage
    When Ik op de "Go to blog" link met id "blog-link" klik
    Then Ben ik op de blog page