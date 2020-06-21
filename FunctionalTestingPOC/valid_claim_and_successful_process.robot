*** Settings ***
Documentation   A test suite for testing processing of records that are valid and successfully processed

Resource        resource.robot

Test Setup      Start The Mock Web API Service And Setup Schema
Test Teardown   Kill The Server And Truncate The Schema

*** Test Cases ***
Basic record
    ${batch}        create batch in database  B0001
    ${batch_id}     get from list   ${batch}    0
    ${initial_record_status}     convert to integer  1
    ${record}        add record to batch  ${batch_id}    C0001   ${initial_record_status}
    ${processing_json}    set variable  {"output": "Test"}
    set validate endpoint to return json  {"Result": "Success"}
    set process endpoint to return json  ${processing_json}
    Run The Integration App
    ${record_id}     get from list   ${record}    0
    ${responses}    get responses for record     ${record_id}
    ${response_count}   get length  ${responses}
    ${expected_response_count}  convert to integer  1
    should be equal  ${expected_response_count}  ${response_count}
    ${response}   get from list  ${responses}   0
    ${response_processing_status}   get from list  ${response}  2
    ${processed_status}     convert to integer  6
    should be equal  ${processed_status}  ${response_processing_status}
    ${response_json}    get from list   ${response}     3
    should be equal  ${processing_json}     ${response_json}
    ${record}    get record  ${record_id}
    ${record_processing_status}   get from list  ${record}  3
    should be equal  ${processed_status}  ${record_processing_status}

