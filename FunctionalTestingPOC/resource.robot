*** Settings ***
Documentation       A resource file with keywords and variables for tests

Library             lib/WebServiceMockLib.py
Library             lib/SampleIntegrationAppLib.py
Library             lib/DataBaseLib.py
Library             Collections

*** Variables ***
${PORT}
${SERVER}           localhost:${PORT}
${PROCESS_URL}      http://${SERVER}/process
${VALIDATION_URL}   http://${SERVER}/validation
${KILL_URL}         http://${SERVER}/kill

*** Keywords ***
Start The Mock Web API Service And Setup Schema
    init database
    Start API Web Service
    init process endpoint
    init validate endpoint

Kill The Server And Truncate The Schema
    Stop API Web Service
    truncate database
