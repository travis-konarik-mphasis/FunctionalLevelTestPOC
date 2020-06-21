*** Settings ***
Documentation   A test suite for testing processing of records that are valid but there is an error during processing

Resource        resource.robot

Test Setup      Start The Mock Web API Service And Setup Schema
Test Teardown   Kill The Server And Truncate The Schema

*** Test Cases ***
GatewayTimeout
    ${batch}        create batch in database  B0001
    ${batch_id}     get from list   ${batch}    0
    ${initial_record_status}     convert to integer  1
    ${record}        add record to batch  ${batch_id}    C0001   ${initial_record_status}
    set validate endpoint to return json  {"Result": "Success"}
    set process endpoint to gateway timeout
    Run The Integration App
    ${record_id}     get from list   ${record}    0
    ${responses}    get responses for record     ${record_id}
    ${response_count}   get length  ${responses}
    ${expected_response_count}  convert to integer  1
    should be equal  ${expected_response_count}  ${response_count}
    ${response}   get from list  ${responses}   0
    ${response_processing_status}   get from list  ${response}  2
    ${processed_status}     convert to integer  5
    should be equal  ${processed_status}  ${response_processing_status}
    ${response_json}    get from list   ${response}     3
    should be equal  {"Result": "Error Processing", "Reason": "Continuous Gateway Timeout"}     ${response_json}
    ${record}    get record  ${record_id}
    ${record_processing_status}   get from list  ${record}  3
    should be equal  ${processed_status}  ${record_processing_status}
