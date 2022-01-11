Feature: Test navigation between pages
  # Hier kan een descriptie geschreven worden


  Scenario: Homepage can go to Blog
    Given I am on the homepage
    When I click on the link with id "blog-link"
    Then I am on the blog page