Feature: Input forms demo
This feature is to verify the input form structure

  Background:
    Given user is in LambdaTest Selenium Playground Page

  Scenario: Verify User Can fillup form
    Given user has navigated to the form demo Page
    When user enters name "Deep Adhikary"
    And user enters email "adhikary33@gmail.com"
    And user enters password "S3rect"
    And user enters company "123 Pty Ltd"
    And user enters website "https://linkedp.com"
    And user selects country as "India"
    And user enters city as "Kolkata"
    And user enters address line 1 as "123 Main Street"
    And user enters address line 2 as "Complex Nagar"
    And user enter state as "West Bengal"
    And user enters zip code as "743318"
    And user clicks on submit button
    Then Form should be submitted
    And success message "Thanks for contacting us, we will get back to you shortly." is displayed

  Scenario: Verify User can fill data in input form
    Given user has navigated to the form demo Page
    When user enters personal informations
      | Field    | Value                |
      | name     | Deep Adhikary        |
      | email    | adhikary33@gmail.com |
      | password | s3rect               |
      | company  |          123 Pty Ltd |
      | website  | https://linkedp.com  |
    And user enters address informations
      | Field          | Value           |
      | country        | India           |
      | city           | Kolkata         |
      | address line 1 | 123 Main Street |
      | address line 2 | Complex Nagar   |
      | state          | West Bengal     |
      | zip            |          743318 |
    And user clicks on submit button
    Then Form should be submitted
    And success message "Thanks for contacting us, we will get back to you shortly." is displayed

  Scenario Outline: Verify form submission <test id>
    Given user has navigated to the form demo Page
    When user enters personal informations
      | Field    | Value      |
      | name     | <name>     |
      | email    | <email>    |
      | password | <password> |
      | company  | <company>  |
      | website  | <website>  |
    And user enters address informations
      | Field          | Value            |
      | country        | <country>        |
      | city           | <city>           |
      | address line 1 | <address line 1> |
      | address line 2 | <address line 2> |
      | state          | <state>          |
      | zip            | <pin code>       |
    And user clicks on submit button
    Then Form should be submitted
    And success message "Thanks for contacting us, we will get back to you shortly." is displayed

    Examples:
      | test id | name          | email                     | password   | company         | website             | country        | city     | address line 1 | address line 2 | state  | pin code |
      |       1 | Sarah Johnson | sarah.johnson@example.com | Passw0rd   | ABC Inc         | https://abcinc.com  | United States  | New York |     123 Elm St | Apt 101        | NY     |    10001 |
      |       2 | David Smith   | david.smith@example.com   | StrongP@ss | XYZ Corporation | https://xyzcorp.com | Canada         | Toronto  |     456 Oak St | Suite 200      | ON     | M5V 2G8  |
      |       3 | Maria Garcia  | maria.garcia@example.com  | Secure123! | QWE Ltd         | https://qweltd.com  | Spain          | Madrid   |   789 Maple St | Floor 3        | Madrid |    28001 |
      |       4 | Kevin Brown   | kevin.brown@example.com   | Brownie12  | RST Corporation | https://rstcorp.com | Australia      | Sydney   |    456 King St | Unit 20        | NSW    |     2000 |
      |       5 | Emma Wilson   | emma.wilson@example.com   | EmmaPW123  | UVW Inc         | https://uvwinc.com  | United Kingdom | London   |   789 Baker St | Apt 5          | London | SW1A 1AA |
