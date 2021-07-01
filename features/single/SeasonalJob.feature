Feature: "Transition from Military to Civilian Life"

Scenario: As a Veteran, I need to obtain information on how to transition out of the Military
    Given I am on "https://www.dol.gov/agencies/vets"
    When I get click "Transition Assistance Program"
    Then the user should get a result with "Transistion Assitance Program"



Feature: "Construction Worker Looking for Project"

Scenario: As construction worker, I am looking for my next construction project
    Given I am on "https://seasonaljobs.dol.gov/"
    When I click "Construction Laborers"
    Then the suser should get a result with "Construction Laborers"