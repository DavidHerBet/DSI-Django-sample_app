Feature: Probando BDD en Django

    Scenario: Home page
        Given I access the url "/sample_app/home"
        Then I see the header "Sample App"