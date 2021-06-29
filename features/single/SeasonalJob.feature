Feature: "Transition from Military to Civilian Life"

Scenario: As a Veteran, I need to obtain information on how to transition out of the Military
    Given I am on "https://www.dol.gov/agencies/vets"
    When I get click "Transition Assistance Program"
    Then the user should get a result with "Transistion Assitance Program"



