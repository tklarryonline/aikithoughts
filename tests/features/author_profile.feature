Feature: Homepage and blog posts
    As a visitor
    I want to see the homepage with posts list

    Background:
        Given the website is on

    Scenario: Visit homepage
        When I visit the homepage
        Then I should see "Home - Aikithoughts" in the page title
        And I should see text "Hello, world!"