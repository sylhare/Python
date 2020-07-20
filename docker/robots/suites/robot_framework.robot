*** Settings ***
Force Tags          RobotTestCase


*** Variables ***

${robotVar} =            FooBarBaz


*** Test Cases ***

Foo Test Case
    [tags]              RobotWebPage
    Log     ${robotVar}
